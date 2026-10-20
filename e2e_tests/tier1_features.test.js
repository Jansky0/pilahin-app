import {
  launchBrowser,
  createPage,
  openApp,
  switchTab,
  getWalletBalance,
  parseRupiah,
  getToastText,
  assert,
  assertEqual,
  delay
} from './helpers.js';

export const name = 'Tier 1: Feature Coverage';

export async function run() {
  const browser = await launchBrowser();
  const page = await createPage(browser);
  const results = [];

  try {
    // -------------------------------------------------------------------------
    // Test 1.1: Leaderboard Absence on Citizen Home Screen
    // Reference: ORIGINAL_REQUEST R2, PROJECT.md Feature 1
    // -------------------------------------------------------------------------
    await (async () => {
      const testName = '1.1: Leaderboard absent on citizen home screen';
      try {
        await openApp(page);
        await switchTab(page, 'home');

        const pageText = await page.evaluate(() => document.body.innerText.toLowerCase());
        const hasLeaderboardTitle = pageText.includes('peringkat kebersihan');
        const hasLeaderboardEntry = pageText.includes('342 kg terpilah') || pageText.includes('rw 05 (lingkunganmu)');

        assert(
          !hasLeaderboardTitle && !hasLeaderboardEntry,
          `Citizen home screen still contains community leaderboard elements! (Title: ${hasLeaderboardTitle}, Entries: ${hasLeaderboardEntry})`
        );

        results.push({ name: testName, status: 'PASS' });
      } catch (err) {
        results.push({ name: testName, status: 'FAIL', error: err.message });
      }
    })();

    // -------------------------------------------------------------------------
    // Test 1.2: Clean Role Navigation & Header Switcher Elimination
    // Reference: ORIGINAL_REQUEST R2, PROJECT.md Feature 2 & 3
    // -------------------------------------------------------------------------
    await (async () => {
      const testName = '1.2: Clean role navigation without header switcher pills';
      try {
        await openApp(page);

        // Header must not contain role switch pills 'Mode Warga' / 'Mode Mitra RW'
        const headerButtons = await page.evaluate(() => {
          const header = document.querySelector('header');
          if (!header) return [];
          return Array.from(header.querySelectorAll('button, a')).map(b => b.innerText.trim());
        });

        const hasRolePillInHeader = headerButtons.some(t =>
          t.toLowerCase().includes('mode warga') || t.toLowerCase().includes('mode mitra')
        );

        assert(
          !hasRolePillInHeader,
          `Header still contains role-switcher pill buttons: [${headerButtons.join(', ')}]`
        );

        results.push({ name: testName, status: 'PASS' });
      } catch (err) {
        results.push({ name: testName, status: 'FAIL', error: err.message });
      }
    })();

    // -------------------------------------------------------------------------
    // Test 1.3: Deposit Calculation
    // Reference: ORIGINAL_REQUEST R2, PROJECT.md Feature 4
    // -------------------------------------------------------------------------
    await (async () => {
      const testName = '1.3: Waste deposit live calculation & estimation';
      try {
        await openApp(page);
        await switchTab(page, 'setor');

        const summaryData = await page.evaluate(() => {
          const text = document.body.innerText;
          const hasKg = text.match(/Total Estimasi Berat:\s*(\d+)\s*kg/i);
          const hasTotal = text.match(/Estimasi Saldo Mengendap Baru:\s*\+Rp\s*([\d.]+)/i);
          return {
            hasKg: hasKg ? parseInt(hasKg[1], 10) : null,
            hasTotal: hasTotal ? parseInt(hasTotal[1].replace(/\./g, ''), 10) : null
          };
        });

        assert(summaryData.hasKg !== null && summaryData.hasKg > 0, 'Deposit total estimated weight not calculated');
        assert(summaryData.hasTotal !== null && summaryData.hasTotal > 0, 'Deposit estimated Rupiah total not calculated');

        results.push({
          name: testName,
          status: 'PASS',
          details: `Estimated ${summaryData.hasKg} kg = Rp ${summaryData.hasTotal}`
        });
      } catch (err) {
        results.push({ name: testName, status: 'FAIL', error: err.message });
      }
    })();

    // -------------------------------------------------------------------------
    // Test 1.4: Deposit Weighing & Balance Update
    // Reference: ORIGINAL_REQUEST R2, PROJECT.md Feature 5 & 6
    // -------------------------------------------------------------------------
    await (async () => {
      const testName = '1.4: Balance update after ticket creation & weighing verification';
      try {
        await openApp(page);
        await switchTab(page, 'dompet');
        const initialBalance = await getWalletBalance(page);

        // Go to Setor tab and create ticket
        await switchTab(page, 'setor');

        // Click Buat Tiket
        const buatTiketClicked = await page.evaluate(() => {
          const btns = Array.from(document.querySelectorAll('button'));
          const btn = btns.find(b => b.innerText.includes('Buat Tiket'));
          if (btn) { btn.click(); return true; }
          return false;
        });
        assert(buatTiketClicked, 'Button "Buat Tiket" not found in Setor tab');
        await delay(500);

        // Verify ticket modal opens with PLH- code
        const ticketCode = await page.evaluate(() => {
          const match = document.body.innerText.match(/PLH-\d{6}/);
          return match ? match[0] : null;
        });
        assert(ticketCode !== null, 'Digital ticket with PLH-XXXXXX code not generated in modal');

        // Click Simulate Partner Weighing
        const simClicked = await page.evaluate(() => {
          const btns = Array.from(document.querySelectorAll('button'));
          const btn = btns.find(b => b.innerText.includes('Simulasikan Timbangan Selesai'));
          if (btn) { btn.click(); return true; }
          return false;
        });
        assert(simClicked, 'Simulation button not found in ticket modal');
        await delay(600);

        // Check new balance in Dompet
        const newBalance = await getWalletBalance(page);
        assert(
          newBalance > initialBalance,
          `Wallet balance did not increase after weighing (Before: ${initialBalance}, After: ${newBalance})`
        );

        results.push({
          name: testName,
          status: 'PASS',
          details: `Ticket ${ticketCode} credited +Rp ${newBalance - initialBalance}`
        });
      } catch (err) {
        results.push({ name: testName, status: 'FAIL', error: err.message });
      }
    })();

    // -------------------------------------------------------------------------
    // Test 1.5: Toko Sirkular Purchase Deduction
    // Reference: ORIGINAL_REQUEST R2, PROJECT.md Feature 8
    // -------------------------------------------------------------------------
    await (async () => {
      const testName = '1.5: Toko Sirkular purchase reduces wallet balance';
      try {
        await openApp(page);
        await switchTab(page, 'toko');

        const initialBalance = await getWalletBalance(page);

        // Click first 'Tukar' button
        const tukarClicked = await page.evaluate(() => {
          const btns = Array.from(document.querySelectorAll('button'));
          const btn = btns.find(b => b.innerText.trim() === 'Tukar');
          if (btn) { btn.click(); return true; }
          return false;
        });
        assert(tukarClicked, 'Button "Tukar" not found in Toko tab');
        await delay(500);

        // Confirm exchange in modal
        const confirmClicked = await page.evaluate(() => {
          const btns = Array.from(document.querySelectorAll('button'));
          const btn = btns.find(b => b.innerText.includes('Konfirmasi Tukar'));
          if (btn) { btn.click(); return true; }
          return false;
        });
        assert(confirmClicked, 'Button "Konfirmasi Tukar" not found in checkout modal');
        await delay(600);

        // Check toast notification
        const toast = await getToastText(page);
        assert(toast && toast.toLowerCase().includes('sukses'), `Expected success toast on purchase, got: "${toast}"`);

        // Check wallet balance in Dompet
        await switchTab(page, 'dompet');
        const afterBalance = await getWalletBalance(page);
        assert(
          afterBalance < initialBalance,
          `Wallet balance was not deducted after store purchase (Before: ${initialBalance}, After: ${afterBalance})`
        );

        results.push({
          name: testName,
          status: 'PASS',
          details: `Balance deducted by Rp ${initialBalance - afterBalance}`
        });
      } catch (err) {
        results.push({ name: testName, status: 'FAIL', error: err.message });
      }
    })();

    // -------------------------------------------------------------------------
    // Test 1.6: E-Wallet Cashout Validation
    // Reference: ORIGINAL_REQUEST R2, PROJECT.md Feature 7
    // -------------------------------------------------------------------------
    await (async () => {
      const testName = '1.6: E-wallet cashout validation & balance deduction';
      try {
        await openApp(page);
        await switchTab(page, 'dompet');
        const initialBalance = await getWalletBalance(page);

        // Select 50000 chip
        const chipSelected = await page.evaluate(() => {
          const btns = Array.from(document.querySelectorAll('button'));
          const chip = btns.find(b => b.innerText.includes('50.000'));
          if (chip) { chip.click(); return true; }
          return false;
        });
        assert(chipSelected, 'Nominal chip "50.000" not found in cashout form');
        await delay(300);

        // Submit cashout
        const submitClicked = await page.evaluate(() => {
          const btns = Array.from(document.querySelectorAll('button'));
          const btn = btns.find(b => b.innerText.includes('Cairkan Sekarang'));
          if (btn) { btn.click(); return true; }
          return false;
        });
        assert(submitClicked, 'Button "Cairkan Sekarang" not found');
        await delay(600);

        // Check toast
        const toast = await getToastText(page);
        assert(toast && toast.toLowerCase().includes('berhasil'), `Expected success toast on cashout, got: "${toast}"`);

        // Check updated balance
        const afterBalance = await getWalletBalance(page);
        assertEqual(
          afterBalance,
          initialBalance - 50000,
          `Wallet balance mismatch after 50k cashout (Initial: ${initialBalance}, After: ${afterBalance})`
        );

        results.push({
          name: testName,
          status: 'PASS',
          details: `Withdrew Rp 50.000 cleanly (Balance: ${initialBalance} -> ${afterBalance})`
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
