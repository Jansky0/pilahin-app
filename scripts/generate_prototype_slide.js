import puppeteer from 'puppeteer-core';
import QRCode from 'qrcode';
import fs from 'fs';
import path from 'path';

const CHROME_PATH = '/home/jansky/.local/bin/google-chrome';
const BASE_URL = 'http://localhost:3000';
const PROD_URL = 'https://pilahin-app.vercel.app';
const OUT_DIR = '/home/jansky/pilahin-app/public';

async function generateSlide() {
  console.log('Generating high-res prototype screenshots...');
  const browser = await puppeteer.launch({
    executablePath: CHROME_PATH,
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 430, height: 932, deviceScaleFactor: 2 });

  // 1. Capture Beranda
  await page.goto(BASE_URL, { waitUntil: 'networkidle0' });
  await new Promise(r => setTimeout(r, 1000));
  const berandaBuf = await page.screenshot({ encoding: 'base64' });

  // 2. Capture SnapSort
  await page.evaluate(() => {
    const btns = Array.from(document.querySelectorAll('button'));
    const snapBtn = btns.find(b => b.textContent && b.textContent.includes('SnapSort AI'));
    if (snapBtn) snapBtn.click();
  });
  await new Promise(r => setTimeout(r, 1200));
  const snapBuf = await page.screenshot({ encoding: 'base64' });

  // 3. Generate QR Code with high resolution
  const qrDataUrl = await QRCode.toDataURL(PROD_URL, {
    margin: 1,
    width: 600,
    color: {
      dark: '#0f172a',
      light: '#ffffff'
    }
  });

  // 4. Construct Slide HTML (1920x1080)
  const slideHtml = `
  <!DOCTYPE html>
  <html>
  <head>
    <meta charset="utf-8">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800;900&display=swap" rel="stylesheet">
    <style>
      * { box-sizing: border-box; margin: 0; padding: 0; }
      body {
        width: 1920px;
        height: 1080px;
        font-family: 'Plus Jakarta Sans', sans-serif;
        background: radial-gradient(circle at 50% 20%, #2b1154 0%, #0d061f 65%, #05020c 100%);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        position: relative;
        color: #ffffff;
      }
      
      /* Atmospheric background glow */
      .glow-orb-1 {
        position: absolute;
        top: -150px;
        left: 50%;
        transform: translateX(-50%);
        width: 900px;
        height: 500px;
        background: radial-gradient(circle, rgba(168, 85, 247, 0.45) 0%, rgba(139, 92, 246, 0.1) 60%, transparent 80%);
        filter: blur(80px);
        pointer-events: none;
      }

      .glow-orb-2 {
        position: absolute;
        bottom: -100px;
        left: 50%;
        transform: translateX(-50%);
        width: 1100px;
        height: 400px;
        background: radial-gradient(circle, rgba(147, 51, 234, 0.25) 0%, transparent 70%);
        filter: blur(100px);
        pointer-events: none;
      }

      /* Slide Header */
      .slide-title {
        font-size: 68px;
        font-weight: 900;
        letter-spacing: 4px;
        text-transform: uppercase;
        background: linear-gradient(180deg, #ffffff 0%, #ddd6fe 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 30px rgba(192, 132, 252, 0.6);
        margin-bottom: 24px;
        z-index: 10;
      }

      /* Main Content Card Container */
      .main-card {
        width: 1540px;
        height: 760px;
        background: #f3effe;
        border-radius: 40px;
        box-shadow: 0 0 0 1px rgba(255, 255, 255, 0.4),
                    0 25px 80px -10px rgba(124, 58, 237, 0.45),
                    0 0 60px rgba(168, 85, 247, 0.35);
        display: flex;
        align-items: center;
        padding: 0 70px;
        position: relative;
        z-index: 10;
        gap: 60px;
      }

      /* Left Side: QR Code & CTA */
      .left-col {
        flex: 0 0 520px;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
      }

      .cta-title {
        font-size: 38px;
        font-weight: 800;
        color: #5b21b6;
        line-height: 1.25;
        margin-bottom: 28px;
        letter-spacing: -0.5px;
      }

      .cta-title span {
        display: block;
        color: #7c3aed;
      }

      .qr-wrapper {
        background: #ffffff;
        padding: 24px;
        border-radius: 28px;
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.08), 0 0 0 1px rgba(0, 0, 0, 0.04);
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
      }

      .qr-image {
        width: 320px;
        height: 320px;
        display: block;
        border-radius: 12px;
      }

      /* Center dino/recycle badge on QR */
      .qr-badge {
        position: absolute;
        width: 54px;
        height: 54px;
        background: #10b981;
        border: 4px solid #ffffff;
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
      }

      .qr-badge svg {
        width: 28px;
        height: 28px;
        fill: #ffffff;
      }

      .qr-subtext {
        margin-top: 20px;
        font-size: 15px;
        font-weight: 700;
        color: #64748b;
        letter-spacing: 0.5px;
      }

      .qr-url {
        color: #7c3aed;
        font-weight: 800;
      }

      /* Right Side: 2 Phone Mockups */
      .right-col {
        flex: 1;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 40px;
        height: 100%;
        padding-top: 10px;
      }

      /* iPhone Frame styling */
      .phone-frame {
        width: 350px;
        height: 680px;
        background: #1e1b2e;
        border-radius: 50px;
        padding: 10px;
        box-shadow: 0 20px 45px rgba(15, 23, 42, 0.22),
                    0 0 0 2px #4c1d95,
                    inset 0 0 0 2px rgba(255, 255, 255, 0.2);
        position: relative;
        display: flex;
        flex-direction: column;
        overflow: hidden;
      }

      /* Dynamic Island */
      .dynamic-island {
        position: absolute;
        top: 18px;
        left: 50%;
        transform: translateX(-50%);
        width: 100px;
        height: 24px;
        background: #000000;
        border-radius: 20px;
        z-index: 30;
      }

      .screen-inner {
        width: 100%;
        height: 100%;
        border-radius: 40px;
        overflow: hidden;
        background: #ffffff;
        position: relative;
      }

      .screen-inner img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        object-position: top center;
        display: block;
      }

      /* Slide Footer / Tagline */
      .slide-footer {
        margin-top: 26px;
        font-size: 32px;
        font-weight: 800;
        letter-spacing: -0.5px;
        color: #e9d5ff;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
        z-index: 10;
      }
    </style>
  </head>
  <body>
    <div class="glow-orb-1"></div>
    <div class="glow-orb-2"></div>

    <div class="slide-title">PILAH.IN</div>

    <div class="main-card">
      <div class="left-col">
        <h2 class="cta-title">
          Scan Here to
          <span>See Prototype!</span>
        </h2>

        <div class="qr-wrapper">
          <img class="qr-image" src="${qrDataUrl}" alt="QR Code" />
          <div class="qr-badge">
            <svg viewBox="0 0 24 24">
              <path d="M7 15h10v2H7zm0-4h10v2H7zm0-4h10v2H7zm-3 12a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4z"/>
            </svg>
          </div>
        </div>

        <p class="qr-subtext">Direct Live Web Demo: <span class="qr-url">pilahin-app.vercel.app</span></p>
      </div>

      <div class="right-col">
        <!-- Phone 1: Beranda Warga & Tinder Card -->
        <div class="phone-frame">
          <div class="dynamic-island"></div>
          <div class="screen-inner">
            <img src="data:image/png;base64,${berandaBuf}" alt="Beranda Pilah.in" />
          </div>
        </div>

        <!-- Phone 2: SnapSort AI Scanner -->
        <div class="phone-frame">
          <div class="dynamic-island"></div>
          <div class="screen-inner">
            <img src="data:image/png;base64,${snapBuf}" alt="SnapSort AI Scanner" />
          </div>
        </div>
      </div>
    </div>

    <div class="slide-footer">Pilah.in — Ubah Pilah Sampah Jadi Rupiah Nyata</div>
  </body>
  </html>
  `;

  const slidePage = await browser.newPage();
  await slidePage.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 2 });
  await slidePage.setContent(slideHtml, { waitUntil: 'networkidle0' });
  await new Promise(r => setTimeout(r, 1000));

  const outPath1 = path.join(OUT_DIR, 'slide_prototype_pilahin.png');
  const outPath2 = '/home/jansky/pilahin_prototype_slide.png';
  const outPath3 = '/home/jansky/Pictures/slide_prototype_pilahin.png';

  await slidePage.screenshot({ path: outPath1, type: 'png' });
  fs.copyFileSync(outPath1, outPath2);
  try {
    fs.mkdirSync('/home/jansky/Pictures', { recursive: true });
    fs.copyFileSync(outPath1, outPath3);
  } catch(e) {}

  console.log(`✅ Slide successfully created at:`);
  console.log(` - ${outPath1}`);
  console.log(` - ${outPath2}`);

  await browser.close();
}

generateSlide().catch(err => {
  console.error('Error generating slide:', err);
  process.exit(1);
});
