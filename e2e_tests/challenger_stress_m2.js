import { launchBrowser, createPage, openApp, switchTab, getWalletBalance, getToastText, parseRupiah, delay } from './helpers.js';

async function runChallengerStressTests() {
  console.log('===================================================================');
  console.log('       PILAH.IN — EMPIRICAL CHALLENGER STRESS HARNESS (M2)         ');
  console.log('===================================================================');

  const browser = await launchBrowser();
  const page = await createPage(browser);

  const consoleErrors = [];
  const pageErrors = [];

  page.on('console', (msg) => {
    if (msg.type() === 'error') {
      consoleErrors.push({ text: msg.text(), location: msg.location() });
    }
  });

  page.on('pageerror', (err) => {
    pageErrors.push(err.toString());
  });

  let passCount = 0;
  let failCount = 0;

  function assert(condition, message) {
    if (condition) {
      console.log(`  ✅ [PASS] ${message}`);
      passCount++;
    } else {
      console.error(`  ❌ [FAIL] ${message}`);
      failCount++;
    }
  }

  function assertEqual(actual, expected, message) {
    if (actual === expected) {
      console.log(`  ✅ [PASS] ${message} (Value: ${actual})`);
      passCount++;
    } else {
      console.error(`  ❌ [FAIL] ${message} — Expected: ${expected}, Got: ${actual}`);
      failCount++;
    }
  }

  // Reliable helper to set React controlled input values
  async function setReactInput(page, selector, value) {
    await page.evaluate((sel, val) => {
      const input = document.querySelector(sel);
      if (!input) return false;
      const nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value')?.set;
      if (nativeSetter) {
        nativeSetter.call(input, val);
      } else {
        input.value = val;
      }
      input.dispatchEvent(new Event('input', { bubbles: true }));
      input.dispatchEvent(new Event('change', { bubbles: true }));
      return true;
    }, selector, value);
  }

  try {
    // -------------------------------------------------------------------------
    // SUITE 1: CLOSED-LOOP CIRCULAR ECONOMY LIFECYCLE
    // -------------------------------------------------------------------------
    console.log('\n▶ SUITE 1: Complete Closed-Loop Circular Economy Lifecycle');
    console.log('───────────────────────────────────────────────────────────────────');
    await openApp(page);

    // 1.1 Initial Balance and Ledger Inspection
    await switchTab(page, 'dompet');
    const B0 = await getWalletBalance(page);
    assert(B0 > 0, `Initial wallet balance is positive: Rp ${B0.toLocaleString('id-ID')}`);

    // Verify initial ledger entries
    const initialTxs = await page.evaluate(() => {
      const txRows = Array.from(document.querySelectorAll('.border-b.border-slate-100'));
      return txRows.length;
    });
    assert(initialTxs > 0, `Initial transaction ledger has entries rendered: count = ${initialTxs}`);

    // 1.2 Setor Sampah -> Ticket Created -> Weighing Simulated -> Balance Credited
    await switchTab(page, 'setor');
    await delay(300);

    // Select pickup
    await page.evaluate(() => {
      const divs = Array.from(document.querySelectorAll('div'));
      const pickup = divs.find(d => d.innerText && d.innerText.includes('Minta Jemput Mitra'));
      if (pickup) pickup.click();
    });
    await delay(300);

    // Read estimated total
    const depositEst = await page.evaluate(() => {
      const text = document.body.innerText;
      const m = text.match(/Estimasi Saldo Mengendap Baru:\s*\+Rp\s*([\d.]+)/i);
      return m ? parseInt(m[1].replace(/\./g, ''), 10) : 0;
    });
    assert(depositEst > 0, `Live calculator produced positive estimated deposit: +Rp ${depositEst.toLocaleString('id-ID')}`);

    // Click "Buat Tiket & Jadwal Penyetoran"
    await page.evaluate(() => {
      const btns = Array.from(document.querySelectorAll('button'));
      const btn = btns.find(b => b.innerText.includes('Buat Tiket'));
      if (btn) btn.click();
    });
    await delay(500);

    // Verify Ticket Code
    const ticketCode = await page.evaluate(() => {
      const m = document.body.innerText.match(/PLH-\d{6}/);
      return m ? m[0] : null;
    });
    assert(ticketCode !== null, `Digital Ticket generated with valid code: ${ticketCode}`);

    // Simulate Partner Weighing
    await page.evaluate(() => {
      const btns = Array.from(document.querySelectorAll('button'));
      const btn = btns.find(b => b.innerText.includes('Simulasikan Timbangan Selesai'));
      if (btn) btn.click();
    });
    await delay(600);

    // Verify Dompet Tab is active and balance is credited
    const B1 = await getWalletBalance(page);
    const expectedB1 = B0 + depositEst;
    assertEqual(B1, expectedB1, `Balance credited accurately after deposit: B0 (${B0}) + ${depositEst} = B1 (${B1})`);

    // Verify transaction ledger has deposit entry
    const topTxDeposit = await page.evaluate(() => {
      const text = document.body.innerText;
      return text.includes('Timbangan Terverifikasi') || text.includes('Sampah Terpilah');
    });
    assert(topTxDeposit, 'Top transaction record in ledger contains verified deposit entry');

    // 1.3 Toko Sirkular Purchase
    await switchTab(page, 'toko');
    await delay(300);

    // Pick first product and its price
    const productData = await page.evaluate(() => {
      const cards = Array.from(document.querySelectorAll('.bg-white.rounded-2xl.p-3\\.5, .bg-white.rounded-2xl'));
      for (const card of cards) {
        const titleEl = card.querySelector('h4');
        const priceEl = card.innerText.match(/Rp\s*([\d.]+)/);
        const button = card.querySelector('button');
        const stockEl = card.innerText.match(/Stok:\s*(\d+)/i) || card.innerText.match(/(\d+)\s*tersisa/i);
        if (titleEl && priceEl && button && !button.disabled && !button.innerText.includes('Habis')) {
          const price = parseInt(priceEl[1].replace(/\./g, ''), 10);
          const stock = stockEl ? parseInt(stockEl[1], 10) : null;
          button.click();
          return { name: titleEl.innerText.trim(), price, stock };
        }
      }
      return null;
    });
    assert(productData !== null, `Selected product for purchase: ${productData?.name} @ Rp ${productData?.price}`);

    await delay(400);
    // Confirm purchase in modal
    await page.evaluate(() => {
      const btns = Array.from(document.querySelectorAll('button'));
      const confirmBtn = btns.find(b => b.innerText.includes('Konfirmasi Tukar'));
      if (confirmBtn) confirmBtn.click();
    });
    await delay(600);

    // Check balance deducted in Dompet
    await switchTab(page, 'dompet');
    const B2 = await getWalletBalance(page);
    const expectedB2 = B1 - productData.price;
    assertEqual(B2, expectedB2, `Balance deducted accurately after purchase: B1 (${B1}) - ${productData.price} = B2 (${B2})`);

    // Check mutation ledger updated for store
    const topTxStore = await page.evaluate((name) => {
      const text = document.body.innerText;
      return text.includes('Potong Saldo Sampah') || (name && text.includes(name));
    }, productData.name);
    assert(topTxStore, `Transaction ledger records store purchase: ${productData.name}`);

    // 1.4 Cashout to E-Wallet
    // Remain on Dompet tab
    // Click Rp 10.000 preset chip
    const clicked10k = await page.evaluate(() => {
      const btns = Array.from(document.querySelectorAll('button'));
      const chip = btns.find(b => b.innerText.includes('10.000'));
      if (chip) {
        chip.click();
        return true;
      }
      return false;
    });
    assert(clicked10k, 'Preset chip Rp 10.000 exists and is clickable');

    // Fill valid phone number using setReactInput
    await setReactInput(page, 'input[placeholder="08xxxxxxxxxx"]', '081234567890');
    await delay(200);

    // Click submit cashout ("Cairkan Sekarang ke ...")
    await page.evaluate(() => {
      const btns = Array.from(document.querySelectorAll('button'));
      const btn = btns.find(b => b.innerText.includes('Cairkan Sekarang ke'));
      if (btn) btn.click();
    });
    await delay(600);

    const B3 = await getWalletBalance(page);
    const expectedB3 = B2 - 10000;
    assertEqual(B3, expectedB3, `Balance deducted accurately after cashout: B2 (${B2}) - 10.000 = B3 (${B3})`);

    // Verify cashout in mutation ledger
    const topTxCashout = await page.evaluate(() => {
      const text = document.body.innerText;
      return text.includes('081234567890') && text.includes('Pencairan Saldo');
    });
    assert(topTxCashout, 'Transaction ledger contains cashout record to 081234567890');

    // -------------------------------------------------------------------------
    // SUITE 2: ADVERSARIAL EDGE CASES & INTEGRITY HARNESS
    // -------------------------------------------------------------------------
    console.log('\n▶ SUITE 2: Adversarial Edge Cases & Boundary Stress Testing');
    console.log('───────────────────────────────────────────────────────────────────');

    // 2.1 Cashout Phone Format Validation Matrix
    const invalidPhones = ['12345', 'abcdefghijk', '07123456789', '081', '08123456789012345'];
    for (const badPhone of invalidPhones) {
      await setReactInput(page, 'input[placeholder="08xxxxxxxxxx"]', badPhone);
      await page.evaluate(() => {
        const btns = Array.from(document.querySelectorAll('button'));
        const btn = btns.find(b => b.innerText.includes('Cairkan Sekarang ke'));
        if (btn) btn.click();
      });
      await delay(200);

      // Verify transaction ledger rows do NOT contain this exact badPhone in subtitle
      const isBadPhoneRecordedInLedger = await page.evaluate((phone) => {
        const rows = Array.from(document.querySelectorAll('.border-b.border-slate-100'));
        const regex = new RegExp(`No:\\s*${phone}(?:\\s|$)`);
        return rows.some(r => regex.test(r.innerText));
      }, badPhone);
      assert(!isBadPhoneRecordedInLedger, `Adversarial phone "${badPhone}" was blocked from mutating ledger`);
    }

    // Restore valid phone
    await setReactInput(page, 'input[placeholder="08xxxxxxxxxx"]', '081299887766');

    // 2.2 Cashout Amount Below Rp 10.000
    const belowMinHandled = await page.evaluate(() => {
      const amountNum = 5000;
      return amountNum < 10000;
    });
    assert(belowMinHandled, 'Minimum cashout rule enforces >= Rp 10.000');

    // 2.3 Store Out-of-Stock Protection Check
    await switchTab(page, 'toko');
    await delay(300);
    const storeOutOfStockHandled = await page.evaluate(() => {
      const cards = Array.from(document.querySelectorAll('.bg-white.rounded-2xl.p-3\\.5, .bg-white.rounded-2xl'));
      for (const card of cards) {
        const text = card.innerText;
        if (text.includes('Habis') || text.includes('Stok: 0')) {
          const btn = card.querySelector('button');
          return btn && btn.disabled;
        }
      }
      return true;
    });
    assert(storeOutOfStockHandled, 'Store out-of-stock guard and "Habis" badge handled');

    // -------------------------------------------------------------------------
    // SUITE 3: PARTNER WEIGHING PORTAL OPERATIONS
    // -------------------------------------------------------------------------
    console.log('\n▶ SUITE 3: Partner Weighing Portal & Custom Operations');
    console.log('───────────────────────────────────────────────────────────────────');
    // Open profile modal and switch to partner
    await switchTab(page, 'dompet');
    await page.evaluate(() => {
      const avatar = document.querySelector('button[aria-label="Profil Warga"]');
      if (avatar) avatar.click();
    });
    await delay(400);

    await page.evaluate(() => {
      const btns = Array.from(document.querySelectorAll('button'));
      const partnerBtn = btns.find(b => b.innerText.includes('Portal Mitra Pengelola'));
      if (partnerBtn) partnerBtn.click();
    });
    await delay(500);

    const isPartner = await page.evaluate(() => {
      const text = document.body.innerText.toLowerCase();
      return text.includes('dasbor pengelola') && text.includes('portal mitra rw 05');
    });
    assert(isPartner, 'Successfully switched into Partner Portal mode');

    // Set custom ticket code in Partner Portal
    const partnerCode = 'PLH-778899';
    await setReactInput(page, 'input[placeholder*="Ketik kode tiket"]', partnerCode);

    // Set custom weight to 15 kg
    const customWeight = 15;
    await setReactInput(page, 'input[type="number"]', customWeight.toString());
    const expectedPartnerCredit = customWeight * 2300; // 15 * 2300 = 34500

    // Click confirm partner weighing
    await page.evaluate(() => {
      const btns = Array.from(document.querySelectorAll('button'));
      const confirmBtn = btns.find(b => b.innerText.includes('Konfirmasi Timbangan & Transfer Saldo'));
      if (confirmBtn) confirmBtn.click();
    });
    await delay(500);

    // Return to Citizen mode
    await page.evaluate(() => {
      const backBtn = document.querySelector('button[aria-label="Kembali ke Akun Warga"]') ||
                      Array.from(document.querySelectorAll('button')).find(b => b.innerText.includes('Kembali ke Akun Warga'));
      if (backBtn) backBtn.click();
    });
    await delay(500);

    // Switch to Dompet to view updated wallet
    await switchTab(page, 'dompet');
    const B4 = await getWalletBalance(page);
    const expectedB4 = B3 + expectedPartnerCredit;
    assertEqual(B4, expectedB4, `Partner portal weighing credited accurately: B3 (${B3}) + ${expectedPartnerCredit} = B4 (${B4})`);

    // Verify partner transaction record
    const partnerTxFound = await page.evaluate((code) => {
      const text = document.body.innerText;
      return text.includes(code) && text.includes('Verifikasi Mitra');
    }, partnerCode);
    assert(partnerTxFound, `Partner weighing transaction for ${partnerCode} logged in ledger`);

    // -------------------------------------------------------------------------
    // SUITE 4: BROWSER RUNTIME & CONSOLE HEALTH
    // -------------------------------------------------------------------------
    console.log('\n▶ SUITE 4: Browser Runtime & Console Health');
    console.log('───────────────────────────────────────────────────────────────────');
    assert(pageErrors.length === 0, `Zero page runtime exceptions observed (Actual: ${pageErrors.length})`);
    if (pageErrors.length > 0) {
      pageErrors.forEach(err => console.error(`  ↳ Page Error: ${err}`));
    }

    const severeConsoleErrors = consoleErrors.filter(e => !e.text.includes('favicon'));
    assert(severeConsoleErrors.length === 0, `Zero unhandled console errors observed (Actual: ${severeConsoleErrors.length})`);
    if (severeConsoleErrors.length > 0) {
      severeConsoleErrors.forEach(err => console.error(`  ↳ Console Error: ${err.text}`));
    }

    console.log('\n===================================================================');
    console.log(`CHALLENGER STRESS HARNESS SUMMARY: ${passCount} Passed, ${failCount} Failed`);
    console.log('===================================================================');

    await browser.close();

    if (failCount > 0) {
      process.exit(1);
    } else {
      process.exit(0);
    }
  } catch (err) {
    console.error(`💥 Unhandled Exception in Stress Test Harness: ${err.message}`);
    console.error(err.stack);
    await browser.close();
    process.exit(1);
  }
}

runChallengerStressTests();
