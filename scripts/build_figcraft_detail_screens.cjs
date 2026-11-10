const fs = require('fs');
const { execSync } = require('child_process');
const path = require('path');

const FIGCRAFT_PATH = '/home/jansky/Pilahin_Mobile_App.figcraft';
const BACKUP_PATH = '/home/jansky/Pilahin_Mobile_App.figcraft.backup';
const JSON_TEMP = '/tmp/pilahin_expanded.json';
const EXPORT_DIR = '/home/jansky/figcraft_screens';

fs.mkdirSync(EXPORT_DIR, { recursive: true });

console.log('🚀 Enhancing Pilahin_Mobile_App.figcraft with Detail & Loading Screens...\n');

// 1. Create backup
fs.copyFileSync(FIGCRAFT_PATH, BACKUP_PATH);
console.log(`✓ Backup created: ${BACKUP_PATH}`);

// 2. Convert to JSON
execSync(`figcraft-cli convert ${FIGCRAFT_PATH} ${JSON_TEMP}`);
const doc = JSON.parse(fs.readFileSync(JSON_TEMP, 'utf8'));

let currentId = doc.next_id || 400;
function nextId() {
  return currentId++;
}

function makeColor(hex, a = 1) {
  const c = hex.replace('#', '');
  return {
    r: parseInt(c.substring(0, 2), 16) / 255,
    g: parseInt(c.substring(2, 4), 16) / 255,
    b: parseInt(c.substring(4, 6), 16) / 255,
    a: a
  };
}

function makeSolidFill(hex, a = 1) {
  return [{
    blend: 'normal',
    color: makeColor(hex, a),
    opacity: 1,
    type: 'solid',
    visible: true
  }];
}

function makeStroke(hex, weight = 1) {
  return {
    strokes: [{
      blend: 'normal',
      color: makeColor(hex),
      opacity: 1,
      type: 'solid',
      visible: true
    }],
    stroke_weight: weight,
    stroke_align: 'inside'
  };
}

function makeCorners(r) {
  return {
    corners: {
      radii: [r, r, r, r],
      smoothing: 0
    }
  };
}

function createTextNode(characters, options = {}) {
  const id = nextId();
  const fontSize = options.fontSize || 12;
  const fontWeight = options.fontWeight || 'Regular';
  const colorHex = options.color || '#FFFFFF';
  const width = options.width || 200;
  const height = options.height || Math.round(fontSize * 1.3);

  const node = {
    id: id,
    name: options.name || characters.substring(0, 30),
    type: 'text',
    characters: characters,
    blend: 'normal',
    width: width,
    height: height,
    fills: makeSolidFill(colorHex),
    style: {
      case: 'original',
      decoration: 'none',
      fills: null,
      font_family: 'Inter',
      font_size: fontSize,
      font_style: fontWeight,
      letter_spacing: { unit: 'percent', value: 0 },
      line_height: { unit: 'auto' },
      link: null
    },
    child_layout: {
      absolute: false,
      grid_column: null,
      grid_column_span: 0,
      grid_row: null,
      grid_row_span: 0,
      max_h: null,
      max_w: null,
      min_h: null,
      min_w: null,
      sizing_h: options.sizing_h || 'hug',
      sizing_v: options.sizing_v || 'hug'
    }
  };

  doc.nodes[String(id)] = node;
  return id;
}

function createFrameNode(name, options = {}) {
  const id = nextId();
  const width = options.width || 390;
  const height = options.height || 844;
  const layoutMode = options.layout || 'vertical';
  const padding = options.padding || [16, 16, 16, 16];
  const gap = options.gap !== undefined ? options.gap : 12;
  const mainAlign = options.mainAlign || 'min';
  let crossAlign = options.crossAlign || 'min';
  if (crossAlign === 'stretch' || !['min', 'center', 'max', 'baseline'].includes(crossAlign)) {
    crossAlign = 'min';
  }
  const bgHex = options.bg || '#0F172A';

  const node = {
    id: id,
    name: name,
    type: 'frame',
    width: width,
    height: height,
    clip: options.clip !== undefined ? options.clip : true,
    children: [],
    transform: [1, 0, 0, 1, options.x || 0, options.y || 0],
    layout: {
      column_tracks: [],
      content_align: 'auto',
      cross_align: crossAlign,
      cross_gap: gap,
      gap: gap,
      grid_columns: 2,
      grid_rows: 2,
      main_align: mainAlign,
      mode: layoutMode,
      padding: padding,
      reverse_z: false,
      row_tracks: [],
      strokes_included: true,
      wrap: false
    },
    child_layout: {
      absolute: options.absolute || false,
      grid_column: null,
      grid_column_span: 0,
      grid_row: null,
      grid_row_span: 0,
      max_h: null,
      max_w: null,
      min_h: null,
      min_w: null,
      sizing_h: options.sizing_h || (options.isTopLevel ? 'fixed' : 'fill'),
      sizing_v: options.sizing_v || (options.isTopLevel ? 'fixed' : 'hug')
    },
    fills: bgHex ? makeSolidFill(bgHex) : [],
    ...makeCorners(options.radius !== undefined ? options.radius : 0)
  };

  if (options.stroke) {
    Object.assign(node, makeStroke(options.stroke, options.strokeWeight || 1));
  }

  doc.nodes[String(id)] = node;
  return id;
}

