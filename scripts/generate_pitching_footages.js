import puppeteer from 'puppeteer-core';
import { spawn, spawnSync, execSync } from 'child_process';
import fs from 'fs';
import path from 'path';

const CHROME_PATH = '/home/jansky/.local/bin/google-chrome';
const BASE_URL = 'http://localhost:3000';
const OUTPUT_DIR = '/home/jansky/pilahin-app/pitching_footages';
const PUBLIC_DIR = '/home/jansky/pilahin-app/public/pitching_footages';

const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

async function createRecorder(page, outputPath, fps = 30) {
  const client = await page.target().createCDPSession();
  const ffmpeg = spawn('/usr/bin/ffmpeg', [
    '-y',
    '-f', 'image2pipe',
    '-vcodec', 'mjpeg',
    '-r', String(fps),
    '-i', '-',
    '-c:v', 'libx264',
    '-preset', 'fast',
    '-crf', '18',
    '-pix_fmt', 'yuv420p',
    '-r', String(fps),
    outputPath
  ]);

  let isRecording = true;

  client.on('Page.screencastFrame', async ({ data, sessionId }) => {
    if (!isRecording) return;
    try {
      ffmpeg.stdin.write(Buffer.from(data, 'base64'));
      await client.send('Page.screencastFrameAck', { sessionId });
    } catch (e) {}
  });

  await client.send('Page.startScreencast', {
    format: 'jpeg',
    quality: 95,
    maxWidth: 860,
    maxHeight: 1864,
    everyNthFrame: 1
  });

  return {
    async stop() {
      isRecording = false;
      try {
        await client.send('Page.stopScreencast');
      } catch (e) {}
      ffmpeg.stdin.end();
      await new Promise((r) => ffmpeg.on('close', r));
      console.log(`Saved clip: ${outputPath}`);
    }
  };
}

async function runSmoothScroll(page, targetY, duration = 800) {
  await page.evaluate(async (y, dur) => {
    const startY = window.scrollY;
    const diff = y - startY;
    const startTime = performance.now();

    return new Promise((resolve) => {
      function step(now) {
        const elapsed = now - startTime;
        const progress = Math.min(elapsed / dur, 1);
        const ease = progress < 0.5
          ? 2 * progress * progress
          : -1 + (4 - 2 * progress) * progress;
        window.scrollTo(0, startY + diff * ease);
        if (progress < 1) {
          requestAnimationFrame(step);
        } else {
          resolve();
        }
      }
      requestAnimationFrame(step);
    });
  }, targetY, duration);
  await delay(200);
}

async function clickByText(page, text, selector = 'button, div, span, a') {
  return await page.evaluate((t, sel) => {
    const elements = Array.from(document.querySelectorAll(sel));
    const target = elements.find(el => el.innerText && el.innerText.trim().includes(t));
    if (target) {
      target.click();
      return true;
    }
    return false;
  }, text, selector);
}

