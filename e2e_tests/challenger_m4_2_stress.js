import { launchBrowser, createPage, openApp, switchTab, delay, clickByText } from './helpers.js';

/**
 * CHALLENGER M4_2: Multi-Device Responsive Stress Test Harness
 * 
 * Target Viewports:
 * 1. 360x640 (Small Android)
 * 2. 375x667 (iPhone SE)
 * 3. 390x844 (iPhone 13/14/15)
 * 4. 412x915 (Samsung Galaxy S20/Ultra)
 * 5. 430x932 (iPhone Pro Max)
 */

const VIEWPORTS = [
  { name: 'Small Android (360x640)', width: 360, height: 640 },
  { name: 'iPhone SE (375x667)', width: 375, height: 667 },
  { name: 'iPhone 13/14/15 (390x844)', width: 390, height: 844 },
  { name: 'Samsung Galaxy (412x915)', width: 412, height: 915 },
  { name: 'iPhone Pro Max (430x932)', width: 430, height: 932 }
];

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

async function runEmpiricalStressTest() {
  console.log('======================================================================');
  console.log('      CHALLENGER M4_2: EMPIRICAL MULTI-DEVICE RESPONSIVE SUITE       ');
  console.log('======================================================================\n');

  const browser = await launchBrowser();

  try {
    for (const vp of VIEWPORTS) {
      console.log(`\n======================================================================`);
      console.log(`▶ VIEWPORT: ${vp.name} (${vp.width}x${vp.height})`);
      console.log(`======================================================================`);

      const page = await createPage(browser, { width: vp.width, height: vp.height });
      await openApp(page);
      await delay(500);
      await page.evaluate(() => document.fonts.ready);

      // ------------------------------------------------------------------
      // 1. CLS (Cumulative Layout Shift) Measurement across Tab Switches
      // ------------------------------------------------------------------
      console.log(`\n  [Test 1: Cumulative Layout Shift (CLS)]`);
      await page.evaluate(() => {
        window.__shifts = [];
        const observer = new PerformanceObserver((entryList) => {
          for (const entry of entryList.getEntries()) {
            if (!entry.hadRecentInput) {
              window.__shifts.push({
                value: entry.value,
                hadRecentInput: entry.hadRecentInput,
                time: entry.startTime
              });
            }
          }
        });
        observer.observe({ type: 'layout-shift', buffered: false });
      });

      // Switch through all tabs
      for (const tab of ['setor', 'toko', 'dompet', 'home']) {
        await switchTab(page, tab);
        await delay(150);
      }

      const shifts = await page.evaluate(() => window.__shifts || []);
      const totalShift = shifts.reduce((acc, s) => acc + s.value, 0);
      check(totalShift === 0, `${vp.name}: Cumulative Layout Shift (CLS) = ${totalShift.toFixed(4)} (Expected: 0.000)`);

      // ------------------------------------------------------------------
      // 2. Horizontal Overflow & Element Bleed Test across all tabs
      // ------------------------------------------------------------------
      console.log(`\n  [Test 2: Zero Horizontal Overflow & Bleed across Tabs]`);
      for (const tab of ['home', 'setor', 'toko', 'dompet']) {
        await switchTab(page, tab);
        await delay(150);

        const overflowInfo = await page.evaluate((tabName) => {
          const docScroll = document.documentElement.scrollWidth;
          const bodyScroll = document.body.scrollWidth;
          const innerW = window.innerWidth;
          
          // Bleeding elements
          const allElements = Array.from(document.querySelectorAll('*'));
          const bleeding = [];
          for (const el of allElements) {
            if (['SCRIPT', 'STYLE', 'META', 'HEAD', 'TITLE'].includes(el.tagName)) continue;
            const rect = el.getBoundingClientRect();
            // Allow 1px tolerance for subpixel anti-aliasing
            if (rect.right > innerW + 1.5 || rect.left < -1.5) {
              // check if any parent has overflow: hidden
              let p = el.parentElement;
              let isClipped = false;
              while (p) {
                const s = window.getComputedStyle(p);
                if (s.overflow === 'hidden' || s.overflowX === 'hidden') {
                  isClipped = true;
                  break;
                }
                p = p.parentElement;
              }
              if (!isClipped) {
                bleeding.push({
                  tag: el.tagName,
                  className: el.className,
                  text: (el.innerText || '').slice(0, 30),
                  rect: { left: rect.left, right: rect.right, width: rect.width }
                });
              }
            }
          }

          return {
            docScroll,
            bodyScroll,
            innerW,
            hasDocScroll: docScroll > innerW,
            hasBodyScroll: bodyScroll > innerW,
            bleedingCount: bleeding.length,
            bleeding
          };
        }, tab);

        check(!overflowInfo.hasDocScroll && !overflowInfo.hasBodyScroll, 
          `${vp.name} [Tab: ${tab}]: Zero page horizontal scroll (Doc: ${overflowInfo.docScroll}px, Body: ${overflowInfo.bodyScroll}px <= Viewport: ${overflowInfo.innerW}px)`);
        check(overflowInfo.bleedingCount === 0, 
          `${vp.name} [Tab: ${tab}]: Zero unclipped bleeding elements (Found: ${overflowInfo.bleedingCount})`);
      }

      // ------------------------------------------------------------------
      // 3. Double-Scroll & Scroll Architecture Analysis
      // ------------------------------------------------------------------
      console.log(`\n  [Test 3: Double-Scroll & Scroll Container Architecture]`);
      const scrollInfo = await page.evaluate(() => {
        // Find all scrollable containers in the document
        const scrollContainers = [];
        const allElements = Array.from(document.querySelectorAll('*'));
        
        for (const el of allElements) {
          if (['SCRIPT', 'STYLE'].includes(el.tagName)) continue;
          const style = window.getComputedStyle(el);
          const hasScrollY = style.overflowY === 'scroll' || style.overflowY === 'auto';
          if (hasScrollY && el.scrollHeight > el.clientHeight + 5 && el !== document.documentElement && el !== document.body) {
            scrollContainers.push({
              tag: el.tagName,
              className: el.className,
              scrollHeight: el.scrollHeight,
              clientHeight: el.clientHeight
            });
          }
        }

        return {
          windowScrollable: document.documentElement.scrollHeight > window.innerHeight,
          scrollContainersCount: scrollContainers.length,
          scrollContainers
        };
      });

      // In clean single-scroll mobile layouts, the page scrolls via the root window,
      // without nested nested full-page scrolling containers causing double scrollbars.
      check(scrollInfo.scrollContainersCount === 0, 
        `${vp.name}: No competing vertical scroll containers on default screen (Found: ${scrollInfo.scrollContainersCount})`);

      // Verify scroll down and content padding bottom (pb-24)
      await switchTab(page, 'toko');
      await delay(150);

      const contentOcclusion = await page.evaluate(() => {
        // Scroll to the bottom
        window.scrollTo(0, document.documentElement.scrollHeight);
        const nav = document.querySelector('nav');
        const navRect = nav.getBoundingClientRect();
        
        // Find the last visible card or item
        const cards = Array.from(document.querySelectorAll('.grid > div, .space-y-4 > div'));
        if (cards.length === 0) return { occluded: false, distance: 999 };
        const lastCard = cards[cards.length - 1];
        const lastCardRect = lastCard.getBoundingClientRect();

        return {
          windowScrollY: window.scrollY,
          lastCardBottom: lastCardRect.bottom,
          navTop: navRect.top,
          // Content is occluded if its bottom is deeper than the nav top
          occluded: lastCardRect.bottom > navRect.top,
          clearance: navRect.top - lastCardRect.bottom
        };
      });

      check(!contentOcclusion.occluded, 
        `${vp.name}: Bottom content is fully readable and not occluded behind fixed navbar (Clearance: ${contentOcclusion.clearance.toFixed(1)}px)`);

      // Scroll back up
      await page.evaluate(() => window.scrollTo(0, 0));

      // ------------------------------------------------------------------
      // 4. Anchored Bottom Navigation Bar
      // ------------------------------------------------------------------
      console.log(`\n  [Test 4: Fixed Anchored Bottom Navbar]`);
      const navMetrics = await page.evaluate(() => {
        const nav = document.querySelector('nav');
        if (!nav) return null;
        const rect = nav.getBoundingClientRect();
        const style = window.getComputedStyle(nav);
        const buttons = Array.from(nav.querySelectorAll('button'));

        return {
          position: style.position,
          bottom: rect.bottom,
          windowHeight: window.innerHeight,
          width: rect.width,
          windowWidth: window.innerWidth,
          isAnchoredToBottom: Math.abs(rect.bottom - window.innerHeight) <= 1,
          buttonCount: buttons.length,
          touchTargets: buttons.map(b => {
            const bRect = b.getBoundingClientRect();
            return {
              text: b.innerText.trim(),
              width: bRect.width,
              height: bRect.height,
              meetsTarget: bRect.width >= 44 && bRect.height >= 44
            };
          })
        };
      });

      check(navMetrics && navMetrics.position === 'fixed', `${vp.name}: Navbar position is 'fixed'`);
      check(navMetrics && navMetrics.isAnchoredToBottom, `${vp.name}: Navbar bottom (${navMetrics?.bottom}px) perfectly aligns with viewport bottom (${navMetrics?.windowHeight}px)`);
      check(navMetrics && navMetrics.buttonCount === 4, `${vp.name}: Navbar has exactly 4 navigation items`);
      
      const allTouchOk = navMetrics && navMetrics.touchTargets.every(t => t.meetsTarget);
      check(allTouchOk, `${vp.name}: All 4 navbar buttons meet standard touch target >= 44x44px`);

      // ------------------------------------------------------------------
      // 5. Responsive Modals & Unclipped Scroll Ergonomics
      // ------------------------------------------------------------------
      console.log(`\n  [Test 5: Responsive Modals Scrolling & Button Reachability]`);
      await switchTab(page, 'home');
      await delay(150);

      // 5.1 Profile Modal
      const avatarBtn = await page.$('button[aria-label="Profil Warga"]');
      if (avatarBtn) {
        await avatarBtn.click();
        await delay(250);

        const profileModalCheck = await page.evaluate(() => {
          const modal = document.querySelector('.fixed.inset-0 .max-h-\\[90dvh\\]');
          if (!modal) return { exists: false };
          const rect = modal.getBoundingClientRect();
          const winH = window.innerHeight;
          const winW = window.innerWidth;
          
          // Look for partner portal button at the bottom of profile modal
          const btns = Array.from(modal.querySelectorAll('button'));
          const partnerBtn = btns.find(b => b.innerText && b.innerText.includes('Portal Mitra Pengelola'));
          let partnerBtnReach = false;
          if (partnerBtn) {
            // Scroll modal container to bottom
            modal.scrollTop = modal.scrollHeight;
            const bRect = partnerBtn.getBoundingClientRect();
            // Check button is within viewport bounds
            partnerBtnReach = bRect.top >= 0 && bRect.bottom <= winH;
          }

          return {
            exists: true,
            fitsInViewport: rect.height <= winH && rect.width <= winW,
            hasOverflowY: window.getComputedStyle(modal).overflowY === 'auto',
            partnerBtnReach
          };
        });

        check(profileModalCheck.exists && profileModalCheck.fitsInViewport, 
          `${vp.name}: Profile Modal fits within viewport constraints without clipping`);
        check(profileModalCheck.hasOverflowY, 
          `${vp.name}: Profile Modal has overflow-y: auto for smooth scrolling`);
        check(profileModalCheck.partnerBtnReach, 
          `${vp.name}: Profile Modal bottom button ('Portal Mitra Pengelola') is reachable and scrollable into view`);

        // Close profile modal
        const closeProfileBtn = await page.$('button[aria-label="Tutup Profil"]');
        if (closeProfileBtn) {
          await closeProfileBtn.click();
        } else {
          await page.evaluate(() => {
            const closeBtn = document.querySelector('.fixed.inset-0 button');
            if (closeBtn) closeBtn.click();
          });
        }
        await delay(200);
      }

      // 5.2 Toko Sirkular Product Modal
      await switchTab(page, 'toko');
      await delay(200);

      const productClicked = await page.evaluate(() => {
        const cards = Array.from(document.querySelectorAll('.grid > div'));
        if (cards.length > 0) {
          cards[0].click();
          return true;
        }
        return false;
      });

      if (productClicked) {
        await delay(250);
        const productModalCheck = await page.evaluate(() => {
          const modal = document.querySelector('.fixed.inset-0 .max-h-\\[90dvh\\]');
          if (!modal) return { exists: false };
          const winH = window.innerHeight;
          const rect = modal.getBoundingClientRect();
          
          const confirmBtn = Array.from(modal.querySelectorAll('button'))
            .find(b => b.innerText && b.innerText.includes('Konfirmasi'));

          let confirmBtnReach = false;
          if (confirmBtn) {
            modal.scrollTop = modal.scrollHeight;
            const bRect = confirmBtn.getBoundingClientRect();
            confirmBtnReach = bRect.top >= 0 && bRect.bottom <= winH;
          }

          return {
            exists: true,
            fitsInViewport: rect.height <= winH,
            hasOverflowY: window.getComputedStyle(modal).overflowY === 'auto',
            confirmBtnReach
          };
        });

        check(productModalCheck.exists && productModalCheck.fitsInViewport, 
          `${vp.name}: Toko Product Modal fits within 90dvh bounds`);
        check(productModalCheck.confirmBtnReach, 
          `${vp.name}: Toko Product Modal action button ('Konfirmasi') is fully reachable and not clipped`);

        // Close product modal
        await page.evaluate(() => {
          const closeBtn = document.querySelector('.fixed.inset-0 button');
          if (closeBtn) closeBtn.click();
        });
        await delay(200);
      }

      // 5.3 Setor Sampah Deposit Ticket Modal
      await switchTab(page, 'setor');
      await delay(200);

      // Click "Lanjutkan & Terbitkan Tiket Penyetoran"
      const ticketIssued = await clickByText(page, 'Lanjutkan & Terbitkan Tiket');
      if (ticketIssued) {
        await delay(300);
        const ticketModalCheck = await page.evaluate(() => {
          const modal = document.querySelector('.fixed.inset-0 .max-h-\\[90dvh\\]');
          if (!modal) return { exists: false };
          const winH = window.innerHeight;
          const rect = modal.getBoundingClientRect();
          
          const simulateBtn = Array.from(modal.querySelectorAll('button'))
            .find(b => b.innerText && b.innerText.includes('Simulasikan Timbangan'));

          let simulateBtnReach = false;
          if (simulateBtn) {
            modal.scrollTop = modal.scrollHeight;
            const bRect = simulateBtn.getBoundingClientRect();
            simulateBtnReach = bRect.top >= 0 && bRect.bottom <= winH;
          }

          return {
            exists: true,
            fitsInViewport: rect.height <= winH,
            hasOverflowY: window.getComputedStyle(modal).overflowY === 'auto',
            simulateBtnReach
          };
        });

        check(ticketModalCheck.exists && ticketModalCheck.fitsInViewport, 
          `${vp.name}: Deposit Ticket Modal fits within 90dvh bounds`);
        check(ticketModalCheck.simulateBtnReach, 
          `${vp.name}: Deposit Ticket Modal bottom button ('Simulasikan Timbangan') is reachable`);

        // Close ticket modal
        await page.evaluate(() => {
          const closeBtn = document.querySelector('.fixed.inset-0 button');
          if (closeBtn) closeBtn.click();
        });
        await delay(200);
      }

      // ------------------------------------------------------------------
      // 6. Partner Mode Layout & Ergonomics
      // ------------------------------------------------------------------
      console.log(`\n  [Test 6: Partner Portal Viewport Responsiveness]`);
      await switchTab(page, 'home');
      await delay(150);

      // Open profile modal and switch to partner
      const avatarForPartner = await page.$('button[aria-label="Profil Warga"]');
      if (avatarForPartner) {
        await avatarForPartner.click();
        await delay(200);
        await page.evaluate(() => {
          const btns = Array.from(document.querySelectorAll('button'));
          const pBtn = btns.find(b => b.innerText && b.innerText.includes('Portal Mitra Pengelola'));
          if (pBtn) pBtn.click();
        });
        await delay(300);

        const partnerMetrics = await page.evaluate(() => {
          const docScroll = document.documentElement.scrollWidth;
          const innerW = window.innerWidth;
          const backBtn = document.querySelector('button[aria-label="Kembali ke Akun Warga"]');
          const hasBackBtn = !!backBtn;
          const scaleInputs = Array.from(document.querySelectorAll('input[type="number"], input'));

          return {
            docScroll,
            innerW,
            hasHorizontalScroll: docScroll > innerW,
            hasBackBtn,
            scaleInputsCount: scaleInputs.length
          };
        });

        check(!partnerMetrics.hasHorizontalScroll, 
          `${vp.name} [Partner Mode]: Zero horizontal overflow (${partnerMetrics.docScroll}px <= ${partnerMetrics.innerW}px)`);
        check(partnerMetrics.hasBackBtn, 
          `${vp.name} [Partner Mode]: Clear 'Kembali ke Akun Warga' header button present`);

        // Switch back to citizen
        await page.evaluate(() => {
          const backBtn = document.querySelector('button[aria-label="Kembali ke Akun Warga"]');
          if (backBtn) backBtn.click();
        });
        await delay(200);
      }

      await page.close();
    }

    // ------------------------------------------------------------------
    // 7. Dynamic Viewport Resizing Stress (Rapid Shrink/Expand)
    // ------------------------------------------------------------------
    console.log(`\n======================================================================`);
    console.log(`▶ DYNAMIC RESIZING STRESS (360 -> 430 -> 360 px)`);
    console.log(`======================================================================`);

    const dynamicPage = await createPage(browser, { width: 360, height: 640 });
    await openApp(dynamicPage);

    const resizeSequence = [
      { width: 375, height: 667 },
      { width: 390, height: 844 },
      { width: 412, height: 915 },
      { width: 430, height: 932 },
      { width: 360, height: 640 }
    ];

    for (const targetDim of resizeSequence) {
      await dynamicPage.setViewport(targetDim);
      await delay(100);

      const overflow = await dynamicPage.evaluate(() => {
        return document.documentElement.scrollWidth > window.innerWidth;
      });
      check(!overflow, `Dynamic Resize to ${targetDim.width}x${targetDim.height}: zero horizontal overflow`);

      const navAnchored = await dynamicPage.evaluate(() => {
        const nav = document.querySelector('nav');
        if (!nav) return false;
        const rect = nav.getBoundingClientRect();
        return Math.abs(rect.bottom - window.innerHeight) <= 1;
      });
      check(navAnchored, `Dynamic Resize to ${targetDim.width}x${targetDim.height}: navbar stays bottom-anchored`);
    }

    await dynamicPage.close();

  } finally {
    await browser.close();
  }

  console.log('\n======================================================================');
  console.log(`CHALLENGER M4_2 SUMMARY: ${passedChecks}/${totalChecks} PASSED (${failedChecks} FAILED)`);
  console.log('======================================================================');

  if (failedChecks > 0) {
    console.error('\nFailures recorded:');
    failureLog.forEach(f => console.error(` - ${f}`));
    process.exit(1);
  } else {
    console.log('\n🎉 ALL EMPIRICAL RESPONSIVE & LAYOUT STRESS CHECKS PASSED WITH 0 DEFECTS!');
    process.exit(0);
  }
}

runEmpiricalStressTest().catch(err => {
  console.error('Fatal stress test execution error:', err);
  process.exit(1);
});