function addChild(parentId, childId) {
  doc.nodes[String(parentId)].children.push(childId);
  doc.nodes[String(childId)].parent = parentId;
}

// ==========================================
// SCREEN 00: SPLASH SCREEN (Halaman Pembuka)
// ==========================================
console.log('🎨 Building Screen 00: Halaman Pembuka (Splash Screen)...');
const splashFrameId = createFrameNode('00 — Halaman Pembuka (Splash Screen)', {
  isTopLevel: true,
  x: -800,
  y: 80,
  width: 390,
  height: 844,
  bg: '#0B1120',
  radius: 36,
  padding: [80, 24, 48, 24],
  mainAlign: 'spaceBetween',
  crossAlign: 'center',
  gap: 24
});

// Center Content Group
const splashCenterId = createFrameNode('Center Branding', {
  width: 342,
  height: 360,
  layout: 'vertical',
  mainAlign: 'center',
  crossAlign: 'center',
  gap: 20,
  bg: null
});

// Logo Icon Box (Emerald Glow)
const splashLogoBoxId = createFrameNode('Logo Mark Glow', {
  width: 104,
  height: 104,
  radius: 30,
  bg: '#064E3B',
  stroke: '#10B981',
  strokeWeight: 2,
  layout: 'vertical',
  mainAlign: 'center',
  crossAlign: 'center',
  gap: 0,
  padding: [0, 0, 0, 0],
  sizing_h: 'fixed',
  sizing_v: 'fixed'
});
const logoTextId = createTextNode('♻️', { fontSize: 44, fontWeight: 'Bold', width: 50, height: 50 });
addChild(splashLogoBoxId, logoTextId);
addChild(splashCenterId, splashLogoBoxId);

// Text Group
const splashTitleId = createTextNode('Pilah.in', {
  fontSize: 34,
  fontWeight: 'Bold',
  color: '#FFFFFF',
  width: 150,
  height: 42
});
addChild(splashCenterId, splashTitleId);

const splashTaglineId = createTextNode('Ekonomi Sirkular dari Rumah', {
  fontSize: 14,
  fontWeight: 'Medium',
  color: '#94A3B8',
  width: 220,
  height: 20
});
addChild(splashCenterId, splashTaglineId);

// Pill Badge
const splashPillId = createFrameNode('Pill Tag', {
  width: 270,
  height: 34,
  radius: 999,
  bg: '#162820',
  stroke: '#10B981',
  layout: 'horizontal',
  mainAlign: 'center',
  crossAlign: 'center',
  padding: [6, 16, 6, 16],
  sizing_h: 'hug',
  sizing_v: 'hug'
});
const pillTextId = createTextNode('🌱 Pilah Sampah • Jemput Mudah • Saldo Nyata', {
  fontSize: 10,
  fontWeight: 'Semi Bold',
  color: '#34D399',
  width: 250
});
addChild(splashPillId, pillTextId);
addChild(splashCenterId, splashPillId);

addChild(splashFrameId, splashCenterId);

// Bottom Progress & Credits
const splashBottomId = createFrameNode('Bottom Loading Area', {
  width: 342,
  height: 100,
  layout: 'vertical',
  mainAlign: 'center',
  crossAlign: 'center',
  gap: 12,
  bg: null
});

// Progress Bar Track
const progressTrackId = createFrameNode('Progress Track', {
  width: 200,
  height: 6,
  radius: 999,
  bg: '#1E293B',
  layout: 'horizontal',
  mainAlign: 'min',
  crossAlign: 'center',
  padding: [0, 0, 0, 0],
  sizing_h: 'fixed',
  sizing_v: 'fixed'
});
const progressFillId = createFrameNode('Progress Fill', {
  width: 145,
  height: 6,
  radius: 999,
  bg: '#10B981',
  sizing_h: 'fixed',
  sizing_v: 'fixed',
  padding: [0, 0, 0, 0]
});
addChild(progressTrackId, progressFillId);
addChild(splashBottomId, progressTrackId);

const statusTextId = createTextNode('Menghubungkan ke Bank Sampah RW 05...', {
  fontSize: 10.5,
  color: '#64748B',
  width: 260
});
addChild(splashBottomId, statusTextId);

const creditTextId = createTextNode('v1.0.0 • UI/UX In Action MIA 2026', {
  fontSize: 9,
  color: '#475569',
  width: 200
});
addChild(splashBottomId, creditTextId);

