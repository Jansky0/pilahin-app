import { launchBrowser, createPage, openApp, switchTab, getWalletBalance, getToastText, parseRupiah, delay } from './helpers.js';

async function runChallengerStressTestsM3() {
  console.log('===================================================================');
  console.log('     PILAH.IN — EMPIRICAL CHALLENGER STRESS HARNESS (M3_2)        ');
  console.log('   Touch Targets, Stepper Isolation & 360x640px Modal Ergonomics   ');
  console.log('===================================================================');

  // Launch headless browser at short mobile viewport 360x640px
  const browser = await launchBrowser();
  const page = await createPage(browser, { width: 360, height: 640 });

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

  try {
    await openApp(page);

    // =========================================================================
    // TEST SUITE 1: 360px Viewport No Horizontal Overflow & Bottom Nav Targets
    // =========================================================================
    console.log('\n--- Test Suite 1: Viewport Geometry & Bottom Navigation ---');
    const viewportCheck = await page.evaluate(() => {
      return {
        bodyScrollWidth: document.body.scrollWidth,
        docScrollWidth: document.documentElement.scrollWidth,
        windowInnerWidth: window.innerWidth,
        windowInnerHeight: window.innerHeight,
      };
    });
    assertEqual(viewportCheck.windowInnerWidth, 360, 'Viewport width is 360px');
    assertEqual(viewportCheck.windowInnerHeight, 640, 'Viewport height is 640px');
    assert(viewportCheck.docScrollWidth <= 360, `No horizontal page overflow (docScrollWidth: ${viewportCheck.docScrollWidth}px <= 360px)`);

    // Check Bottom Nav buttons meet >= 44px touch targets
    const navButtons = await page.evaluate(() => {
      const nav = document.querySelector('nav');
      if (!nav) return [];
      return Array.from(nav.querySelectorAll('button')).map(btn => {
        const rect = btn.getBoundingClientRect();
        return {
          text: btn.innerText.trim(),
          width: Math.round(rect.width),
          height: Math.round(rect.height),
          top: Math.round(rect.top),
          bottom: Math.round(rect.bottom)
        };
      });
    });
    assertEqual(navButtons.length, 4, 'Bottom nav has 4 columns');
    navButtons.forEach(btn => {
      assert(btn.height >= 44, `Nav button "${btn.text}" height ${btn.height}px >= 44px`);
      assert(btn.width >= 44, `Nav button "${btn.text}" width ${btn.width}px >= 44px`);
    });

    // =========================================================================
    // TEST SUITE 2: Setor Tab — Steppers Hit Area & Propagation Isolation
    // =========================================================================
    console.log('\n--- Test Suite 2: Setor Tab Steppers & Event Isolation ---');
    await switchTab(page, 'setor');
    await delay(300);

    // Check and identify cards
    const initialCards = await page.evaluate(() => {
      const cards = Array.from(document.querySelectorAll('.grid.grid-cols-2 > div'));
      return cards.map(c => ({
        hasCheck: !!c.querySelector('.bg-emerald-600'),
        hasStepper: !!c.querySelector('[aria-label="Tambah berat"]')
      }));
    });
    assert(initialCards.length > 0, `Found ${initialCards.length} waste category cards in Setor`);

    // Ensure first card is selected
    if (!initialCards[0].hasStepper) {
      await page.evaluate(() => {
        const cards = Array.from(document.querySelectorAll('.grid.grid-cols-2 > div'));
        cards[0].click();
      });
      await delay(200);
    }

    // Check stepper dimensions
    const stepperMetrics = await page.evaluate(() => {
      const cards = Array.from(document.querySelectorAll('.grid.grid-cols-2 > div'));
      const selectedCard = cards.find(c => c.querySelector('[aria-label="Kurangi berat"]'));
      if (!selectedCard) return null;

      const minusBtn = selectedCard.querySelector('[aria-label="Kurangi berat"]');
      const plusBtn = selectedCard.querySelector('[aria-label="Tambah berat"]');
      const stepper = minusBtn.parentElement;
      const weightDisplay = stepper.querySelector('span.tabular-nums');

      const minusRect = minusBtn.getBoundingClientRect();
      const plusRect = plusBtn.getBoundingClientRect();
      const stepperRect = stepper.getBoundingClientRect();

      return {
        minus: { width: Math.round(minusRect.width), height: Math.round(minusRect.height) },
        plus: { width: Math.round(plusRect.width), height: Math.round(plusRect.height) },
        stepper: { width: Math.round(stepperRect.width), height: Math.round(stepperRect.height) },
        initialWeight: parseInt(weightDisplay.innerText.replace(/[^\d]/g, ''), 10)
      };
    });

    assert(stepperMetrics !== null, 'Stepper is rendered inside selected card');
    assert(stepperMetrics.minus.width >= 36 && stepperMetrics.minus.height >= 36,
      `Stepper Minus button size ${stepperMetrics.minus.width}x${stepperMetrics.minus.height}px meets compact touch standard (>= 36px)`);
    assert(stepperMetrics.plus.width >= 36 && stepperMetrics.plus.height >= 36,
      `Stepper Plus button size ${stepperMetrics.plus.width}x${stepperMetrics.plus.height}px meets compact touch standard (>= 36px)`);

    const w0 = stepperMetrics.initialWeight;

    // ACCIDENTAL CLICK TEST: Clicking Plus 3 times must NOT toggle parent card selection
    console.log(`  Testing stepper click propagation (Plus button from ${w0}kg)...`);
    for (let i = 0; i < 3; i++) {
      await page.evaluate(() => {
        const plusBtn = document.querySelector('[aria-label="Tambah berat"]');
        plusBtn.click();
      });
      await delay(100);
    }

    const afterPlusState = await page.evaluate(() => {
      const cards = Array.from(document.querySelectorAll('.grid.grid-cols-2 > div'));
      const card = cards.find(c => c.querySelector('[aria-label="Tambah berat"]')) || cards[0];
      const isSelected = card.classList.contains('border-emerald-500') || card.classList.contains('bg-emerald-50/70');
      const hasStepper = !!card.querySelector('[aria-label="Tambah berat"]');
      const weightText = card.querySelector('span.tabular-nums')?.innerText.trim();
      const weightNum = weightText ? parseInt(weightText.replace(/[^\d]/g, ''), 10) : null;
      return { isSelected, hasStepper, weightNum };
    });

    assert(afterPlusState.isSelected, 'Card remains SELECTED after clicking Plus button 3x (stopPropagation effective)');
    assert(afterPlusState.hasStepper, 'Stepper remains rendered after clicking Plus button');
    assertEqual(afterPlusState.weightNum, w0 + 3, `Weight correctly incremented by 3 (from ${w0}kg to ${w0 + 3}kg)`);

    // ACCIDENTAL CLICK TEST: Clicking Minus 2 times must NOT toggle parent card selection
    console.log(`  Testing stepper click propagation (Minus button from ${w0 + 3}kg)...`);
    for (let i = 0; i < 2; i++) {
      await page.evaluate(() => {
        const minusBtn = document.querySelector('[aria-label="Kurangi berat"]');
        minusBtn.click();
      });
      await delay(100);
    }

    const afterMinusState = await page.evaluate(() => {
      const cards = Array.from(document.querySelectorAll('.grid.grid-cols-2 > div'));
      const card = cards.find(c => c.querySelector('[aria-label="Kurangi berat"]')) || cards[0];
      const isSelected = card.classList.contains('border-emerald-500') || card.classList.contains('bg-emerald-50/70');
      const weightText = card.querySelector('span.tabular-nums')?.innerText.trim();
      const weightNum = weightText ? parseInt(weightText.replace(/[^\d]/g, ''), 10) : null;
      return { isSelected, weightNum };
    });

    assert(afterMinusState.isSelected, 'Card remains SELECTED after clicking Minus button 2x (stopPropagation effective)');
    assertEqual(afterMinusState.weightNum, w0 + 1, `Weight correctly decremented by 2 (from ${w0 + 3}kg to ${w0 + 1}kg)`);

    // ACCIDENTAL CLICK TEST: Clicking stepper wrapper background (between buttons)
    console.log('  Testing stepper wrapper click propagation...');
    await page.evaluate(() => {
      const plusBtn = document.querySelector('[aria-label="Tambah berat"]');
      const wrapper = plusBtn.parentElement.parentElement;
      wrapper.click();
    });
    await delay(100);

    const afterWrapperClick = await page.evaluate(() => {
      const cards = Array.from(document.querySelectorAll('.grid.grid-cols-2 > div'));
      const card = cards.find(c => c.querySelector('[aria-label="Tambah berat"]')) || cards[0];
      return card.classList.contains('border-emerald-500') || card.classList.contains('bg-emerald-50/70');
    });
    assert(afterWrapperClick, 'Card remains SELECTED after clicking stepper wrapper background');

    // Deselection test: Clicking directly on card title area outside stepper SHOULD toggle deselection
    console.log('  Testing card deselection when clicking outside stepper...');
    await page.evaluate(() => {
      const cards = Array.from(document.querySelectorAll('.grid.grid-cols-2 > div'));
      const card = cards.find(c => c.querySelector('[aria-label="Tambah berat"]')) || cards[0];
      const cardTitle = card.querySelector('p.font-bold');
      if (cardTitle) cardTitle.click();
      else card.click();
    });
    await delay(100);

    const afterDeselect = await page.evaluate(() => {
      const cards = Array.from(document.querySelectorAll('.grid.grid-cols-2 > div'));
      const card = cards[0];
      return {
        isSelected: card.classList.contains('border-emerald-500'),
        hasStepper: !!card.querySelector('[aria-label="Tambah berat"]')
      };
    });
    assert(!afterDeselect.isSelected, 'Card successfully DESELECTED when user taps card outside stepper');
    assert(!afterDeselect.hasStepper, 'Stepper hidden when card is deselected');

    // Re-select card for remaining tests
    await page.evaluate(() => {
      const cards = Array.from(document.querySelectorAll('.grid.grid-cols-2 > div'));
      cards[0].click();
    });
    await delay(100);

    // =========================================================================
    // TEST SUITE 3: Toko Tab — Filter Chips & Product Action Buttons
    // =========================================================================
    console.log('\n--- Test Suite 3: Toko Tab Chips & Button Touch Targets ---');
    await switchTab(page, 'toko');
    await delay(300);

    const chipMetrics = await page.evaluate(() => {
      const chipsContainer = document.querySelector('.overflow-x-auto');
      if (!chipsContainer) return [];
      const chips = Array.from(chipsContainer.querySelectorAll('button'));
      return chips.map(chip => {
        const rect = chip.getBoundingClientRect();
        return {
          text: chip.innerText.trim(),
          width: Math.round(rect.width),
          height: Math.round(rect.height),
          minHeightStyle: window.getComputedStyle(chip).minHeight
        };
      });
    });

    assert(chipMetrics.length >= 4, `Found ${chipMetrics.length} category filter chips in Toko`);
    chipMetrics.forEach(chip => {
      assert(chip.height >= 44, `Filter chip "${chip.text}" height ${chip.height}px >= 44px (minHeight: ${chip.minHeightStyle})`);
      assert(chip.width >= 44, `Filter chip "${chip.text}" width ${chip.width}px >= 44px`);
    });

    // Check Toko product Tukar button touch target
    const tukarButtonMetrics = await page.evaluate(() => {
      const tukarBtns = Array.from(document.querySelectorAll('button')).filter(b => b.innerText.trim() === 'Tukar');
      if (tukarBtns.length === 0) return null;
      const rect = tukarBtns[0].getBoundingClientRect();
      return {
        width: Math.round(rect.width),
        height: Math.round(rect.height),
        minHeightStyle: window.getComputedStyle(tukarBtns[0]).minHeight,
        minWidthStyle: window.getComputedStyle(tukarBtns[0]).minWidth
      };
    });

    assert(tukarButtonMetrics !== null, 'Product Tukar button found');
    assert(tukarButtonMetrics.height >= 44, `Tukar button height ${tukarButtonMetrics.height}px >= 44px`);
    assert(tukarButtonMetrics.width >= 44, `Tukar button width ${tukarButtonMetrics.width}px >= 44px (actual: ${tukarButtonMetrics.width}px)`);

    // =========================================================================
    // TEST SUITE 4: Dompet Tab — Cashout Channel Buttons & Amount Presets
    // =========================================================================
    console.log('\n--- Test Suite 4: Dompet Tab Cashout Targets ---');
    await switchTab(page, 'dompet');
    await delay(300);

    const cashoutChannelMetrics = await page.evaluate(() => {
      const channels = ['GoPay', 'DANA', 'OVO', 'BCA'];
      const buttons = Array.from(document.querySelectorAll('button')).filter(b => channels.includes(b.innerText.trim()));
      return buttons.map(b => {
        const rect = b.getBoundingClientRect();
        return {
          channel: b.innerText.trim(),
          width: Math.round(rect.width),
          height: Math.round(rect.height)
        };
      });
    });

    assertEqual(cashoutChannelMetrics.length, 4, 'Found all 4 cashout channels');
    cashoutChannelMetrics.forEach(c => {
      assert(c.height >= 44, `Cashout channel button "${c.channel}" height ${c.height}px >= 44px`);
      assert(c.width >= 44, `Cashout channel button "${c.channel}" width ${c.width}px >= 44px`);
    });

    const presetAmountMetrics = await page.evaluate(() => {
      const buttons = Array.from(document.querySelectorAll('button')).filter(b => {
        const txt = b.innerText.replace(/\s+/g, ' ').trim();
        return /(10|25|50|100)\.000/.test(txt);
      });
      return buttons.map(b => {
        const rect = b.getBoundingClientRect();
        return {
          amount: b.innerText.replace(/\s+/g, ' ').trim(),
          width: Math.round(rect.width),
          height: Math.round(rect.height)
        };
      });
    });

    assertEqual(presetAmountMetrics.length, 4, 'Found all 4 preset amount chips');
    presetAmountMetrics.forEach(p => {
      assert(p.height >= 44, `Preset chip "${p.amount}" height ${p.height}px >= 44px`);
      assert(p.width >= 44, `Preset chip "${p.amount}" width ${p.width}px >= 44px`);
    });

    // Check Cashout Submit Button
    const submitCashoutMetrics = await page.evaluate(() => {
      const submitBtn = Array.from(document.querySelectorAll('button')).find(b => b.innerText.includes('Cairkan Sekarang'));
      if (!submitBtn) return null;
      const rect = submitBtn.getBoundingClientRect();
      return {
        width: Math.round(rect.width),
        height: Math.round(rect.height)
      };
    });
    assert(submitCashoutMetrics !== null, 'Submit Cashout button found');
    assert(submitCashoutMetrics.height >= 44, `Submit Cashout button height ${submitCashoutMetrics.height}px >= 44px`);

    // =========================================================================
    // TEST SUITE 5: Modal Scrolling & Ergonomics on Short 360x640px Viewport
    // =========================================================================
    console.log('\n--- Test Suite 5: Modal Scrolling on Short Viewport (360x640px) ---');
    const viewportHeight = 640;
    const maxAllowedModalHeight = Math.round(viewportHeight * 0.9); // 90dvh = 576px

    // Helper to evaluate modal ergonomics
    async function testModalErgonomics(modalName, triggerFn, closeFn, actionButtonSelector) {
      console.log(`\n  Testing Modal: [${modalName}]`);
      await triggerFn();
      await delay(400);

      const modalInfo = await page.evaluate(() => {
        const backdrop = document.querySelector('.fixed.inset-0.z-50');
        if (!backdrop) return null;
        const dialog = backdrop.querySelector('.overflow-y-auto') || backdrop.firstElementChild;
        if (!dialog) return null;

        const rect = dialog.getBoundingClientRect();
        const style = window.getComputedStyle(dialog);

        return {
          width: Math.round(rect.width),
          height: Math.round(rect.height),
          top: Math.round(rect.top),
          bottom: Math.round(rect.bottom),
          scrollHeight: dialog.scrollHeight,
          clientHeight: dialog.clientHeight,
          overflowY: style.overflowY,
          maxHeight: style.maxHeight
        };
      });

      assert(modalInfo !== null, `${modalName} rendered with dialog container`);
      if (!modalInfo) {
        return;
      }

      assert(modalInfo.height <= maxAllowedModalHeight + 2,
        `${modalName} height ${modalInfo.height}px fits within 90dvh (${maxAllowedModalHeight}px)`);
      assert(modalInfo.overflowY === 'auto' || modalInfo.overflowY === 'scroll',
        `${modalName} has overflow-y: ${modalInfo.overflowY} for smooth scrolling`);

      // Test scrolling down to action button
      if (actionButtonSelector) {
        const buttonCheck = await page.evaluate((sel) => {
          const backdrop = document.querySelector('.fixed.inset-0.z-50');
          const dialog = backdrop ? (backdrop.querySelector('.overflow-y-auto') || backdrop.firstElementChild) : null;
          if (!dialog) return { found: false };

          // Scroll dialog to bottom
          dialog.scrollTop = dialog.scrollHeight;
          const btn = dialog.querySelector(sel);
          if (!btn) return { found: false };
          const btnRect = btn.getBoundingClientRect();
          const dialogRect = dialog.getBoundingClientRect();

          // Verify button is inside dialog visible bounds (not clipped)
          const isInsideDialog = (btnRect.top >= dialogRect.top - 5) && (btnRect.bottom <= dialogRect.bottom + 5);
          const isInsideViewport = (btnRect.top >= 0) && (btnRect.bottom <= window.innerHeight);

          return {
            found: true,
            isInsideDialog,
            isInsideViewport,
            btnHeight: Math.round(btnRect.height),
            btnTop: Math.round(btnRect.top),
            btnBottom: Math.round(btnRect.bottom),
            dialogTop: Math.round(dialogRect.top),
            dialogBottom: Math.round(dialogRect.bottom)
          };
        }, actionButtonSelector);

        assert(buttonCheck.found, `${modalName} contains specified action button (${actionButtonSelector})`);
        if (buttonCheck.found) {
          assert(buttonCheck.isInsideViewport, `${modalName} action button is inside viewport (top:${buttonCheck.btnTop}, bottom:${buttonCheck.btnBottom})`);
          assert(buttonCheck.btnHeight >= 36, `${modalName} action button height ${buttonCheck.btnHeight}px meets hit area standard`);
        }
      }

      await closeFn();
      await delay(300);
    }

    // 5.1 Modal: Profil Warga
    await testModalErgonomics(
      'Profil Warga Modal',
      async () => {
        await switchTab(page, 'beranda');
        await delay(200);
        await page.evaluate(() => {
          const profileBtn = document.querySelector('button[aria-label="Profil Warga"]');
          if (profileBtn) profileBtn.click();
        });
      },
      async () => {
        await page.evaluate(() => {
          const closeBtn = document.querySelector('[aria-label="Tutup Profil"]') ||
            document.querySelector('.fixed.inset-0.z-50 button');
          if (closeBtn) closeBtn.click();
        });
      },
      'button.bg-gradient-to-r' // Masuk ke Portal Mitra button
    );

    // 5.2 Modal: Eco-Impact Certificate
    await testModalErgonomics(
      'Eco-Impact Certificate Modal',
      async () => {
        await switchTab(page, 'beranda');
        await delay(200);
        await page.evaluate(() => {
          const certTrigger = Array.from(document.querySelectorAll('button')).find(b => b.innerText.includes('Sertifikat'));
          if (certTrigger) certTrigger.click();
        });
      },
      async () => {
        await page.evaluate(() => {
          const closeBtn = document.querySelector('.fixed.inset-0.z-50 button.text-slate-400');
          if (closeBtn) closeBtn.click();
        });
      },
      'button.bg-emerald-500' // Bagikan ke IG Story button
    );

    // 5.3 Modal: Notification Drawer
    await testModalErgonomics(
      'Notification Drawer Modal',
      async () => {
        await switchTab(page, 'beranda');
        await delay(200);
        await page.evaluate(() => {
          const bellBtn = Array.from(document.querySelectorAll('button')).find(b =>
            b.querySelector('svg.lucide-bell') || b.innerHTML.includes('bell')
          );
          if (bellBtn) bellBtn.click();
        });
      },
      async () => {
        await page.evaluate(() => {
          const closeBtn = document.querySelector('.fixed.inset-0.z-50 button');
          if (closeBtn) closeBtn.click();
        });
      },
      null
    );

    // 5.4 Modal: Toko Product Purchase
    await testModalErgonomics(
      'Toko Product Purchase Modal',
      async () => {
        await switchTab(page, 'toko');
        await delay(200);
        await page.evaluate(() => {
          const tukarBtn = Array.from(document.querySelectorAll('button')).find(b => b.innerText.trim() === 'Tukar');
          if (tukarBtn) tukarBtn.click();
        });
      },
      async () => {
        await page.evaluate(() => {
          const closeBtn = document.querySelector('.fixed.inset-0.z-50 button.text-slate-400');
          if (closeBtn) closeBtn.click();
        });
      },
      'button.bg-emerald-600' // Konfirmasi Tukar button
    );

    // 5.5 Modal: Deposit Ticket & Weighing Simulation
    await testModalErgonomics(
      'Deposit Ticket Modal',
      async () => {
        await switchTab(page, 'setor');
        await delay(200);
        // Ensure card is selected
        await page.evaluate(() => {
          const card = document.querySelector('.grid.grid-cols-2 > div');
          if (card && !card.classList.contains('border-emerald-500')) {
            card.click();
          }
        });
        await delay(200);
        // Click submit deposit
        await page.evaluate(() => {
          const submitBtn = Array.from(document.querySelectorAll('button')).find(b =>
            b.innerText.includes('Buat Tiket') || b.innerText.includes('Dapatkan Tiket')
          );
          if (submitBtn) submitBtn.click();
        });
      },
      async () => {
        await page.evaluate(() => {
          const closeBtn = document.querySelector('.fixed.inset-0.z-50 button.text-slate-400');
          if (closeBtn) closeBtn.click();
        });
      },
      'button.bg-emerald-600' // Simulasikan Timbangan button
    );

    // Check Console & Page Errors
    console.log('\n--- Error Summary ---');
    assertEqual(consoleErrors.length, 0, 'No console error logs recorded during stress run');
    assertEqual(pageErrors.length, 0, 'No uncaught page errors recorded during stress run');

  } catch (err) {
    console.error('Fatal stress test runner exception:', err);
    failCount++;
  } finally {
    await browser.close();
  }

  console.log('\n===================================================================');
  console.log(`STRESS RESULTS: ${passCount} Passed, ${failCount} Failed`);
  console.log('===================================================================');

  if (failCount > 0) {
    process.exit(1);
  } else {
    process.exit(0);
  }
}

runChallengerStressTestsM3();
