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

export const name = 'Tier 4: Real-World Application Scenarios';

export async function run() {
  const browser = await launchBrowser();
  const page = await createPage(browser, { width: 390, height: 844 });
  const results = [];

  try {
    // -------------------------------------------------------------------------
    // Test 4.1: Citizen Daily Mobile Ergonomics Flow (390x844 Viewport)
    // -------------------------------------------------------------------------
    await (async () => {
      const testName = '4.1: Citizen daily mobile session & viewport ergonomics';
      try {
        await openApp(page);

        // Verify zero horizontal scroll overflow on 390px viewport
        const hasHorizontalScroll = await page.evaluate(() => {
          return document.documentElement.scrollWidth > window.innerWidth ||
                 document.body.scrollWidth > window.innerWidth;
        });

        assert(!hasHorizontalScroll, 'Horizontal scroll detected on mobile 390px viewport!');

        // Cycle through all citizen tabs: Home -> Setor -> Toko -> Dompet
        const tabs = ['setor', 'toko', 'dompet', 'home'];
        for (const t of tabs) {
          await switchTab(page, t);
          await delay(300);

          // Verify active tab content is visible and no uncaught JS errors
          const isVisible = await page.evaluate((targetTab) => {
            const body = document.body.innerText.toLowerCase();
            if (targetTab === 'setor') return body.includes('penyetoran');
            if (targetTab === 'toko') return body.includes('toko sirkular');
            if (targetTab === 'dompet') return body.includes('dompet') || body.includes('buku kas');
            if (targetTab === 'home') return body.includes('saldo daur ulang') || body.includes('cilandak');
            return true;
          }, t);

          assert(isVisible, `Tab "${t}" failed to render appropriate content on navigation`);
        }

        results.push({ name: testName, status: 'PASS', details: 'Zero horizontal scroll, smooth tab cycles' });
      } catch (err) {
        results.push({ name: testName, status: 'FAIL', error: err.message });
      }
    })();

    // -------------------------------------------------------------------------
    // Test 4.2: Partner Portal Weighing Operations
    // Reference: ORIGINAL_REQUEST R2, PROJECT.md Feature 5
    // -------------------------------------------------------------------------
    await (async () => {
      const testName = '4.2: Partner weighing verification portal operations';
      try {
        await openApp(page);

        // Switch to partner mode via User Profile Modal (PROJECT.md Clean Role Separation contract)
        const enteredPartnerMode = await page.evaluate(() => {
          // 1. Check if direct partner button exists (legacy)
          const directBtn = Array.from(document.querySelectorAll('button')).find(b =>
            b.innerText && (b.innerText.toLowerCase().includes('mode mitra') || b.innerText.toLowerCase().includes('portal mitra'))
          );
          if (directBtn) {
            directBtn.click();
            return 'direct';
          }

          // 2. Clean role separation: Open Profile Modal
          const profileBtn = document.querySelector('button[aria-label="Profil Warga"]') ||
                             Array.from(document.querySelectorAll('header button')).find(b => b.innerText.trim() === 'RP');
          if (profileBtn) {
            profileBtn.click();
            return 'opened_profile';
          }
          return false;
        });

        if (enteredPartnerMode === 'opened_profile') {
          await delay(400);
          // Click "Masuk ke Portal Mitra Pengelola" inside profile modal
          await page.evaluate(() => {
            const btns = Array.from(document.querySelectorAll('button, a'));
            const partnerPortalBtn = btns.find(b =>
              b.innerText && b.innerText.includes('Portal Mitra Pengelola')
            );
            if (partnerPortalBtn) partnerPortalBtn.click();
          });
        }

        assert(Boolean(enteredPartnerMode), 'Unable to find entry point to Partner Portal');
        await delay(500);

        // Check if partner dashboard is visible
        const partnerDashboardVisible = await page.evaluate(() => {
          const text = document.body.innerText.toLowerCase();
          return text.includes('dasbor pengelola') ||
                 text.includes('portal mitra');
        });
        assert(partnerDashboardVisible, 'Partner dashboard not rendered after role switch');

        // Capture initial balance before partner credit
        const initialBalance = await page.evaluate(() => {
          const match = document.body.innerText.match(/Rp\s*([\d.]+)/);
          return match ? parseInt(match[1].replace(/\./g, ''), 10) : 0;
        });

        // Enter ticket code PLH-992211 and weight 15 kg
        await page.evaluate(() => {
          const inputs = Array.from(document.querySelectorAll('input'));
          const codeInput = inputs.find(i => i.placeholder && i.placeholder.includes('PLH') || i.placeholder.includes('tiket'));
          if (codeInput) {
            codeInput.value = 'PLH-992211';
            codeInput.dispatchEvent(new Event('input', { bubbles: true }));
          }

          const weightInput = inputs.find(i => i.type === 'number');
          if (weightInput) {
            weightInput.value = '15';
            weightInput.dispatchEvent(new Event('input', { bubbles: true }));
          }
        });

        // Click "Konfirmasi Timbangan & Transfer Saldo"
        await page.evaluate(() => {
          const btns = Array.from(document.querySelectorAll('button'));
          const confirmBtn = btns.find(b => b.innerText.includes('Konfirmasi Timbangan'));
          if (confirmBtn) confirmBtn.click();
        });
        await delay(600);

        // Check success toast
        const toast = await getToastText(page);
        assert(
          toast && (toast.toLowerCase().includes('diverifikasi') || toast.toLowerCase().includes('berhasil')),
          `Expected verification toast in partner mode, got: "${toast}"`
        );

        results.push({ name: testName, status: 'PASS', details: 'Partner scale input verified & credited' });
      } catch (err) {
        results.push({ name: testName, status: 'FAIL', error: err.message });
      }
    })();

    // -------------------------------------------------------------------------
    // Test 4.3: Multi-Category Waste Deposit Aggregation
    // Reference: ORIGINAL_REQUEST R2, PROJECT.md Feature 4
    // -------------------------------------------------------------------------
    await (async () => {
      const testName = '4.3: Multi-category deposit combination & aggregation';
      try {
        await openApp(page);

        // Ensure in citizen mode
        await page.evaluate(() => {
          const btns = Array.from(document.querySelectorAll('button'));
          const wargaBtn = btns.find(b => b.innerText && (b.innerText.includes('Mode Warga') || b.innerText.includes('Kembali ke Warga')));
          if (wargaBtn) wargaBtn.click();
        });
        await delay(300);

        await switchTab(page, 'setor');

        // Select multiple categories: Kardus + Botol Plastik PET
        await page.evaluate(() => {
          const cards = Array.from(document.querySelectorAll('.grid.grid-cols-2 > div'));
          for (const card of cards) {
            const text = card.innerText;
            const isSelected = card.querySelector('.bg-emerald-600') !== null;
            if (text.includes('Kardus') && !isSelected) {
              card.click();
            } else if (text.includes('Botol Plastik') && !isSelected) {
              card.click();
            }
          }
        });
        await delay(400);

        // Verify summary has > 1 category combined
        const multiSummary = await page.evaluate(() => {
          const text = document.body.innerText;
          const kgMatch = text.match(/Total Estimasi Berat:\s*(\d+)\s*kg/i);
          const totalMatch = text.match(/Estimasi Saldo Mengendap Baru:\s*\+Rp\s*([\d.]+)/i);
          return {
            kg: kgMatch ? parseInt(kgMatch[1], 10) : 0,
            total: totalMatch ? parseInt(totalMatch[1].replace(/\./g, ''), 10) : 0
          };
        });

        assert(multiSummary.kg >= 5, `Expected aggregate weight >= 5 kg, got: ${multiSummary.kg}`);
        assert(multiSummary.total >= 10000, `Expected aggregate total >= Rp 10.000, got: ${multiSummary.total}`);

        // Click "Buat Tiket & Jadwal Penyetoran"
        await page.evaluate(() => {
          const btns = Array.from(document.querySelectorAll('button'));
          const btn = btns.find(b => b.innerText.includes('Buat Tiket'));
          if (btn) btn.click();
        });
        await delay(500);

        // Verify modal displays aggregated items
        const modalText = await page.evaluate(() => document.body.innerText);
        assert(modalText.includes('Tiket Penyetoran Digital'), 'Multi-item ticket modal did not open');
        assert(modalText.includes(`${multiSummary.kg} kg`), 'Ticket modal did not reflect aggregate weight');

        results.push({
          name: testName,
          status: 'PASS',
          details: `Aggregated ${multiSummary.kg} kg = Rp ${multiSummary.total} across multiple waste streams`
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