addChild(splashFrameId, splashBottomId);

// ==========================================
// SCREEN 00B: ONBOARDING & PENGENALAN ALUR
// ==========================================
console.log('🎨 Building Screen 00B: Pengenalan Alur (Onboarding)...');
const onbFrameId = createFrameNode('00B — Pengenalan Alur (Onboarding)', {
  isTopLevel: true,
  x: -360,
  y: 80,
  width: 390,
  height: 844,
  bg: '#0F172A',
  radius: 36,
  padding: [48, 20, 36, 20],
  mainAlign: 'spaceBetween',
  crossAlign: 'min',
  gap: 16
});

// Top bar
const onbTopBarId = createFrameNode('Top Bar', {
  width: 350,
  height: 28,
  layout: 'horizontal',
  mainAlign: 'spaceBetween',
  crossAlign: 'center',
  bg: null
});
const onbLogoSmallId = createTextNode('Pilah.in', { fontSize: 16, fontWeight: 'Bold', color: '#10B981', width: 70 });
const onbSkipId = createTextNode('Lewati →', { fontSize: 11, fontWeight: 'Medium', color: '#64748B', width: 55 });
addChild(onbTopBarId, onbLogoSmallId);
addChild(onbTopBarId, onbSkipId);
addChild(onbFrameId, onbTopBarId);

// Hero Visual Card
const onbHeroId = createFrameNode('Hero Circular Visual', {
  width: 350,
  height: 210,
  radius: 24,
  bg: '#1E293B',
  stroke: '#334155',
  layout: 'vertical',
  mainAlign: 'center',
  crossAlign: 'center',
  gap: 14,
  padding: [20, 20, 20, 20],
  sizing_h: 'fill',
  sizing_v: 'fixed'
});
const heroIconGroupId = createFrameNode('3 Icons Flow', {
  width: 300,
  height: 54,
  layout: 'horizontal',
  mainAlign: 'center',
  crossAlign: 'center',
  gap: 16,
  bg: null
});
const icon1 = createTextNode('📸 Foto AI', { fontSize: 11, fontWeight: 'Semi Bold', color: '#38BDF8', width: 75 });
const arrow1 = createTextNode('➔', { fontSize: 14, color: '#64748B', width: 18 });
const icon2 = createTextNode('🛵 Jemput', { fontSize: 11, fontWeight: 'Semi Bold', color: '#34D399', width: 75 });
const arrow2 = createTextNode('➔', { fontSize: 14, color: '#64748B', width: 18 });
const icon3 = createTextNode('💵 Saldo', { fontSize: 11, fontWeight: 'Semi Bold', color: '#FBBF24', width: 70 });
addChild(heroIconGroupId, icon1);
addChild(heroIconGroupId, arrow1);
addChild(heroIconGroupId, icon2);
addChild(heroIconGroupId, arrow2);
addChild(heroIconGroupId, icon3);
addChild(onbHeroId, heroIconGroupId);

const heroQuote = createTextNode('"Memilah sampah kini semudah memotret dari dapur, dijemput motor Tossa ke teras rumah."', {
  fontSize: 11,
  fontWeight: 'Medium',
  color: '#94A3B8',
  width: 290
});
addChild(onbHeroId, heroQuote);
addChild(onbFrameId, onbHeroId);

// Headline & Feature Highlights
const onbContentGroupId = createFrameNode('Content Features', {
  width: 350,
  height: 290,
  layout: 'vertical',
  mainAlign: 'min',
  crossAlign: 'min',
  gap: 12,
  bg: null
});

const onbHeading = createTextNode('Ubah Sampah Jadi Saldo Tunai Riil', {
  fontSize: 20,
  fontWeight: 'Bold',
  color: '#FFFFFF',
  width: 330
});
addChild(onbContentGroupId, onbHeading);

const onbSubheading = createTextNode('Tanpa wajib punya timbangan di rumah. Taksir volume visual, kurir timbang langsung di tempat.', {
  fontSize: 11.5,
  color: '#94A3B8',
  width: 340
});
addChild(onbContentGroupId, onbSubheading);

function makeFeatureRow(icon, title, desc) {
  const row = createFrameNode('Feature Row', {
    width: 350,
    height: 52,
    radius: 14,
    bg: '#1E293B',
    layout: 'horizontal',
    mainAlign: 'min',
    crossAlign: 'center',
    gap: 12,
    padding: [8, 12, 8, 12]
  });
  const ic = createTextNode(icon, { fontSize: 18, width: 28, height: 28 });
  const textCol = createFrameNode('Text Col', {
    width: 280,
    height: 38,
    layout: 'vertical',
    gap: 2,
    padding: [0, 0, 0, 0],
    bg: null
  });
  const t = createTextNode(title, { fontSize: 11.5, fontWeight: 'Bold', color: '#F8FAFC', width: 270 });
  const d = createTextNode(desc, { fontSize: 9.5, color: '#94A3B8', width: 270 });
  addChild(textCol, t);
  addChild(textCol, d);
  addChild(row, ic);
  addChild(row, textCol);
  return row;
}

