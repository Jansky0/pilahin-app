import {
  launchBrowser,
  createPage,
  openApp,
  switchTab,
  getWalletBalance,
  getToastText,
  delay
} from './helpers.js';

/**
 * CHALLENGER M4_1 Gen2: Full End-to-End User Journey Empirical Challenge
 * 
 * Strict Journey Sequence:
 * Beranda -> Setor -> Timbang Mitra -> Toko -> Tarik e-Wallet -> Profile -> Mode Mitra -> Kembali
 * 
 * Target: http://localhost:3000
 */

let totalChecks = 0;
let passedChecks = 0;
let failedChecks = 0;
const failureLog = [];

function check(condition, desc) {
  totalChecks++;
  if (condition) {
    console.log(`  ✅ [PASS] ${desc}`);
    passedChecks++;
  } else {
    console.error(`  ❌ [FAIL] ${desc}`);
    failedChecks++;
    failureLog.push(desc);
  }
}

async function dismissToast(page) {
  await page.evaluate(() => {
    const closeBtn = document.querySelector('[role="alert"] button');
    if (closeBtn) closeBtn.click();
  });
  await delay(150);
}

async function runFullUserJourneyChallenge() {
  console.log('======================================================================');
  console.log('   CHALLENGER M4_1 GEN2: EMPIRICAL FULL USER JOURNEY VERIFICATION     ');
  console.log('======================================================================\n');
  console.log('Journey Sequence:');
  console.log('Beranda -> Setor -> Timbang Mitra -> Toko -> Tarik e-Wallet -> Profile -> Mode Mitra -> Kembali\n');

  const browser = await launchBrowser();
  const page = await createPage(browser, { width: 390, height: 844 });

  const consoleErrors = [];
  page.on('console', msg => {
    if (msg.type() === 'error') {
      consoleErrors.push(msg.text());
    }
  });
  page.on('pageerror', err => {
    consoleErrors.push(err.message);
  });

  try {
    // -----------------------------------------------------------------------
    // STAGE 1: BERANDA (Citizen Home Screen & Clean UI Verification)
    // -----------------------------------------------------------------------
    console.log('▶ STAGE 1: BERANDA');
    await openApp(page);

    // 1.1 Leaderboard check
    const hasLeaderboard = await page.evaluate(() => {
      const text = document.body.innerText.toLowerCase();
      return text.includes('papan peringkat') || text.includes('leaderboard') || text.includes('peringkat kebersihan');
    });
    check(!hasLeaderboard, 'Beranda: Leaderboard / Papan Peringkat RW completely absent from DOM');

    // 1.2 Clean header without role switcher pills
    const headerPills = await page.evaluate(() => {
      const header = document.querySelector('header');
      if (!header) return [];
      return Array.from(header.querySelectorAll('button, a'))
        .map(b => b.innerText.trim())
        .filter(t => t.toLowerCase().includes('mode warga') || t.toLowerCase().includes('mode mitra'));
    });
    check(headerPills.length === 0, 'Beranda: Header contains 0 role-switcher pill buttons');

    // 1.3 Hero Wallet Card
    const initialBalance = await getWalletBalance(page);
    check(initialBalance === 148500, `Beranda: Initial Hero Wallet Balance is Rp 148.500 (Got: ${initialBalance})`);

    // 1.4 Quick Action Hub (4 interactive buttons)
    const quickActionButtons = await page.evaluate(() => {
      const buttons = Array.from(document.querySelectorAll('button'));
      return buttons.map(b => b.innerText.replace(/\s+/g, ' ').trim());
    });
    const hasSetorHub = quickActionButtons.some(t => t.includes('Setor'));
    const hasTarikHub = quickActionButtons.some(t => t.includes('Tarik'));
    const hasTokoHub = quickActionButtons.some(t => t.includes('Toko'));
    const hasRiwayatHub = quickActionButtons.some(t => t.includes('Riwayat'));
    check(
      hasSetorHub && hasTarikHub && hasTokoHub && hasRiwayatHub,
      'Beranda: Quick Action Hub rendered with 4 core actions (Setor, Tarik, Toko, Riwayat)'
    );

    // 1.5 Personal Eco-Impact Bento Card
    const hasEcoImpact = await page.evaluate(() => {
      const text = document.body.innerText;
      return text.toUpperCase().includes('DAMPAK SIRKULAR KAMU') && text.includes('Terselamatkan') && text.includes('Pahlawan Hijau');
    });
    check(hasEcoImpact, 'Beranda: Personal Eco-Impact Bento Card present and active ("DAMPAK SIRKULAR KAMU")');

    // -----------------------------------------------------------------------
    // STAGE 2: SETOR (Waste Deposit Flow & Live Estimator)
    // -----------------------------------------------------------------------
    console.log('\n▶ STAGE 2: SETOR');
    await switchTab(page, 'setor');
    await delay(300);

    // Verify Setor UI
    const setorTitle = await page.evaluate(() => {
      const h2 = document.querySelector('h2');
      return h2 ? h2.innerText : '';
    });
    check(setorTitle.toLowerCase().includes('setor') || setorTitle.toLowerCase().includes('pilih'), `Setor: Setor screen active ("${setorTitle}")`);

    // Check live weight & balance estimation
    const depositEst = await page.evaluate(() => {
      const text = document.body.innerText;
      const mKg = text.match(/Total Estimasi Berat:\s*(\d+)\s*kg/i);
      const mRp = text.match(/Estimasi Saldo Mengendap Baru:\s*\+Rp\s*([\d.]+)/i);
      return {
        kg: mKg ? parseInt(mKg[1], 10) : 0,
        rp: mRp ? parseInt(mRp[1].replace(/\./g, ''), 10) : 0
      };
    });
    check(depositEst.kg === 11, `Setor: Default selected categories calculate to 11 kg (Got: ${depositEst.kg} kg)`);
    check(depositEst.rp === 24900, `Setor: Estimated escrow deposit is +Rp 24.900 (Got: +Rp ${depositEst.rp})`);

    // Create deposit ticket
    const clickedSubmitTicket = await page.evaluate(() => {
      const btns = Array.from(document.querySelectorAll('button'));
      const btn = btns.find(b => b.innerText.includes('Buat Tiket'));
      if (btn) { btn.click(); return true; }
      return false;
    });
    check(clickedSubmitTicket, 'Setor: Clicked "Buat Tiket" button');
    await delay(500);

    // Digital ticket modal inspection
    const ticketInfo = await page.evaluate(() => {
      const match = document.body.innerText.match(/PLH-\d{6}/);
      const modal = Array.from(document.querySelectorAll('h3')).find(h => h.innerText.includes('Tiket Penyetoran Digital'));
      return {
        code: match ? match[0] : null,
        modalVisible: !!modal
      };
    });
    check(ticketInfo.modalVisible, 'Setor: Digital Ticket Modal opened');
    check(ticketInfo.code !== null, `Setor: Generated unique ticket code: ${ticketInfo.code}`);

    // -----------------------------------------------------------------------
    // STAGE 3: TIMBANG MITRA (Partner Weighing Simulation & Auto Credit)
    // -----------------------------------------------------------------------
    console.log('\n▶ STAGE 3: TIMBANG MITRA');
    const balanceBeforeWeighing = initialBalance; // 148500

    const clickedSimulateWeighing = await page.evaluate(() => {
      const btns = Array.from(document.querySelectorAll('button'));
      const btn = btns.find(b => b.innerText.includes('Simulasikan Timbangan Selesai'));
      if (btn) { btn.click(); return true; }
      return false;
    });
    check(clickedSimulateWeighing, 'Timbang Mitra: Triggered "Simulasikan Timbangan Selesai & Tambah Saldo"');
    await delay(200);

    // Toast check
    const toastAfterWeighing = await getToastText(page);
    check(
      toastAfterWeighing && toastAfterWeighing.includes(ticketInfo.code) && toastAfterWeighing.includes('Saldo Mengendap'),
      `Timbang Mitra: Toast notification confirmed credit for ticket ${ticketInfo.code}`
    );
    await dismissToast(page);

    // Check balance update in Dompet (app redirects to Dompet after weighing)
    const balanceAfterWeighing = await getWalletBalance(page);
    const expectedB1 = balanceBeforeWeighing + depositEst.rp; // 148500 + 24900 = 173400
    check(
      balanceAfterWeighing === expectedB1,
      `Timbang Mitra: Wallet balance accurately updated to Rp ${expectedB1} (B0: ${balanceBeforeWeighing} + ${depositEst.rp} -> Got: ${balanceAfterWeighing})`
    );

    // Ledger audit for deposit
    const hasDepositInLedger = await page.evaluate((code) => {
      const text = document.body.innerText;
      return text.includes('Setor 11 kg') || (code && text.includes(code)) || text.includes('Timbangan Terverifikasi');
    }, ticketInfo.code);
    check(hasDepositInLedger, 'Timbang Mitra: Credit entry recorded in Dompet transaction ledger');

    // -----------------------------------------------------------------------
    // STAGE 4: TOKO (Circular Store Purchase with Escrow Balance)
    // -----------------------------------------------------------------------
    console.log('\n▶ STAGE 4: TOKO');
    await switchTab(page, 'toko');
    await delay(400);

    // Inspect first product (Pupuk Kompos @ Rp 18.000 saldo sampah)
    const productInfo = await page.evaluate(() => {
      const firstCard = document.querySelector('.bg-white.rounded-2xl.p-3\\.5');
      if (!firstCard) return null;
      const titleEl = firstCard.querySelector('h4');
      const title = titleEl ? titleEl.innerText : 'Pupuk Kompos';
      const priceMatch = firstCard.innerText.match(/Rp\s*([\d.]+)/);
      const price = priceMatch ? parseInt(priceMatch[1].replace(/\./g, ''), 10) : 18000;
      
      const tukarBtn = firstCard.querySelector('button');
      if (tukarBtn) tukarBtn.click();
      return { title, price };
    });
    check(productInfo !== null, `Toko: Selected product "${productInfo?.title}" (Price: Rp ${productInfo?.price})`);
    await delay(500);

    // Modal confirmation
    const clickedConfirmBuy = await page.evaluate(() => {
      const btns = Array.from(document.querySelectorAll('button'));
      const btn = btns.find(b => b.innerText.includes('Konfirmasi Tukar'));
      if (btn) { btn.click(); return true; }
      return false;
    });
    check(clickedConfirmBuy, 'Toko: Clicked "Konfirmasi Tukar" in modal');
    await delay(200);

    // Toast check
    const toastAfterBuy = await getToastText(page);
    check(
      toastAfterBuy && toastAfterBuy.toLowerCase().includes('sukses menukar'),
      `Toko: Toast confirmed store purchase: "${toastAfterBuy}"`
    );
    await dismissToast(page);

    // Switch to Dompet and verify balance deduction
    await switchTab(page, 'dompet');
    await delay(300);
    const balanceAfterBuy = await getWalletBalance(page);
    const expectedB2 = balanceAfterWeighing - (productInfo?.price || 18000); // 173400 - 18000 = 155400
    check(
      balanceAfterBuy === expectedB2,
      `Toko: Balance deducted by store price (Expected: Rp ${expectedB2}, Got: Rp ${balanceAfterBuy})`
    );

    // Ledger audit for store purchase
    const hasStoreInLedger = await page.evaluate(() => {
      const text = document.body.innerText;
      return text.includes('Pupuk Kompos') || text.includes('Potong Saldo Sampah') || text.includes('Toko Sirkular');
    });
    check(hasStoreInLedger, 'Toko: Debit entry recorded in Dompet transaction ledger');

    // -----------------------------------------------------------------------
    // STAGE 5: TARIK E-WALLET (Instant Cashout to GoPay/DANA)
    // -----------------------------------------------------------------------
    console.log('\n▶ STAGE 5: TARIK E-WALLET');
    // Select Rp 50.000 preset chip
    const selected50k = await page.evaluate(() => {
      const btns = Array.from(document.querySelectorAll('button'));
      const chip = btns.find(b => b.innerText.includes('50.000'));
      if (chip) { chip.click(); return true; }
      return false;
    });
    check(selected50k, 'Tarik e-Wallet: Selected Rp 50.000 cashout chip');
    await delay(200);

    // Click "Cairkan Sekarang"
    const clickedCashout = await page.evaluate(() => {
      const btns = Array.from(document.querySelectorAll('button'));
      const btn = btns.find(b => b.innerText.includes('Cairkan Sekarang'));
      if (btn) { btn.click(); return true; }
      return false;
    });
    check(clickedCashout, 'Tarik e-Wallet: Clicked "Cairkan Sekarang"');
    await delay(200);

    // Toast check
    const toastAfterCashout = await getToastText(page);
    check(
      toastAfterCashout && toastAfterCashout.toLowerCase().includes('berhasil'),
      `Tarik e-Wallet: Toast confirmed cashout: "${toastAfterCashout}"`
    );
    await dismissToast(page);

    // Balance verification
    const balanceAfterCashout = await getWalletBalance(page);
    const expectedB3 = balanceAfterBuy - 50000; // 155400 - 50000 = 105400
    check(
      balanceAfterCashout === expectedB3,
      `Tarik e-Wallet: Balance deducted by cashout amount (Expected: Rp ${expectedB3}, Got: Rp ${balanceAfterCashout})`
    );

    // Ledger audit for cashout
    const hasCashoutInLedger = await page.evaluate(() => {
      const text = document.body.innerText;
      return text.includes('Pencairan Saldo') || text.includes('Transfer E-Wallet') || text.includes('-Rp 50.000');
    });
    check(hasCashoutInLedger, 'Tarik e-Wallet: Debit entry recorded in Dompet transaction ledger');

    // -----------------------------------------------------------------------
    // STAGE 6: PROFILE (User Profile Modal & Eco Stats)
    // -----------------------------------------------------------------------
    console.log('\n▶ STAGE 6: PROFILE');
    // Open Profile via avatar button
    const openedProfile = await page.evaluate(() => {
      const avatarBtn = document.querySelector('button[aria-label="Profil Warga"]') ||
        Array.from(document.querySelectorAll('header button')).find(b => b.innerText.trim() === 'RP');
      if (avatarBtn) { avatarBtn.click(); return true; }
      return false;
    });
    check(openedProfile, 'Profile: Opened User Profile Modal via header avatar (RP)');
    await delay(500);

    // Verify Profile content
    const profileData = await page.evaluate(() => {
      const text = document.body.innerText;
      const hasName = text.includes('Raka Pradipta');
      const hasRW = text.includes('RW 05');
      const hasPartnerBtn = text.includes('Masuk ke Portal Mitra Pengelola');
      return { hasName, hasRW, hasPartnerBtn };
    });
    check(profileData.hasName && profileData.hasRW, 'Profile: Displayed user identity (Raka Pradipta - Kelurahan Cilandak Barat RW 05)');
    check(profileData.hasPartnerBtn, 'Profile: Partner access portal button present ("Masuk ke Portal Mitra Pengelola")');

    // -----------------------------------------------------------------------
    // STAGE 7: MODE MITRA (Partner Portal Dashboard & Operations)
    // -----------------------------------------------------------------------
    console.log('\n▶ STAGE 7: MODE MITRA');
    const enteredPartnerMode = await page.evaluate(() => {
      const btns = Array.from(document.querySelectorAll('button'));
      const btn = btns.find(b => b.innerText.includes('Masuk ke Portal Mitra Pengelola'));
      if (btn) { btn.click(); return true; }
      return false;
    });
    check(enteredPartnerMode, 'Mode Mitra: Transitioned to Partner Portal');
    await delay(600);

    // Verify Partner Portal UI elements (case-insensitive for CSS uppercase)
    const partnerUI = await page.evaluate(() => {
      const text = document.body.innerText.toUpperCase();
      const hasPartnerTitle = text.includes('DASBOR PENGELOLA DAUR ULANG');
      const hasWeighSection = text.includes('VERIFIKASI TIKET & INPUT TIMBANGAN WARGA');
      const hasPriceSection = text.includes('ATUR HARGA BELI SAMPAH HARI INI');
      const hasBackBtn = Array.from(document.querySelectorAll('button')).some(b => b.innerText.includes('Kembali ke Akun Warga'));
      return { hasPartnerTitle, hasWeighSection, hasPriceSection, hasBackBtn };
    });
    check(partnerUI.hasPartnerTitle, 'Mode Mitra: Partner Dashboard active ("Dasbor Pengelola Daur Ulang")');
    check(partnerUI.hasWeighSection, 'Mode Mitra: Ticket verification and scale input interface present');
    check(partnerUI.hasBackBtn, 'Mode Mitra: "← Kembali ke Akun Warga" button rendered clearly');

    // Perform Mitra Operational Scale Verification
    console.log('  [Mitra Action: Direct scale verification in portal]');
    const clickedConfirmMitraWeigh = await page.evaluate(() => {
      const inputs = Array.from(document.querySelectorAll('input'));
      const codeInput = inputs.find(i => i.placeholder && i.placeholder.includes('kode tiket'));
      const weightInput = inputs.find(i => i.type === 'number');

      const nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
      if (codeInput) {
        nativeSetter.call(codeInput, 'PLH-778899');
        codeInput.dispatchEvent(new Event('input', { bubbles: true }));
      }
      if (weightInput) {
        nativeSetter.call(weightInput, '5');
        weightInput.dispatchEvent(new Event('input', { bubbles: true }));
      }

      const confirmBtn = Array.from(document.querySelectorAll('button')).find(b =>
        b.innerText.includes('Konfirmasi Timbangan')
      );
      if (confirmBtn) {
        confirmBtn.click();
        return true;
      }
      return false;
    });
    check(clickedConfirmMitraWeigh, 'Mode Mitra: Clicked "Konfirmasi Timbangan & Transfer Saldo" for ticket PLH-778899 (5 kg)');
    await delay(300);

    const toastMitraWeighing = await getToastText(page);
    check(
      toastMitraWeighing && toastMitraWeighing.includes('PLH-778899') && toastMitraWeighing.includes('berhasil dikreditkan'),
      `Mode Mitra: Toast confirmed credit: "${toastMitraWeighing}"`
    );
    await dismissToast(page);

    // -----------------------------------------------------------------------
    // STAGE 8: KEMBALI (Return to Citizen Mode & State Integrity Audit)
    // -----------------------------------------------------------------------
    console.log('\n▶ STAGE 8: KEMBALI');
    const clickedKembali = await page.evaluate(() => {
      const btns = Array.from(document.querySelectorAll('button'));
      const btn = btns.find(b => b.innerText.includes('Kembali ke Akun Warga'));
      if (btn) { btn.click(); return true; }
      return false;
    });
    check(clickedKembali, 'Kembali: Clicked "← Kembali ke Akun Warga"');
    await delay(600);

    // Verify back to Citizen view
    const citizenRestored = await page.evaluate(() => {
      const header = document.querySelector('header');
      const isCitizenHeader = header && header.innerText.includes('Pilah.in');
      const hasBottomNav = document.querySelectorAll('nav button').length >= 4;
      return isCitizenHeader && hasBottomNav;
    });
    check(citizenRestored, 'Kembali: Citizen UI and 4-tab bottom navigation restored');

    // Verify Final Balance Consistency
    // Math audit:
    // B0: 148.500
    // + Deposit (11 kg): 24.900 -> 173.400
    // - Store Buy (Pupuk Kompos): 18.000 -> 155.400
    // - E-Wallet Cashout: 50.000 -> 105.400
    // + Mitra Scale Verification (5 kg @ 2.300): 11.500 -> 116.900
    await switchTab(page, 'dompet');
    await delay(300);
    const finalBalance = await getWalletBalance(page);
    const expectedFinal = 105400 + (5 * 2300); // 116900
    check(
      finalBalance === expectedFinal,
      `Kembali: Final balance mathematically consistent across all 8 stages (Expected: Rp ${expectedFinal}, Got: Rp ${finalBalance})`
    );

    // Verify 0 runtime console errors
    check(consoleErrors.length === 0, `Runtime Stability: 0 console errors during full journey (Errors: [${consoleErrors.join(', ')}])`);

  } catch (err) {
    console.error(`💥 Journey execution error: ${err.message}`);
    check(false, `Unexpected fatal exception: ${err.message}`);
  } finally {
    await browser.close();
  }

  console.log('\n======================================================================');
  console.log(`JOURNEY RESULTS: ${passedChecks} / ${totalChecks} Checks Passed (${((passedChecks / totalChecks) * 100).toFixed(1)}%)`);
  if (failedChecks > 0) {
    console.log(`Failures recorded (${failedChecks}):`);
    failureLog.forEach(f => console.log(`  - ${f}`));
    process.exit(1);
  } else {
    console.log('🎉 COMPLETE USER JOURNEY VERIFIED FLAWLESSLY! EXIT CODE 0.');
    process.exit(0);
  }
}

runFullUserJourneyChallenge();
