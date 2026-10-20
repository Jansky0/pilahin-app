import {
  launchBrowser,
  createPage,
  openApp,
  switchTab,
  getWalletBalance,
  getToastText,
  assert,
  assertEqual,
  delay
} from './helpers.js';

export const name = 'Tier 3: Cross-Feature Combinations (Full Circular Loop)';

export async function run() {
  const browser = await launchBrowser();
  const page = await createPage(browser);
  const results = [];

  try {
    // -------------------------------------------------------------------------
    // Test 3.1: Full Circular Loop Transaction Flow
    // Reference: ORIGINAL_REQUEST R2 & R4, PROJECT.md Core Circular Loop
    // Flow: Setor Sampah -> Timbang -> Saldo Naik -> Belanja Toko -> Saldo Turun -> Tarik E-Wallet
    // -------------------------------------------------------------------------
    await (async () => {
      const testName = '3.1: Complete Closed-Loop Circular Economy Transaction Sequence';
      try {
        await openApp(page);

        // --- STEP 1: Capture Baseline Balance B0 in Dompet ---
        await switchTab(page, 'dompet');
        const B0 = await getWalletBalance(page);
        assert(B0 > 0, `Initial wallet balance invalid: ${B0}`);

        // --- STEP 2: Setor Sampah (Create Deposit Ticket) ---
        await switchTab(page, 'setor');

        // Select pickup method
        await page.evaluate(() => {
          const divs = Array.from(document.querySelectorAll('div'));
          const pickupDiv = divs.find(d => d.innerText && d.innerText.includes('Minta Jemput Mitra'));
          if (pickupDiv) pickupDiv.click();
        });
        await delay(300);

        // Read estimated deposit amount from summary card
        const depositEst = await page.evaluate(() => {
          const text = document.body.innerText;
          const m = text.match(/Estimasi Saldo Mengendap Baru:\s*\+Rp\s*([\d.]+)/i);
          return m ? parseInt(m[1].replace(/\./g, ''), 10) : 0;
        });
        assert(depositEst > 0, `Failed to calculate deposit estimate: ${depositEst}`);

        // Click "Buat Tiket & Jadwal Penyetoran"
        await page.evaluate(() => {
          const btns = Array.from(document.querySelectorAll('button'));
          const btn = btns.find(b => b.innerText.includes('Buat Tiket'));
          if (btn) btn.click();
        });
        await delay(500);

        // Verify Ticket Modal Opened
        const ticketCode = await page.evaluate(() => {
          const match = document.body.innerText.match(/PLH-\d{6}/);
          return match ? match[0] : null;
        });
        assert(ticketCode !== null, 'Digital ticket with PLH-XXXXXX code not generated');

        // --- STEP 3: Mitra Verifies Weighing & Credits Saldo ---
        await page.evaluate(() => {
          const btns = Array.from(document.querySelectorAll('button'));
          const btn = btns.find(b => b.innerText.includes('Simulasikan Timbangan Selesai'));
          if (btn) btn.click();
        });
        await delay(600);

        // App automatically redirects to Dompet tab
        const B1 = await getWalletBalance(page);
        const expectedB1 = B0 + depositEst;
        assertEqual(
          B1,
          expectedB1,
          `Balance after deposit credit does not match B0 + depositEst (Expected: ${expectedB1}, Got: ${B1})`
        );

        // --- STEP 4: Belanja Toko Sirkular with Escrow Balance ---
        await switchTab(page, 'toko');

        // Get first product details (Pupuk Kompos @ Rp 18.000)
        const productInfo = await page.evaluate(() => {
          const firstCard = document.querySelector('.bg-white.rounded-2xl.p-3\\.5');
          if (!firstCard) return null;
          const name = firstCard.querySelector('h4') ? firstCard.querySelector('h4').innerText : 'Product';
          const priceMatch = firstCard.innerText.match(/Rp\s*([\d.]+)/);
          const price = priceMatch ? parseInt(priceMatch[1].replace(/\./g, ''), 10) : 0;
          const tukarBtn = firstCard.querySelector('button');
          if (tukarBtn) tukarBtn.click();
          return { name, price };
        });

        assert(productInfo && productInfo.price > 0, 'Could not select store product');
        await delay(500);

        // Confirm Tukar in Modal
        await page.evaluate(() => {
          const btns = Array.from(document.querySelectorAll('button'));
          const confirmBtn = btns.find(b => b.innerText.includes('Konfirmasi Tukar'));
          if (confirmBtn) confirmBtn.click();
        });
        await delay(600);

        // Verify balance after store purchase: B2 = B1 - productInfo.price
        await switchTab(page, 'dompet');
        const B2 = await getWalletBalance(page);
        const expectedB2 = B1 - productInfo.price;
        assertEqual(
          B2,
          expectedB2,
          `Balance after store purchase does not match B1 - price (Expected: ${expectedB2}, Got: ${B2})`
        );

        // --- STEP 5: Tarik Saldo ke E-Wallet (GoPay 50k) ---
        // Click 50000 chip
        await page.evaluate(() => {
          const btns = Array.from(document.querySelectorAll('button'));
          const chip50k = btns.find(b => b.innerText.includes('50.000'));
          if (chip50k) chip50k.click();
        });
        await delay(300);

        // Click Cairkan Sekarang
        await page.evaluate(() => {
          const btns = Array.from(document.querySelectorAll('button'));
          const cairkan = btns.find(b => b.innerText.includes('Cairkan Sekarang'));
          if (cairkan) cairkan.click();
        });
        await delay(600);

        // Verify balance after cashout: B3 = B2 - 50000
        const B3 = await getWalletBalance(page);
        const expectedB3 = B2 - 50000;
        assertEqual(
          B3,
          expectedB3,
          `Balance after e-wallet cashout does not match B2 - 50.000 (Expected: ${expectedB3}, Got: ${B3})`
        );

        // --- STEP 6: Ledger Audit in Dompet ---
        const historyText = await page.evaluate(() => {
          const historyCard = Array.from(document.querySelectorAll('.bg-white.rounded-2xl'))
            .find(c => c.innerText && c.innerText.toLowerCase().includes('riwayat transaksi'));
          return historyCard ? historyCard.innerText : '';
        });

        // Must contain:
        // 1. Credit: Setor Sampah / Timbangan
        // 2. Debit: Beli 1x (Product)
        // 3. Debit: Pencairan Saldo
        assert(historyText.includes('Setor') || historyText.includes('Timbangan'), 'Ledger missing deposit credit entry');
        assert(historyText.includes('Beli') || historyText.includes('Toko'), 'Ledger missing store purchase debit entry');
        assert(historyText.includes('Pencairan') || historyText.includes('Transfer'), 'Ledger missing cashout debit entry');

        results.push({
          name: testName,
          status: 'PASS',
          details: `Lifecycle verified: B0(${B0}) -> +${depositEst} -> -${productInfo.price} -> -50000 -> B3(${B3})`
        });
      } catch (err) {
        results.push({ name: testName, status: 'FAIL', error: err.message });
      }
    })();

  } finally {
    await browser.close();
  }

  return results;
}