addChild(onbContentGroupId, makeFeatureRow('📸', 'SnapSort AI Detector', 'Deteksi botol, kardus & panduan cuci botol otomatis.'));
addChild(onbContentGroupId, makeFeatureRow('⚖️', 'Zero-Scale Jemput Tossa', 'Panggil dulu, timbang di teras dengan ongkir 10% transparan.'));
addChild(onbContentGroupId, makeFeatureRow('💳', 'Dompet Rupiah Tanpa Koin', 'Saldo cair langsung ke GoPay / DANA 0% biaya admin.'));

addChild(onbFrameId, onbContentGroupId);

// Actions
const onbActionsId = createFrameNode('Actions Group', {
  width: 350,
  height: 100,
  layout: 'vertical',
  gap: 10,
  mainAlign: 'center',
  crossAlign: 'min',
  bg: null
});

const onbPrimaryBtn = createFrameNode('Btn Primary', {
  width: 350,
  height: 48,
  radius: 14,
  bg: '#10B981',
  layout: 'horizontal',
  mainAlign: 'center',
  crossAlign: 'center',
  padding: [12, 20, 12, 20]
});
const btnText1 = createTextNode('Mulai Pilah Sekarang', { fontSize: 13, fontWeight: 'Bold', color: '#091E16', width: 160 });
addChild(onbPrimaryBtn, btnText1);
addChild(onbActionsId, onbPrimaryBtn);

const onbSecText = createTextNode('Sudah punya akun? Masuk dengan WhatsApp', {
  fontSize: 11,
  fontWeight: 'Medium',
  color: '#34D399',
  width: 260
});
addChild(onbActionsId, onbSecText);

addChild(onbFrameId, onbActionsId);

// ==========================================
// SCREEN 06: LOADING SNAPSORT AI SCANNER
// ==========================================
console.log('🎨 Building Screen 06: Loading SnapSort AI (Scanning State)...');
const scanFrameId = createFrameNode('06 — Loading SnapSort AI (Scanning State)', {
  isTopLevel: true,
  x: 80,
  y: 980,
  width: 390,
  height: 844,
  bg: '#0A0F1D',
  radius: 36,
  padding: [44, 20, 36, 20],
  mainAlign: 'spaceBetween',
  crossAlign: 'min',
  gap: 16
});

// Camera Top Bar
const camTopBar = createFrameNode('Camera Top Bar', {
  width: 350,
  height: 36,
  layout: 'horizontal',
  mainAlign: 'spaceBetween',
  crossAlign: 'center',
  bg: null
});
const camClose = createTextNode('✕ Batal', { fontSize: 11, color: '#94A3B8', width: 60 });
const camTitle = createTextNode('SnapSort AI Scanner', { fontSize: 14, fontWeight: 'Bold', color: '#FFFFFF', width: 170 });
const camFlash = createTextNode('⚡ Auto', { fontSize: 11, color: '#FBBF24', width: 55 });
addChild(camTopBar, camClose);
addChild(camTopBar, camTitle);
addChild(camTopBar, camFlash);
addChild(scanFrameId, camTopBar);

// Viewfinder Box (350x340)
const viewfinder = createFrameNode('Camera Viewfinder', {
  width: 350,
  height: 340,
  radius: 24,
  bg: '#111827',
  stroke: '#10B981',
  strokeWeight: 2,
  layout: 'vertical',
  mainAlign: 'spaceBetween',
  crossAlign: 'min',
  padding: [16, 16, 16, 16],
  sizing_h: 'fill',
  sizing_v: 'fixed'
});

// Viewfinder Corners indicator
const vfTopRow = createFrameNode('VF Top Indicators', {
  width: 318,
  height: 24,
  layout: 'horizontal',
  mainAlign: 'spaceBetween',
  crossAlign: 'center',
  bg: null
});
const vfTag = createTextNode('● AI DETECTING ACTIVE', { fontSize: 9.5, fontWeight: 'Bold', color: '#10B981', width: 150 });
const vfFps = createTextNode('30 FPS • HD', { fontSize: 9.5, color: '#64748B', width: 70 });
addChild(vfTopRow, vfTag);
addChild(vfTopRow, vfFps);
addChild(viewfinder, vfTopRow);

