import { launchBrowser, createPage, openApp, delay } from './helpers.js';

async function runStressTests() {
  console.log('===============================================================');
  console.log('       PILAH.IN — ADVERSARIAL STRESS TEST HARNESS (M1)         ');
  console.log('===============================================================');

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

  // Polling helper
  async function pollUntil(fn, timeoutMs = 4000, intervalMs = 30) {
    const start = Date.now();
    while (Date.now() - start < timeoutMs) {
      const res = await fn();
      if (res) return res;
      await delay(intervalMs);
    }
    return false;
  }

  try {
    console.log('\n▶ Test Suite 1: Initial Load & DOM Cleanliness Check');
    await openApp(page);

    // 1. Check absence of Leaderboard
    const leaderboardText = await page.evaluate(() => {
      const text = document.body.innerText.toLowerCase();
      return text.includes('peringkat kebersihan rw cilandak') ||
             text.includes('peringkat kebersihan') ||
             text.includes('papan peringkat');
    });
    assert(!leaderboardText, 'Peringkat Kebersihan RW Cilandak is completely absent from DOM');

    // 2. Check absence of header switcher pills
    const headerPillPresent = await page.evaluate(() => {
      const header = document.querySelector('header');
      if (!header) return false;
      const text = header.innerText.toLowerCase();
      return text.includes('mode warga') || text.includes('mode mitra rw');
    });
    assert(!headerPillPresent, 'Role switcher pills are completely absent from header');

    // 3. Check absence of frame toggle button in header
    const frameTogglePresent = await page.evaluate(() => {
      const header = document.querySelector('header');
      if (!header) return false;
      const text = header.innerText.toLowerCase();
      return text.includes('mode hp') || text.includes('full');
    });
    assert(!frameTogglePresent, 'Frame toggle buttons (Mode HP / Full) are completely absent from header');

    // 4. Check absence of Award icon SVG in DOM
    const awardSvgPresent = await page.evaluate(() => {
      const svgs = Array.from(document.querySelectorAll('svg'));
      return svgs.some(s => s.classList.contains('lucide-award'));
    });
    assert(!awardSvgPresent, 'Award icon (lucide-award) is completely absent from DOM');

    console.log('\n▶ Test Suite 2: Rapid Role Switching Stress Test (30 Consecutive Cycles)');
    const totalCycles = 30;
    let successfulCycles = 0;

    for (let i = 1; i <= totalCycles; i++) {
      // 1. Click Profile Avatar (Alternate between Header Avatar and Home Greeting Avatar)
      const clickedAvatar = await page.evaluate((cycle) => {
        const avatars = Array.from(document.querySelectorAll('button[aria-label="Profil Warga"]'));
        if (avatars.length === 0) return false;
        const target = (cycle % 2 === 0 && avatars.length > 1) ? avatars[1] : avatars[0];
        target.click();
        return true;
      }, i);
      if (!clickedAvatar) {
        throw new Error(`Cycle ${i}: Avatar button "Profil Warga" not found!`);
      }

      // Wait for Profile Modal
      const modalReady = await pollUntil(async () => {
        return await page.evaluate(() => {
          const btns = Array.from(document.querySelectorAll('button'));
          return btns.some(b => b.innerText && b.innerText.includes('Portal Mitra Pengelola'));
        });
      }, 3000);
      if (!modalReady) {
        throw new Error(`Cycle ${i}: Profile modal failed to render!`);
      }

      // 2. Click "Masuk ke Portal Mitra Pengelola"
      await page.evaluate(() => {
        const btns = Array.from(document.querySelectorAll('button'));
        const partnerBtn = btns.find(b => b.innerText && b.innerText.includes('Portal Mitra Pengelola'));
        if (partnerBtn) partnerBtn.click();
      });

      // Wait for Partner Portal to be active
      const inPartnerMode = await pollUntil(async () => {
        return await page.evaluate(() => {
          const text = document.body.innerText.toLowerCase();
          return text.includes('dasbor pengelola') && text.includes('portal mitra rw 05');
        });
      }, 3000);
      if (!inPartnerMode) {
        throw new Error(`Cycle ${i}: Failed to enter Partner Portal!`);
      }

      // 3. Alternate between Top Header Back Button and In-View Back Button
      await page.evaluate((cycle) => {
        if (cycle % 2 === 0) {
          const headerBack = document.querySelector('header button[aria-label="Kembali ke Akun Warga"]');
          if (headerBack) {
            headerBack.click();
            return;
          }
        }
        const inViewBack = document.querySelector('main button[aria-label="Kembali ke Akun Warga"]') ||
                          document.querySelector('button[aria-label="Kembali ke Akun Warga"]');
        if (inViewBack) inViewBack.click();
      }, i);

      // Wait for Citizen mode to be active
      const inCitizenMode = await pollUntil(async () => {
        return await page.evaluate(() => {
          const text = document.body.innerText.toLowerCase();
          return text.includes('raka pradipta') && text.includes('saldo daur ulang');
        });
      }, 3000);
      if (!inCitizenMode) {
        throw new Error(`Cycle ${i}: Failed to return to Citizen mode!`);
      }

      successfulCycles++;
      if (i % 10 === 0) {
        console.log(`    ... completed ${i}/${totalCycles} rapid cycles without error`);
      }
    }

    assert(successfulCycles === totalCycles, `All ${totalCycles} rapid role-switch cycles completed successfully without state corruption or navigation loops`);

    console.log('\n▶ Test Suite 3: Cross-Tab State Preservation Across Role Switches');
    const tabs = ['home', 'setor', 'toko', 'dompet'];
    let tabIntegrityPass = true;

    for (const tabId of tabs) {
      // Click bottom nav tab
      await page.evaluate((targetId) => {
        const mapping = {
          home: 'Beranda',
          setor: 'Setor',
          toko: 'Toko',
          dompet: 'Dompet'
        };
        const text = mapping[targetId];
        const btn = Array.from(document.querySelectorAll('nav button')).find(b => b.textContent.includes(text));
        if (btn) btn.click();
      }, tabId);

      await delay(100);

      // Verify bottom nav still visible in Citizen mode
      const navVisibleBefore = await page.evaluate(() => {
        const nav = document.querySelector('nav');
        return nav && nav.querySelectorAll('button').length === 4;
      });
      if (!navVisibleBefore) tabIntegrityPass = false;

      // Switch to partner
      await page.evaluate(() => {
        const avatar = document.querySelector('button[aria-label="Profil Warga"]');
        if (avatar) avatar.click();
      });

      await pollUntil(async () => {
        return await page.evaluate(() => {
          const btns = Array.from(document.querySelectorAll('button'));
          return btns.some(b => b.innerText && b.innerText.includes('Portal Mitra Pengelola'));
        });
      }, 2000);

      await page.evaluate(() => {
        const btns = Array.from(document.querySelectorAll('button'));
        const partnerBtn = btns.find(b => b.innerText && b.innerText.includes('Portal Mitra Pengelola'));
        if (partnerBtn) partnerBtn.click();
      });

      // Verify bottom nav is HIDDEN in Partner mode
      const navHiddenInPartner = await pollUntil(async () => {
        return await page.evaluate(() => {
          const text = document.body.innerText.toLowerCase();
          return text.includes('dasbor pengelola') && document.querySelectorAll('nav').length === 0;
        });
      }, 2000);
      if (!navHiddenInPartner) tabIntegrityPass = false;

      // Switch back to citizen
      await page.evaluate(() => {
        const backBtn = document.querySelector('button[aria-label="Kembali ke Akun Warga"]');
        if (backBtn) backBtn.click();
      });

      // Verify returned to citizen and bottom nav RESTORED
      const navRestored = await pollUntil(async () => {
        return await page.evaluate(() => {
          const nav = document.querySelector('nav');
          return nav && nav.querySelectorAll('button').length === 4;
        });
      }, 2000);
      if (!navRestored) tabIntegrityPass = false;
    }

    assert(tabIntegrityPass, 'Cross-tab switching and role toggling preserved navigation integrity and bottom nav lifecycle');

    console.log('\n▶ Test Suite 4: Modal Chaining and Overlay Cleanliness');
    // Open Profile -> Open Certificate -> Close Certificate -> Verify no deadlocks
    await page.evaluate(() => {
      const avatarBtn = document.querySelector('button[aria-label="Profil Warga"]');
      if (avatarBtn) avatarBtn.click();
    });

    await pollUntil(async () => {
      return await page.evaluate(() => {
        const btns = Array.from(document.querySelectorAll('button'));
        return btns.some(b => b.innerText && b.innerText.includes('Sertifikat Dampak Daur Ulang'));
      });
    }, 2000);

    const openedCert = await page.evaluate(() => {
      const btns = Array.from(document.querySelectorAll('button'));
      const certBtn = btns.find(b => b.innerText && b.innerText.includes('Sertifikat Dampak Daur Ulang'));
      if (certBtn) {
        certBtn.click();
        return true;
      }
      return false;
    });
    assert(openedCert, 'Certificate shortcut clicked inside Profile modal');

    const certVisible = await pollUntil(async () => {
      return await page.evaluate(() => document.body.innerText.includes('Sertifikat Resmi Pilah.in'));
    }, 2000);
    assert(certVisible, 'Certificate modal opened seamlessly from Profile shortcut');

    // Close certificate via modal button targeted within certificate modal container
    await page.evaluate(() => {
      const certModal = Array.from(document.querySelectorAll('.fixed')).find(m => m.innerText.includes('Sertifikat Resmi Pilah.in'));
      if (certModal) {
        const closeBtn = certModal.querySelector('button');
        if (closeBtn) closeBtn.click();
      }
    });

    const certClosed = await pollUntil(async () => {
      return await page.evaluate(() => !document.body.innerText.includes('Sertifikat Resmi Pilah.in'));
    }, 2000);
    assert(certClosed, 'Certificate modal closed cleanly without leaving backdrop lock');

    console.log('\n▶ Test Suite 5: Extreme Hammering / Double-Click Race Conditions');
    // Rapidly fire multiple clicks to stress state transitions
    for (let j = 0; j < 5; j++) {
      await page.evaluate(() => {
        const btn = document.querySelector('button[aria-label="Profil Warga"]');
        if (btn) {
          btn.click();
          btn.click();
        }
      });
      await delay(50);
      await page.evaluate(() => {
        const btns = Array.from(document.querySelectorAll('button'));
        const partnerBtn = btns.find(b => b.innerText && b.innerText.includes('Portal Mitra Pengelola'));
        if (partnerBtn) {
          partnerBtn.click();
          partnerBtn.click();
        }
      });
      await delay(50);
      await page.evaluate(() => {
        const backBtn = document.querySelector('button[aria-label="Kembali ke Akun Warga"]');
        if (backBtn) {
          backBtn.click();
          backBtn.click();
        }
      });
      await delay(50);
    }

    const robustAfterSpam = await pollUntil(async () => {
      return await page.evaluate(() => {
        const text = document.body.innerText.toLowerCase();
        return text.includes('pilah.in') && text.includes('raka pradipta');
      });
    }, 2000);
    assert(robustAfterSpam, 'Application survives rapid double-clicking and spam toggling without crash or deadlock');

    console.log('\n▶ Test Suite 6: Console & Runtime Error Evaluation');
    assert(pageErrors.length === 0, `Zero page runtime errors detected (Actual: ${pageErrors.length})`);
    if (pageErrors.length > 0) {
      console.error('Page errors detail:', pageErrors);
    }

    const criticalConsoleErrors = consoleErrors.filter(e => !e.text.includes('React DevTools'));
    assert(criticalConsoleErrors.length === 0, `Zero uncaught console errors detected (Actual: ${criticalConsoleErrors.length})`);
    if (criticalConsoleErrors.length > 0) {
      console.error('Console errors detail:', criticalConsoleErrors);
    }

  } catch (err) {
    console.error('💥 Test execution threw an unexpected error:', err);
    failCount++;
  } finally {
    await browser.close();
  }

  console.log('\n===============================================================');
  console.log(`TOTAL PASSED: ${passCount} | TOTAL FAILED: ${failCount}`);
  console.log('===============================================================');

  if (failCount > 0) {
    process.exit(1);
  } else {
    process.exit(0);
  }
}

runStressTests();
