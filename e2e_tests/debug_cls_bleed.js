import { launchBrowser, createPage, openApp, switchTab, delay } from './helpers.js';

async function debugCLS() {
  const browser = await launchBrowser();
  const page = await createPage(browser, { width: 390, height: 844 });
  await openApp(page);

  console.log('\n--- DIAGNOSING BLEEDING ELEMENTS ---');
  for (const tab of ['home', 'setor', 'toko', 'dompet']) {
    await switchTab(page, tab);
    await delay(200);

    const bleed = await page.evaluate((currentTab) => {
      const innerW = window.innerWidth;
      const all = Array.from(document.querySelectorAll('*'));
      const items = [];
      for (const el of all) {
        if (['SCRIPT', 'STYLE', 'META', 'HEAD', 'TITLE'].includes(el.tagName)) continue;
        const rect = el.getBoundingClientRect();
        if (rect.right > innerW + 1.5 || rect.left < -1.5) {
          items.push({
            tab: currentTab,
            tag: el.tagName,
            id: el.id,
            className: el.className,
            text: (el.innerText || '').slice(0, 30),
            left: rect.left,
            right: rect.right,
            width: rect.width,
            parentOverflow: window.getComputedStyle(el.parentElement).overflow
          });
        }
      }
      return items;
    }, tab);

    console.log(`Tab ${tab}: found ${bleed.length} bleeding elements:`);
    for (const b of bleed) {
      console.log(`  - Tag: ${b.tag}, text: "${b.text}", left: ${b.left}, right: ${b.right}, parentOverflow: ${b.parentOverflow}, class: ${b.className}`);
    }
  }

  console.log('\n--- DIAGNOSING CLS (Cumulative Layout Shift) ---');
  // Re-open and monitor CLS from fresh state
  await openApp(page);
  await delay(500);

  await page.evaluate(() => {
    window.__shifts = [];
    const obs = new PerformanceObserver((list) => {
      for (const entry of list.getEntries()) {
        window.__shifts.push({
          value: entry.value,
          hadRecentInput: entry.hadRecentInput,
          time: entry.startTime,
          sources: entry.sources ? entry.sources.map(s => ({
            tag: s.node ? s.node.tagName : null,
            class: s.node ? s.node.className : null,
            text: s.node && s.node.innerText ? s.node.innerText.slice(0, 40) : null,
            prevRect: s.previousRect,
            currRect: s.currentRect
          })) : []
        });
      }
    });
    obs.observe({ type: 'layout-shift', buffered: true });
  });

  const tabs = ['setor', 'toko', 'dompet', 'home'];
  for (const t of tabs) {
    console.log(`Switching to ${t}...`);
    await switchTab(page, t);
    await delay(300);
  }

  const shiftData = await page.evaluate(() => window.__shifts);
  console.log(`Total shift entries recorded: ${shiftData.length}`);
  for (let i = 0; i < shiftData.length; i++) {
    const s = shiftData[i];
    console.log(`\nShift #${i + 1}: value=${s.value}, hadRecentInput=${s.hadRecentInput}, time=${s.time}`);
    for (const src of s.sources) {
      console.log(`  Source: ${src.tag}.${src.class} ("${src.text}")`);
      console.log(`    prev:`, src.prevRect);
      console.log(`    curr:`, src.currRect);
    }
  }

  await browser.close();
}

debugCLS();