// Viewfinder Center Target
const vfTarget = createFrameNode('Center Object Target', {
  width: 318,
  height: 210,
  radius: 16,
  bg: '#162238',
  stroke: '#38BDF8',
  strokeWeight: 1,
  layout: 'vertical',
  mainAlign: 'center',
  crossAlign: 'center',
  gap: 8,
  padding: [12, 12, 12, 12]
});
const bottleIcon = createTextNode('🍾', { fontSize: 44, width: 50, height: 50 });
const laserLine = createFrameNode('Scanning Laser Bar', {
  width: 260,
  height: 3,
  radius: 999,
  bg: '#34D399',
  sizing_h: 'fixed',
  sizing_v: 'fixed',
  padding: [0, 0, 0, 0]
});
const detectPill = createFrameNode('Detect Pill', {
  width: 220,
  height: 26,
  radius: 999,
  bg: '#064E3B',
  stroke: '#10B981',
  layout: 'horizontal',
  mainAlign: 'center',
  crossAlign: 'center',
  padding: [4, 12, 4, 12],
  sizing_h: 'hug',
  sizing_v: 'hug'
});
const detectText = createTextNode('✓ Terdeteksi: Plastik PET Bening (97.4%)', { fontSize: 9.5, fontWeight: 'Bold', color: '#34D399', width: 230 });
addChild(detectPill, detectText);

addChild(vfTarget, bottleIcon);
addChild(vfTarget, laserLine);
addChild(vfTarget, detectPill);
addChild(viewfinder, vfTarget);

const vfBottomRow = createFrameNode('VF Bottom Guidance', {
  width: 318,
  height: 20,
  layout: 'horizontal',
  mainAlign: 'center',
  crossAlign: 'center',
  bg: null
});
const vfTipText = createTextNode('Posisikan botol/kardus di dalam kotak hijau', { fontSize: 9.5, color: '#94A3B8', width: 250 });
addChild(vfBottomRow, vfTipText);
addChild(viewfinder, vfBottomRow);

addChild(scanFrameId, viewfinder);

// AI Status Card
const aiStatusCard = createFrameNode('AI Analysis Card', {
  width: 350,
  height: 180,
  radius: 20,
  bg: '#1E293B',
  stroke: '#334155',
  layout: 'vertical',
  mainAlign: 'min',
  crossAlign: 'min',
  gap: 10,
  padding: [16, 16, 16, 16]
});

const statusRow = createFrameNode('Status Title Row', {
  width: 318,
  height: 22,
  layout: 'horizontal',
  mainAlign: 'spaceBetween',
  crossAlign: 'center',
  bg: null
});
const aiStatusTitle = createTextNode('⚡ Memproses Spesifikasi Sampah...', { fontSize: 12, fontWeight: 'Bold', color: '#34D399', width: 230 });
const aiPct = createTextNode('85%', { fontSize: 12, fontWeight: 'Bold', color: '#10B981', width: 35 });
addChild(statusRow, aiStatusTitle);
addChild(statusRow, aiPct);
addChild(aiStatusCard, statusRow);

// Progress bar
const aiTrack = createFrameNode('AI Progress Track', {
  width: 318,
  height: 6,
  radius: 999,
  bg: '#0F172A',
  layout: 'horizontal',
  padding: [0, 0, 0, 0]
});
const aiFill = createFrameNode('AI Progress Fill', {
  width: 270,
  height: 6,
  radius: 999,
  bg: '#10B981',
  padding: [0, 0, 0, 0]
});
addChild(aiTrack, aiFill);
addChild(aiStatusCard, aiTrack);

// Price & Prep Info
const priceBadgeRow = createFrameNode('Price Estimate Row', {
  width: 318,
  height: 38,
  radius: 12,
  bg: '#0F172A',
  layout: 'horizontal',
  mainAlign: 'spaceBetween',
  crossAlign: 'center',
  padding: [8, 12, 8, 12]
});
const prLabel = createTextNode('Harga Acuan Bank Sampah RW:', { fontSize: 10, color: '#94A3B8', width: 170 });
const prValue = createTextNode('Rp 3.500 / kg', { fontSize: 12, fontWeight: 'Bold', color: '#FBBF24', width: 100 });
addChild(priceBadgeRow, prLabel);
addChild(priceBadgeRow, prValue);
addChild(aiStatusCard, priceBadgeRow);

const decontamTip = createTextNode('💡 Tips Dekontaminasi: Lepaskan tutup botol & keringkan sisa air agar timbangan bersih dan nilai jual maksimal.', {
  fontSize: 9.5,
  color: '#94A3B8',
  width: 318
});
addChild(aiStatusCard, decontamTip);

addChild(scanFrameId, aiStatusCard);

// Bottom Actions
const scanActions = createFrameNode('Camera Action Buttons', {
  width: 350,
  height: 68,
  layout: 'horizontal',
  mainAlign: 'spaceBetween',
  crossAlign: 'center',
  bg: null
});
const btnRetake = createFrameNode('Btn Retake', {
  width: 140,
  height: 46,
  radius: 12,
  bg: '#1E293B',
  stroke: '#475569',
  layout: 'horizontal',
  mainAlign: 'center',
  crossAlign: 'center',
  padding: [10, 16, 10, 16]
});
const retakeTxt = createTextNode('Foto Ulang', { fontSize: 11.5, fontWeight: 'Semi Bold', color: '#CBD5E1', width: 80 });
addChild(btnRetake, retakeTxt);