async function recordAll() {
  fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  fs.mkdirSync(PUBLIC_DIR, { recursive: true });

  console.log('🚀 Starting Pilah.in Automated High-Fidelity Video Recorder...');

  const browser = await puppeteer.launch({
    executablePath: CHROME_PATH,
    headless: 'new',
    args: [
      '--no-sandbox',
      '--disable-gpu',
      '--window-size=430,932',
      '--disable-dev-shm-usage'
    ]
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 430, height: 932, deviceScaleFactor: 2 });

  // =========================================================================
  // FOOTAGE 1: Beranda Warga & Interaksi Tiket Tinder Stack (Durasi: ~12 detik)
  // =========================================================================
  console.log('\n▶ Recording Footage 1: Beranda Warga & Tinder Ticket Stack...');
  await page.goto(BASE_URL, { waitUntil: 'networkidle0' });
  await delay(800);

  const clip1Path = path.join(OUTPUT_DIR, '01_beranda_dan_tiket.mp4');
  let recorder = await createRecorder(page, clip1Path);

  await delay(1500); // Tampilkan Hero Balance Card & Header
  await runSmoothScroll(page, 320, 1000); // Scroll lembut ke area tiket aktif
  await delay(1000);

  // Klik tombol Berikutnya pada tumpukan tiket
  await clickByText(page, 'Berikutnya');
  await delay(1800); // Tiket 2 (Minyak Jelantah)

  // Klik tombol Berikutnya lagi menuju Tiket 3 (Sad Path: Kurasi Ditolak)
  await clickByText(page, 'Berikutnya');
  await delay(2500); // Tiket 3 (Banner merah Ditolak & edukasi)

  // Scroll kembali ke atas
  await runSmoothScroll(page, 0, 800);
  await delay(1000);

  await recorder.stop();

  // =========================================================================
  // FOOTAGE 2: SnapSort AI Scanner (Computer Vision) (Durasi: ~12 detik)
  // =========================================================================
  console.log('\n▶ Recording Footage 2: SnapSort AI Scanner...');
  const clip2Path = path.join(OUTPUT_DIR, '02_snapsort_ai_scanner.mp4');
  recorder = await createRecorder(page, clip2Path);

  // Pindah ke tab SnapSort AI
  await page.evaluate(() => {
    const aiBtn = Array.from(document.querySelectorAll('button, nav button')).find(b => 
      b.innerText && (b.innerText.includes('Snap') || b.innerText.includes('AI'))
    );
    if (aiBtn) aiBtn.click();
  });
  await delay(1500); // Tampilkan viewfinder kamera AI

  // Klik sampel botol PET (Lolos Kurasi)
  await clickByText(page, 'Botol PET');
  await delay(2000); // Deteksi AI: PET 96%, Rp 3.500/kg

  // Klik sampel Baterai (B3) -> SAD PATH SISTEM MENOLAK
  await clickByText(page, 'Baterai (B3)');
  await delay(2500); // Tampilkan banner merah MATERIAL DITOLAK (LIMBAH B3)

  // Klik kembali Botol PET dan klik "Langsung Setor"
  await clickByText(page, 'Botol PET');
  await delay(1000);
  await clickByText(page, 'Langsung Setor');
  await delay(1500);

  await recorder.stop();

  // =========================================================================
  // FOOTAGE 3: Zero-Scale Barrier & Setor Sampah Tossa (Durasi: ~14 detik)
  // =========================================================================
  console.log('\n▶ Recording Footage 3: Setor Sampah & Zero-Scale Barrier...');
  const clip3Path = path.join(OUTPUT_DIR, '03_setor_sampah_tossa.mp4');
  recorder = await createRecorder(page, clip3Path);

  // Tambahkan pilihan Kardus Box
  await clickByText(page, 'Kardus Box');
  await delay(1200);

  // Naikkan berat pada stepper kg
  await page.evaluate(() => {
    const plusBtns = Array.from(document.querySelectorAll('button')).filter(b => b.innerText.trim() === '+');
    if (plusBtns.length > 0) {
      plusBtns[0].click();
      setTimeout(() => plusBtns[0].click(), 300);
    }
  });
  await delay(1500); // Animasi live calculation

  await runSmoothScroll(page, 280, 800);

  // Buka pilihan alamat dan pilih Depok (Luar Radius) -> SAD PATH
  await page.evaluate(() => {
    const addrBtns = Array.from(document.querySelectorAll('button')).filter(b => 
      b.innerText && b.innerText.includes('Tebet')
    );
    if (addrBtns.length > 0) addrBtns[0].click();
  });
  await delay(1000);

  await clickByText(page, 'Depok');
  await delay(2200); // Tampilkan banner merah SISTEM MENOLAK (DI LUAR RADIUS)

  // Kembalikan ke alamat Tebet (RW 05)
  await page.evaluate(() => {
    const addrBtns = Array.from(document.querySelectorAll('button')).filter(b => 
      b.innerText && b.innerText.includes('Depok')
    );
    if (addrBtns.length > 0) addrBtns[0].click();
  });
  await delay(800);
  await clickByText(page, 'Rumah Utama');
  await delay(1200);

  // Klik Ajukan Penjemputan Tossa
  await clickByText(page, 'Ajukan Penjemputan Tossa');
  await delay(2200); // Tiket QR PLH terbit

  // Tutup modal tiket
  await page.evaluate(() => {
    const closeBtns = Array.from(document.querySelectorAll('button')).filter(b => 
      b.innerText && (b.innerText.includes('Tutup') || b.innerText.includes('Kembali'))
    );
    if (closeBtns.length > 0) closeBtns[0].click();
  });
  await delay(800);

  await recorder.stop();

  // =========================================================================
  // FOOTAGE 4: Portal Mitra Pengelola & Kurasi Timbangan (Durasi: ~13 detik)
  // =========================================================================
  console.log('\n▶ Recording Footage 4: Portal Mitra Pengelola...');
  const clip4Path = path.join(OUTPUT_DIR, '04_portal_mitra_timbangan.mp4');
  recorder = await createRecorder(page, clip4Path);

  // Buka Profile Modal
  await page.evaluate(() => {
    const profileBtn = Array.from(document.querySelectorAll('header button')).find(b => 
      b.innerText && b.innerText.trim() === 'RP'
    );
    if (profileBtn) profileBtn.click();
  });
  await delay(1000);

  // Klik Masuk ke Portal Mitra Pengelola
  await clickByText(page, 'Portal Mitra Pengelola');
  await delay(1800); // Portal Mitra terbuka dengan tema oranye/amber

  // Input berat timbangan 15 kg
  await page.evaluate(() => {
    const numInput = document.querySelector('input[type="number"]');
    if (numInput) {
      numInput.value = '15';
      numInput.dispatchEvent(new Event('input', { bubbles: true }));
    }
  });
  await delay(1000);

  // Klik Konfirmasi Timbangan
  await clickByText(page, 'Konfirmasi Timbangan');
  await delay(2000); // Toast hijau: saldo dikreditkan

  // Klik Tolak Sampah (Kurasi Gagal)
  await clickByText(page, 'Tolak Sampah');
  await delay(1600); // Modal penolakan kurasi terbuka

  // Konfirmasi penolakan
  await clickByText(page, 'Konfirmasi Penolakan Tiket');
  await delay(2000); // Status ditolak tersimpan

  // Kembali ke akun warga
  await page.evaluate(() => {
    const backBtn = Array.from(document.querySelectorAll('button')).find(b => 
      b.innerText && b.innerText.includes('Kembali ke Akun Warga')
    );
    if (backBtn) backBtn.click();
  });
  await delay(1200);

  await recorder.stop();

  // =========================================================================
  // FOOTAGE 5: Toko Sirkular & Tarik Tunai E-Wallet (Durasi: ~14 detik)
  // =========================================================================
  console.log('\n▶ Recording Footage 5: Toko Sirkular & Tarik Tunai Dompet...');
  // Pastikan sesi berada di Beranda Warga
  await page.goto(BASE_URL, { waitUntil: 'networkidle0' });
  await delay(800);

  const clip5Path = path.join(OUTPUT_DIR, '05_toko_sirkular_dan_dompet.mp4');
  recorder = await createRecorder(page, clip5Path);

  // Pindah ke tab Toko Sirkular
  await page.evaluate(() => {
    const tokoBtn = Array.from(document.querySelectorAll('nav button')).find(b => 
      b.innerText && b.innerText.includes('Toko')
    );
    if (tokoBtn) tokoBtn.click();
  });
  await delay(1500); // Katalog produk kompos tampil

  // Klik tombol 'Tukar' pada Pupuk Kompos (Rp 18.000)
  await page.evaluate(() => {
    const buyBtns = Array.from(document.querySelectorAll('button')).filter(b => 
      b.innerText && b.innerText.trim() === 'Tukar'
    );
    if (buyBtns.length > 0) buyBtns[0].click();
  });
  await delay(1500); // Modal konfirmasi pupuk terbuka

  // Klik 'Konfirmasi Tukar Pakai Saldo Sampah'
  await clickByText(page, 'Konfirmasi Tukar Pakai Saldo');
  await delay(2200); // Toast sukses tukar kompos

  // Pindah ke tab Dompet
  await page.evaluate(() => {
    const dompetBtn = Array.from(document.querySelectorAll('nav button')).find(b => 
      b.innerText && b.innerText.includes('Dompet')
    );
    if (dompetBtn) dompetBtn.click();
  });
  await delay(1500); // Halaman Dompet tampil

  // Pilih preset chip Rp 50.000
  await page.evaluate(() => {
    const chip50k = Array.from(document.querySelectorAll('button')).find(b => 
      b.innerText && b.innerText.includes('50.000')
    );
    if (chip50k) chip50k.click();
  });
  await delay(1000);

  // Klik tombol Cairkan Sekarang
  await clickByText(page, 'Cairkan Sekarang ke GoPay');
  await delay(2500); // Toast hijau: Pencairan Rp 50.000 ke GoPay berhasil & saldo terpotong

  await recorder.stop();
  await browser.close();

  console.log('\n✅ All 5 raw clips recorded successfully with solid durations!');

  // =========================================================================
  // STITCHING CLIPS WITH SMOOTH XFADE TRANSITIONS USING FFMPEG
  // =========================================================================
  console.log('\n🎞️ Stitching footages with smooth transitions (xfade fade)...');

  const masterOutputPath = path.join(OUTPUT_DIR, 'pilahin_pitching_master_showcase.mp4');

  function getDuration(filePath) {
    const out = execSync(`/usr/bin/ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "${filePath}"`);
    return parseFloat(out.toString().trim());
  }

  const d1 = getDuration(clip1Path);
  const d2 = getDuration(clip2Path);
  const d3 = getDuration(clip3Path);
  const d4 = getDuration(clip4Path);
  const d5 = getDuration(clip5Path);

  console.log(`Measured Clip Durations:
  [1] Beranda & Tiket:     ${d1.toFixed(2)}s
  [2] SnapSort AI:          ${d2.toFixed(2)}s
  [3] Setor Sampah Tossa:   ${d3.toFixed(2)}s
  [4] Portal Mitra Timbang: ${d4.toFixed(2)}s
  [5] Toko & Dompet Tunai:  ${d5.toFixed(2)}s`);

  const transDuration = 0.5; // 0.5s smooth crossfade
  const offset1 = d1 - transDuration;
  const offset2 = offset1 + d2 - transDuration;
  const offset3 = offset2 + d3 - transDuration;
  const offset4 = offset3 + d4 - transDuration;

  const filterComplex = [
    `[0:v][1:v]xfade=transition=fade:duration=${transDuration}:offset=${offset1.toFixed(2)}[v01]`,
    `[v01][2:v]xfade=transition=fade:duration=${transDuration}:offset=${offset2.toFixed(2)}[v02]`,
    `[v02][3:v]xfade=transition=fade:duration=${transDuration}:offset=${offset3.toFixed(2)}[v03]`,
    `[v03][4:v]xfade=transition=fade:duration=${transDuration}:offset=${offset4.toFixed(2)}[v]`
  ].join(';');

  const ffmpegArgs = [
    '-y',
    '-i', clip1Path,
    '-i', clip2Path,
    '-i', clip3Path,
    '-i', clip4Path,
    '-i', clip5Path,
    '-filter_complex', filterComplex,
    '-map', '[v]',
    '-c:v', 'libx264',
    '-preset', 'medium',
    '-crf', '19',
    '-pix_fmt', 'yuv420p',
    masterOutputPath
  ];

  console.log('Running ffmpeg xfade synthesis...');
  const res = spawnSync('/usr/bin/ffmpeg', ffmpegArgs, { stdio: 'inherit' });
  if (res.error || res.status !== 0) {
    throw new Error(`FFmpeg stitching failed with status ${res.status}`);
  }

  console.log(`\n🎉 MASTER SHOWCASE CREATED: ${masterOutputPath}`);

  // Copy files to public directory and user's Videos folder
  fs.copyFileSync(masterOutputPath, path.join(PUBLIC_DIR, 'pilahin_pitching_master_showcase.mp4'));
  [clip1Path, clip2Path, clip3Path, clip4Path, clip5Path].forEach((file) => {
    fs.copyFileSync(file, path.join(PUBLIC_DIR, path.basename(file)));
  });

  const userVideoDir = '/home/jansky/Videos';
  if (fs.existsSync(userVideoDir)) {
    fs.copyFileSync(masterOutputPath, path.join(userVideoDir, 'pilahin_pitching_master_showcase.mp4'));
  }

  console.log('✅ All video files copied to public web folder & user directory!');
}

recordAll().catch(err => {
  console.error('Fatal error during footage recording:', err);
  process.exit(1);
});
