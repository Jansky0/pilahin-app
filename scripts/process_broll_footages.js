import { spawnSync } from 'child_process';
import fs from 'fs';
import path from 'path';

const RAW_DIR = '/home/jansky/pilahin-app/broll_raw';
const OUT_DIR = '/home/jansky/pilahin-app/public/broll_footages';
const USER_VIDEOS_DIR = '/home/jansky/Videos/broll_latar_belakang';

fs.mkdirSync(OUT_DIR, { recursive: true });
fs.mkdirSync(USER_VIDEOS_DIR, { recursive: true });

console.log('🎬 Processing High-Quality B-Roll Stock Footages for Pitching Video...\n');

// Definition of B-Roll Clips for Problem Statement & Background
const clips = [
  {
    name: '01_krisis_gunungan_sampah_tpa.mp4',
    title: 'Krisis Gunungan Sampah TPA',
    input: path.join(RAW_DIR, 'scavenge_1.webm'),
    start: '00:00:00',
    duration: '00:00:06.5',
    description: 'Hamparan gunungan sampah plastik dan limbah tercampur di tempat pembuangan akhir.'
  },
  {
    name: '02_buang_sampah_sembarangan_lingkungan.mp4',
    title: 'Pencemaran & Pembuangan Sampah Liar',
    input: path.join(RAW_DIR, 'illegal_dumping.webm'),
    start: '00:00:08',
    duration: '00:00:08',
    description: 'Sampah plastik, kardus, dan limbah rumah tangga yang dibuang sembarangan di parit dan pinggir jalan.'
  },
  {
    name: '03_realita_tumpukan_sampah_indonesia.mp4',
    title: 'Realita Pengangkutan Sampah Domestik Indonesia',
    input: path.join(RAW_DIR, 'indonesia_plastic.webm'),
    start: '00:00:00',
    duration: '00:00:08',
    description: 'Truk pengangkut sampah lokal Indonesia dan karung limbah anorganik di pemukiman.'
  },
  {
    name: '04_pemilahan_botol_plastik_pet.mp4',
    title: 'Pemilahan Botol Plastik Daur Ulang',
    input: path.join(RAW_DIR, 'recycling_video.webm'),
    start: '00:00:23',
    duration: '00:00:08',
    description: 'Petugas memilah botol-botol plastik minuman di atas ban berjalan (conveyor belt).'
  },
  {
    name: '05_fasilitas_sortir_daur_ulang.mp4',
    title: 'Proses Sortir Material Daur Ulang',
    input: path.join(RAW_DIR, 'recycling_video.webm'),
    start: '00:00:58',
    duration: '00:00:08',
    description: 'Pekerja dengan rompi keselamatan memilah berbagai fraksi plastik dan karton untuk didaur ulang.'
  }
];

const renderedClips = [];

for (const clip of clips) {
  const outPath = path.join(OUT_DIR, clip.name);
  console.log(`▶ Trimming & Encoding: ${clip.title} -> ${clip.name}`);

  // ffmpeg transcode: 1920x1080 30fps h264 yuv420p
  const args = [
    '-y',
    '-ss', clip.start,
    '-i', clip.input,
    '-t', clip.duration,
    '-vf', 'scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,fps=30',
    '-c:v', 'libx264',
    '-preset', 'fast',
    '-crf', '19',
    '-pix_fmt', 'yuv420p',
    '-an', // remove random raw audio so user can put their clean voiceover & BGM
    outPath
  ];

  const res = spawnSync('/usr/bin/ffmpeg', args);
  if (res.status !== 0) {
    console.error(`Error encoding ${clip.name}:`, res.stderr.toString());
  } else {
    console.log(`  ✓ Saved: ${outPath}`);
    renderedClips.push(outPath);
    // Copy to user Videos folder
    fs.copyFileSync(outPath, path.join(USER_VIDEOS_DIR, clip.name));
  }
}

console.log(`\n🎞️ Assembling Master Stitched B-Roll Sequence with Smooth Crossfades...`);

// Let's create master stitched B-Roll with xfade
// Measured durations: 6.5s, 8s, 8s, 8s, 8s
// Transitions at:
// clip0 ends at 6.5. xfade d=0.5 -> offset = 6.0.
// clip1 ends at 6.0 + 8.0 = 14.0. xfade d=0.5 -> offset = 13.5.
// clip2 ends at 13.5 + 8.0 = 21.5. xfade d=0.5 -> offset = 21.0.
// clip3 ends at 21.0 + 8.0 = 29.0. xfade d=0.5 -> offset = 28.5.
// total duration = 28.5 + 8.0 = 36.5s.

const masterOut = path.join(OUT_DIR, 'broll_latar_belakang_master.mp4');

const filterComplex = [
  `[0:v][1:v]xfade=transition=fade:duration=0.5:offset=6.0[v01]`,
  `[v01][2:v]xfade=transition=fade:duration=0.5:offset=13.5[v02]`,
  `[v02][3:v]xfade=transition=fade:duration=0.5:offset=21.0[v03]`,
  `[v03][4:v]xfade=transition=fade:duration=0.5:offset=28.5[v_out]`
].join(';');

const stitchArgs = [
  '-y',
  '-i', renderedClips[0],
  '-i', renderedClips[1],
  '-i', renderedClips[2],
  '-i', renderedClips[3],
  '-i', renderedClips[4],
  '-filter_complex', filterComplex,
  '-map', '[v_out]',
  '-c:v', 'libx264',
  '-preset', 'fast',
  '-crf', '18',
  '-pix_fmt', 'yuv420p',
  masterOut
];

const stitchRes = spawnSync('/usr/bin/ffmpeg', stitchArgs);
if (stitchRes.status === 0) {
  console.log(`\n🎉 MASTER B-ROLL SHOWCASE CREATED: ${masterOut}`);
  fs.copyFileSync(masterOut, path.join(USER_VIDEOS_DIR, 'broll_latar_belakang_master.mp4'));
} else {
  console.error('Error during master B-Roll stitching:', stitchRes.stderr.toString());
}

console.log('\n✅ All B-Roll clips and master video ready in:');
console.log(` - ${OUT_DIR}`);
console.log(` - ${USER_VIDEOS_DIR}`);