const btnUse = createFrameNode('Btn Use Photo', {
  width: 195,
  height: 46,
  radius: 12,
  bg: '#10B981',
  layout: 'horizontal',
  mainAlign: 'center',
  crossAlign: 'center',
  padding: [10, 16, 10, 16]
});
const useTxt = createTextNode('Setor Sampah Ini →', { fontSize: 11.5, fontWeight: 'Bold', color: '#042F22', width: 140 });
addChild(btnUse, useTxt);

addChild(scanActions, btnRetake);
addChild(scanActions, btnUse);
addChild(scanFrameId, scanActions);

// ==========================================
// SCREEN 07: LOADING TIKET & ARMADA TOSSA
// ==========================================
console.log('🎨 Building Screen 07: Loading Tiket & Armada Tossa...');
const tossaFrameId = createFrameNode('07 — Loading Tiket & Armada Tossa', {
  isTopLevel: true,
  x: 520,
  y: 980,
  width: 390,
  height: 844,
  bg: '#0F172A',
  radius: 36,
  padding: [50, 20, 36, 20],
  mainAlign: 'spaceBetween',
  crossAlign: 'min',
  gap: 16
});

const tossaHeader = createFrameNode('Header Group', {
  width: 350,
  height: 64,
  layout: 'vertical',
  gap: 4,
  bg: null
});
const tTitle = createTextNode('Mengonfirmasi Penjemputan', { fontSize: 19, fontWeight: 'Bold', color: '#FFFFFF', width: 330 });
const tSub = createTextNode('Sistem sedang mengalokasikan armada motor Tossa RW 05 terdekat...', { fontSize: 11, color: '#94A3B8', width: 340 });
addChild(tossaHeader, tTitle);
addChild(tossaHeader, tSub);
addChild(tossaFrameId, tossaHeader);

// Radar Card
const radarCard = createFrameNode('Radar Dispatch Card', {
  width: 350,
  height: 220,
  radius: 24,
  bg: '#1E293B',
  stroke: '#334155',
  layout: 'vertical',
  mainAlign: 'center',
  crossAlign: 'center',
  gap: 14,
  padding: [20, 20, 20, 20]
});
const radarCircle = createFrameNode('Radar Circle', {
  width: 80,
  height: 80,
  radius: 40,
  bg: '#064E3B',
  stroke: '#10B981',
  strokeWeight: 2,
  layout: 'vertical',
  mainAlign: 'center',
  crossAlign: 'center',
  gap: 0,
  padding: [0, 0, 0, 0],
  sizing_h: 'fixed',
  sizing_v: 'fixed'
});
const tossaIcon = createTextNode('🛵', { fontSize: 34, width: 40, height: 40 });
addChild(radarCircle, tossaIcon);
addChild(radarCard, radarCircle);

const radarStatusPill = createFrameNode('Radar Pill', {
  width: 280,
  height: 28,
  radius: 999,
  bg: '#0F172A',
  stroke: '#10B981',
  layout: 'horizontal',
  mainAlign: 'center',
  crossAlign: 'center',
  padding: [4, 12, 4, 12]
});
const radarText = createTextNode('🟢 Mencari Kurir RW (Radius 1.2 km)', { fontSize: 10, fontWeight: 'Bold', color: '#34D399', width: 230 });
addChild(radarStatusPill, radarText);
addChild(radarCard, radarStatusPill);
addChild(tossaFrameId, radarCard);

// Ticket Skeleton / Preview Card
const ticketCard = createFrameNode('Ticket Preview Card', {
  width: 350,
  height: 240,
  radius: 20,
  bg: '#1A2333',
  stroke: '#38BDF8',
  strokeWeight: 1,
  layout: 'vertical',
  mainAlign: 'min',
  crossAlign: 'min',
  gap: 12,
  padding: [16, 16, 16, 16]
});

const tRow1 = createFrameNode('Row 1', {
  width: 318,
  height: 24,
  layout: 'horizontal',
  mainAlign: 'spaceBetween',
  crossAlign: 'center',
  bg: null
});
const tCodeTitle = createTextNode('NOMOR TIKET SEMENTARA', { fontSize: 9.5, fontWeight: 'Bold', color: '#38BDF8', width: 170 });
const tStatus = createTextNode('DIJADWALKAN', { fontSize: 9.5, fontWeight: 'Bold', color: '#FBBF24', width: 95 });
addChild(tRow1, tCodeTitle);
addChild(tRow1, tStatus);
addChild(ticketCard, tRow1);

