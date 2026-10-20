import { launchBrowser, createPage, openApp, switchTab, delay } from './helpers.js';

async function verifyResponsiveViewports() {
  console.log('===============================================================');
  console.log('   PILAH.IN — MULTI-VIEWPORT RESPONSIVENESS VERIFICATION (M4)  ');
  console.log('   Testing viewports: 360px, 375px, 390px, 412px, 430px       ');
  console.log('===============================================================');

  const viewports = [
    { name: 'Small Android (360x640)', width: 360, height: 640 },
    { name: 'iPhone SE (375x667)', width: 375, height: 667 },
    { name: 'iPhone 13/14/15 (390x844)', width: 390, height: 844 },
    { name: 'Samsung Galaxy (412x915)', width: 412, height: 915 },
    { name: 'iPhone Pro Max (430x932)', width: 430, height: 932 }
  ];

  const browser = await launchBrowser();
  let totalTests = 0;
  let passedTests = 0;
  let failedTests = 0;

  function assert(condition, message) {
    totalTests++;
    if (condition) {
      console.log(`  ✅ [PASS] ${message}`);
      passedTests++;
    } else {
      console.error(`  ❌ [FAIL] ${message}`);
      failedTests++;
    }
  }

  for (const vp of viewports) {
    console.log(`\n▶ Testing Viewport: ${vp.name} [${vp.width}x${vp.height}px]`);
    const page = await createPage(browser, { width: vp.width, height: vp.height });
    await openApp(page);

    // 1. Verify No Horizontal Page Overflow on Initial Load (Home)
    const homeOverflow = await page.evaluate(() => {
      return {
        docScrollWidth: document.documentElement.scrollWidth,
        bodyScrollWidth: document.body.scrollWidth,
        innerWidth: window.innerWidth,
        hasHorizontalScroll: document.documentElement.scrollWidth > window.innerWidth
      };
    });
    assert(!homeOverflow.hasHorizontalScroll, `${vp.name}: Home page has no horizontal overflow (${homeOverflow.docScrollWidth}px <= ${homeOverflow.innerWidth}px)`);

    // 2. Test each tab in the viewport
    for (const tab of ['home', 'setor', 'toko', 'dompet']) {
      await switchTab(page, tab);
      await delay(150);

      const tabOverflow = await page.evaluate(() => {
        return {
          docScrollWidth: document.documentElement.scrollWidth,
          bodyScrollWidth: document.body.scrollWidth,
          innerWidth: window.innerWidth,
          hasHorizontalScroll: document.documentElement.scrollWidth > window.innerWidth
        };
      });
      assert(!tabOverflow.hasHorizontalScroll, `${vp.name} [Tab: ${tab}]: Zero page horizontal scroll (${tabOverflow.docScrollWidth}px <= ${tabOverflow.innerWidth}px)`);

      // Verify bottom nav is intact and visible
      const navBounds = await page.evaluate(() => {
        const nav = document.querySelector('nav');
        if (!nav) return null;
        const rect = nav.getBoundingClientRect();
        const btns = nav.querySelectorAll('button');
        return {
          visible: rect.height > 0 && rect.width > 0,
          buttonCount: btns.length,
          allMinHeight: Array.from(btns).every(b => b.getBoundingClientRect().height >= 44)
        };
      });
      assert(navBounds && navBounds.visible && navBounds.buttonCount === 4, `${vp.name} [Tab: ${tab}]: Bottom navbar properly positioned with 4 columns`);
    }

    // 3. Verify Partner Mode Viewport Responsiveness
    // Open Profile -> Switch to Partner
    const profileAvatar = await page.$('button[aria-label="Profil Warga"]');
    if (profileAvatar) {
      await profileAvatar.click();
      await delay(250);

      // Find Partner Button
      const switched = await page.evaluate(() => {
        const btns = Array.from(document.querySelectorAll('button'));
        const pBtn = btns.find(b => b.innerText && b.innerText.includes('Portal Mitra Pengelola'));
        if (pBtn) {
          pBtn.click();
          return true;
        }
        return false;
      });
      await delay(300);

      if (switched) {
        const partnerOverflow = await page.evaluate(() => {
          return {
            docScrollWidth: document.documentElement.scrollWidth,
            innerWidth: window.innerWidth,
            hasHorizontalScroll: document.documentElement.scrollWidth > window.innerWidth
          };
        });
        assert(!partnerOverflow.hasHorizontalScroll, `${vp.name} [Partner Mode]: Zero horizontal overflow (${partnerOverflow.docScrollWidth}px <= ${partnerOverflow.innerWidth}px)`);

        // Switch back to citizen
        await page.evaluate(() => {
          const backBtn = document.querySelector('button[aria-label="Kembali ke Akun Warga"]');
          if (backBtn) backBtn.click();
        });
        await delay(200);
      }
    }

    await page.close();
  }

  await browser.close();

  console.log('\n===============================================================');
  console.log(`MULTI-VIEWPORT VERIFICATION SUMMARY: ${passedTests}/${totalTests} Passed (${failedTests} Failed)`);
  console.log('===============================================================');

  if (failedTests > 0) process.exit(1);
}

verifyResponsiveViewports().catch(err => {
  console.error('Fatal viewport verification error:', err);
  process.exit(1);
});
