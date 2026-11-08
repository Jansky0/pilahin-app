import { launchBrowser, DEFAULT_APP_URL } from './helpers.js';

(async () => {
  console.log('🚀 Testing Tinder-Style Swipe & Poin Removal in Pilah.in...');
  const browser = await launchBrowser();
  const page = await browser.newPage();
  await page.setViewport({ width: 390, height: 844 });
  await page.goto(DEFAULT_APP_URL, { waitUntil: 'networkidle0' });

  // 1. Verify Poin is completely absent from the Home screen
  const bodyText = await page.evaluate(() => document.body.innerText);
  if (/(\d+)\s*poin/i.test(bodyText)) {
    throw new Error('FAILED: "Poin" text found on screen! Should be completely removed.');
  }
  console.log('✅ Poin is completely removed from the home screen.');

  // 2. Verify Jejak Card stack exists with initial counter "Tiket 1 dari ..."
  const ticketCounter = await page.evaluate(() => {
    const el = Array.from(document.querySelectorAll('span')).find(s => s.innerText && s.innerText.includes('Tiket 1 dari'));
    return el ? el.innerText : null;
  });
  console.log('Found ticket counter:', ticketCounter);
  if (!ticketCounter || !/Tiket 1 dari \d+/.test(ticketCounter)) {
    throw new Error('FAILED: Initial ticket counter "Tiket 1 dari ..." not found!');
  }
  console.log('✅ Initial Tinder ticket stack correctly shows ticket 1.');

  // 3. Test Navigation: Click "Berikutnya"
  await page.evaluate(() => {
    const btn = document.querySelector('button[aria-label="Tiket Berikutnya"]');
    if (btn) btn.click();
  });
  await new Promise(r => setTimeout(r, 400));

  const secondCounter = await page.evaluate(() => {
    const el = Array.from(document.querySelectorAll('span')).find(s => s.innerText && s.innerText.includes('Tiket 2 dari'));
    return el ? el.innerText : null;
  });
  console.log('After clicking Berikutnya:', secondCounter);
  if (!secondCounter || !/Tiket 2 dari \d+/.test(secondCounter)) {
    throw new Error('FAILED: After clicking next, ticket counter did not advance to "Tiket 2 dari ..."!');
  }
  console.log('✅ Successfully navigated to Ticket 2 via Next button.');

  // 4. Test Navigation: Click "Sebelumnya"
  await page.evaluate(() => {
    const btn = document.querySelector('button[aria-label="Tiket Sebelumnya"]');
    if (btn) btn.click();
  });
  await new Promise(r => setTimeout(r, 400));

  const backCounter = await page.evaluate(() => {
    const el = Array.from(document.querySelectorAll('span')).find(s => s.innerText && s.innerText.includes('Tiket 1 dari'));
    return el ? el.innerText : null;
  });
  if (!backCounter || !/Tiket 1 dari \d+/.test(backCounter)) {
    throw new Error('FAILED: After clicking previous, ticket counter did not return to "Tiket 1 dari ..."!');
  }
  console.log('✅ Successfully navigated back to Ticket 1 via Prev button.');

  // 5. Test Mouse Drag / Swipe gesture (Drag card right by 80px)
  const cardHandle = await page.$('.cursor-grab');
  if (!cardHandle) {
    throw new Error('FAILED: Swipeable card handle (.cursor-grab) not found!');
  }
  // Scroll card cleanly into view
  await cardHandle.scrollIntoView();
  await new Promise(r => setTimeout(r, 200));

  const boundingBox = await cardHandle.boundingBox();
  const startX = boundingBox.x + boundingBox.width / 2;
  const startY = boundingBox.y + 60; // Top portion of card, away from bottom navbar

  await page.mouse.move(startX, startY);
  await page.mouse.down();
  for (let i = 1; i <= 6; i++) {
    await page.mouse.move(startX + i * 20, startY, { steps: 2 });
    await new Promise(r => setTimeout(r, 25));
  }
  await page.mouse.up();
  await new Promise(r => setTimeout(r, 500));

  const swipedCounter = await page.evaluate(() => {
    const el = Array.from(document.querySelectorAll('span')).find(s => s.innerText && s.innerText.includes('Tiket 2 dari'));
    return el ? el.innerText : null;
  });
  console.log('After Tinder swipe drag:', swipedCounter);
  if (!swipedCounter || !/Tiket 2 dari \d+/.test(swipedCounter)) {
    throw new Error('FAILED: Drag gesture did not trigger ticket advance!');
  }
  console.log('✅ Tinder swipe drag gesture (Right) successfully advanced to Ticket 2!');

  // 6. Test Mouse Drag / Swipe gesture (Drag card left by 120px to return to Ticket 1)
  const cardHandle2 = await page.$('.cursor-grab');
  const box2 = await cardHandle2.boundingBox();
  const startX2 = box2.x + box2.width / 2;
  const startY2 = box2.y + 60;

  await page.mouse.move(startX2, startY2);
  await page.mouse.down();
  for (let i = 1; i <= 6; i++) {
    await page.mouse.move(startX2 - i * 20, startY2, { steps: 2 });
    await new Promise(r => setTimeout(r, 25));
  }
  await page.mouse.up();
  await new Promise(r => setTimeout(r, 500));

  const swipedBackCounter = await page.evaluate(() => {
    const el = Array.from(document.querySelectorAll('span')).find(s => s.innerText && s.innerText.includes('Tiket 1 dari'));
    return el ? el.innerText : null;
  });
  console.log('After Tinder swipe left drag:', swipedBackCounter);
  if (!swipedBackCounter || !/Tiket 1 dari \d+/.test(swipedBackCounter)) {
    throw new Error('FAILED: Drag left gesture did not return to Ticket 1!');
  }
  console.log('✅ Tinder swipe drag gesture (Left) successfully returned to Ticket 1!');

  await browser.close();
  console.log('🎉 ALL TINDER SWIPE & POIN REMOVAL TESTS PASSED!');
})();