const tCodeText = createTextNode('PLH-•••••• (Auto Generated)', { fontSize: 16, fontWeight: 'Bold', color: '#FFFFFF', width: 250 });
addChild(ticketCard, tCodeText);

function makeDetailRow(label, value) {
  const row = createFrameNode('Detail Row', {
    width: 318,
    height: 22,
    layout: 'horizontal',
    mainAlign: 'spaceBetween',
    crossAlign: 'center',
    bg: null
  });
  const l = createTextNode(label, { fontSize: 10.5, color: '#94A3B8', width: 150 });
  const v = createTextNode(value, { fontSize: 10.5, fontWeight: 'Semi Bold', color: '#F8FAFC', width: 160 });
  addChild(row, l);
  addChild(row, v);
  return row;
}

addChild(ticketCard, makeDetailRow('Jadwal Penjemputan', 'Hari Ini, 14:00 - 16:00 WIB'));
addChild(ticketCard, makeDetailRow('Taksiran Volume', '± 2 Kantong Sedang'));
addChild(ticketCard, makeDetailRow('Ongkir Armada Tossa', '10% (Transparan)'));
addChild(ticketCard, makeDetailRow('Metode Timbang', 'Timbang di Teras Rumah'));

addChild(tossaFrameId, ticketCard);

// Bottom Warning
const tWarning = createFrameNode('Warning Note', {
  width: 350,
  height: 48,
  radius: 12,
  bg: '#14202E',
  layout: 'horizontal',
  mainAlign: 'center',
  crossAlign: 'center',
  padding: [8, 12, 8, 12]
});
const wText = createTextNode('💡 Kurir akan membawa timbangan digital resmi. Saldo akan otomatis bertambah saat penimbangan diverifikasi.', {
  fontSize: 9.5,
  color: '#94A3B8',
  width: 320
});
addChild(tWarning, wText);
addChild(tossaFrameId, tWarning);

// ==========================================
// SCREEN 08: DIALOG SUKSES & SALDO MASUK
// ==========================================
console.log('🎨 Building Screen 08: Dialog Sukses Setor & Saldo Masuk...');
const successFrameId = createFrameNode('08 — Dialog Sukses Setor & Saldo Masuk', {
  isTopLevel: true,
  x: 960,
  y: 980,
  width: 390,
  height: 844,
  bg: '#0B0F19',
  radius: 36,
  padding: [40, 20, 36, 20],
  mainAlign: 'center',
  crossAlign: 'center',
  gap: 16
});

// Modal Card
const modalSheet = createFrameNode('Success Modal Sheet', {
  width: 350,
  height: 640,
  radius: 28,
  bg: '#1E293B',
  stroke: '#10B981',
  strokeWeight: 1.5,
  layout: 'vertical',
  mainAlign: 'spaceBetween',
  crossAlign: 'center',
  gap: 16,
  padding: [24, 20, 24, 20],
  sizing_h: 'fill',
  sizing_v: 'hug'
});

// Success Icon Badge
const checkCircle = createFrameNode('Checkmark Circle', {
  width: 72,
  height: 72,
  radius: 36,
  bg: '#064E3B',
  stroke: '#10B981',
  strokeWeight: 2,
  layout: 'vertical',
  mainAlign: 'center',
  crossAlign: 'center',
  gap: 0,
  padding: [0, 0, 0, 0],
  sizing_h: 'fixed',
  sizing_v: 'fixed'
});
const checkIcon = createTextNode('✓', { fontSize: 36, fontWeight: 'Bold', color: '#10B981', width: 36, height: 36 });
addChild(checkCircle, checkIcon);
addChild(modalSheet, checkCircle);

// Title & Ticket
const modalTitle = createTextNode('Setoran Berhasil Diterima!', {
  fontSize: 19,
  fontWeight: 'Bold',
  color: '#FFFFFF',
  width: 280
});
addChild(modalSheet, modalTitle);

const modalTicketPill = createFrameNode('Ticket Completed Pill', {
  width: 240,
  height: 28,
  radius: 8,
  bg: '#0F172A',
  layout: 'horizontal',
  mainAlign: 'center',
  crossAlign: 'center',
  padding: [4, 12, 4, 12]
});
const tCompText = createTextNode('TIKET SELESAI: PLH-829103', { fontSize: 10, fontWeight: 'Bold', color: '#38BDF8', width: 190 });
addChild(modalTicketPill, tCompText);
addChild(modalSheet, modalTicketPill);

// Breakdown Box
const breakdownBox = createFrameNode('Breakdown Box', {
  width: 310,
  height: 180,
  radius: 16,
  bg: '#131D2D',
  layout: 'vertical',
  mainAlign: 'min',
  crossAlign: 'min',
  gap: 8,
  padding: [14, 14, 14, 14]
});

addChild(breakdownBox, makeDetailRow('Timbangan Riil Mitra', '14.5 kg (Kardus & PET)'));
addChild(breakdownBox, makeDetailRow('Nilai Kotor Sampah', 'Rp 38.500'));
addChild(breakdownBox, makeDetailRow('Potongan Ongkir (10%)', '-Rp 3.850'));

// Divider line
const bDivider = createFrameNode('Divider', {
  width: 282,
  height: 1,
  bg: '#334155',
  padding: [0, 0, 0, 0],
  sizing_h: 'fill',
  sizing_v: 'fixed'
});
addChild(breakdownBox, bDivider);

// Saldo Bersih Row
const netRow = createFrameNode('Net Row', {
  width: 282,
  height: 30,
  layout: 'horizontal',
  mainAlign: 'spaceBetween',
  crossAlign: 'center',
  bg: null
});
const netLabel = createTextNode('Saldo Bersih Masuk:', { fontSize: 11.5, fontWeight: 'Bold', color: '#FFFFFF', width: 140 });
const netVal = createTextNode('Rp 34.650', { fontSize: 15, fontWeight: 'Bold', color: '#34D399', width: 110 });
addChild(netRow, netLabel);
addChild(netRow, netVal);
addChild(breakdownBox, netRow);

addChild(modalSheet, breakdownBox);

// Circular Store Benefit Callout
const storeCallout = createFrameNode('Store Callout', {
  width: 310,
  height: 60,
  radius: 14,
  bg: '#064E3B',
  stroke: '#10B981',
  layout: 'horizontal',
  mainAlign: 'center',
  crossAlign: 'center',
  gap: 8,
  padding: [10, 12, 10, 12]
});
const calloutText = createTextNode('🛍️ Belanja Kompos Sirkular: Saldo ini dapat langsung dibelanjakan pupuk organik olahan TPS3R dengan diskon 15%!', {
  fontSize: 9.5,
  color: '#A7F3D0',
  width: 280
});
addChild(storeCallout, calloutText);
addChild(modalSheet, storeCallout);

// Action buttons
const modalActions = createFrameNode('Modal Actions', {
  width: 310,
  height: 96,
  layout: 'vertical',
  gap: 8,
  mainAlign: 'center',
  crossAlign: 'min',
  bg: null
});

const btnGoWallet = createFrameNode('Btn Go Wallet', {
  width: 310,
  height: 44,
  radius: 12,
  bg: '#10B981',
  layout: 'horizontal',
  mainAlign: 'center',
  crossAlign: 'center',
  padding: [10, 16, 10, 16]
});
const walletTxt = createTextNode('Lihat Dompet & Tarik Saldo', { fontSize: 12, fontWeight: 'Bold', color: '#042F22', width: 190 });
addChild(btnGoWallet, walletTxt);
addChild(modalActions, btnGoWallet);

const btnHome = createTextNode('Kembali ke Beranda', { fontSize: 11, fontWeight: 'Medium', color: '#94A3B8', width: 130 });
addChild(modalActions, btnHome);

addChild(modalSheet, modalActions);
addChild(successFrameId, modalSheet);

// ==========================================
// 4. ADD NEW FRAMES TO PAGE 1
// ==========================================
console.log('📌 Linking all new frames to Page 1 of the Document...');
const page1 = doc.nodes['1'];

// Add new frames in logical chronological order
const newTopLevelIds = [
  splashFrameId,
  onbFrameId,
  scanFrameId,
  tossaFrameId,
  successFrameId
];

newTopLevelIds.forEach(id => {
  page1.children.push(id);
  doc.nodes[String(id)].parent = 1;
});

// Update next_id
doc.next_id = currentId + 10;

// Save updated JSON
fs.writeFileSync(JSON_TEMP, JSON.stringify(doc, null, 2), 'utf8');

// Convert JSON back to .figcraft
console.log('💾 Converting JSON back into FigCraft format...');
execSync(`figcraft-cli convert ${JSON_TEMP} ${FIGCRAFT_PATH}`);

// Verify with info
console.log('\n🔍 Verifying resulting FigCraft document:');
const infoOutput = execSync(`figcraft-cli info ${FIGCRAFT_PATH}`).toString();
console.log(infoOutput);

// Render full canvas preview
console.log('🖼️ Rendering full canvas preview image...');
const previewPath = '/home/jansky/Pilahin_Canvas_Full.png';
execSync(`figcraft-cli render --out ${previewPath} ${FIGCRAFT_PATH}`);
console.log(`✓ Full Canvas Render saved to: ${previewPath}`);

// Export individual new screens as PNG
console.log('📸 Exporting new individual screens to /home/jansky/figcraft_screens/ ...');
execSync(`figcraft-cli export --out ${EXPORT_DIR} ${FIGCRAFT_PATH}`);

console.log('\n🎉 ALL DETAIL & LOADING SCREENS CREATED SUCCESSFULLY IN FIGCRAFT!');
