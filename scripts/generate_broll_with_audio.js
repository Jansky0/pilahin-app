import { spawnSync } from 'child_process';
import fs from 'fs';
import path from 'path';

const RAW_DIR = '/home/jansky/pilahin-app/broll_raw';
const OUT_DIR = '/home/jansky/pilahin-app/public/broll_footages';
const USER_VIDEOS_DIR = '/home/jansky/Videos/broll_latar_belakang';

fs.mkdirSync(OUT_DIR, { recursive: true });
fs.mkdirSync(USER_VIDEOS_DIR, { recursive: true });

console.log('🎬 Processing High-Quality B-Roll Stock Footages with Citizen Transactions...\n');

const clipsConfig = [
  {
    name: '01_krisis_gunungan_sampah_tpa.mp4',
    title: 'Krisis Gunungan Sampah TPA',
    input: path.join(RAW_DIR, 'scavenge_1.webm'),
    start: '00:00:00',
    duration: '00:00:07.0',
    description: 'Hamparan gunungan sampah plastik dan limbah tercampur di tempat pembuangan akhir.'
  },
  {
    name: '02_buang_sampah_sembarangan_lingkungan.mp4',
    title: 'Pencemaran & Pembuangan Sampah Liar',
    input: path.join(RAW_DIR, 'illegal_dumping.webm'),
    start: '00:00:08',
    duration: '00:00:07.5',
    description: 'Sampah plastik, kardus, dan limbah rumah tangga yang dibuang sembarangan di parit dan pinggir jalan.'
  },
  {
    name: '03_transaksi_warga_setor_sampah.mp4',
    title: 'Transaksi Langsung Setor Sampah Warga ke Pos RW',
    input: path.join(RAW_DIR, 'transaksi_warga_rw05.mp4'),
    start: '00:02:22',
    duration: '00:00:09.0',
    description: 'Warga mengantar tumpukan kardus dan karung sampah dengan motor, berinteraksi langsung dengan pengurus bank sampah.'
  },
  {
    name: '04_penimbangan_fisik_timbangan_digital.mp4',
    title: 'Penimbangan Sampah & Pencatatan Lapangan',
    input: path.join(RAW_DIR, 'transaksi_warga_rw05.mp4'),
    start: '00:03:45',
    duration: '00:00:09.0',
    description: 'Petugas bank sampah menimbang sampah di timbangan digital disaksikan warga dan mencatat di buku kertas manual.'
  },
  {
    name: '05_pemilahan_botol_plastik_pet.mp4',
    title: 'Pemilahan Botol Plastik Daur Ulang',
    input: path.join(RAW_DIR, 'recycling_video.webm'),
    start: '00:00:23',
    duration: '00:00:08.5',
    description: 'Petugas memilah botol-botol plastik minuman di atas ban berjalan (conveyor belt).'
  },
  {
    name: '06_jemput_motor_tossa_lingkungan.mp4',
    title: 'Armada Motor Tossa Menjemput Sampah Warga',
    input: path.join(RAW_DIR, 'jemput_sampah_warga.mp4'),
    start: '00:00:33',
    duration: '00:00:09.0',
    description: 'Motor roda tiga Tossa pengangkut sampah melintas di jalan pemukiman warga menjemput sampah terpilah.'
  }
];

const renderedClips = [];

for (const clip of clipsConfig) {
  const outPath = path.join(OUT_DIR, clip.name);
  console.log(`▶ Trimming & Encoding: ${clip.title} -> ${clip.name}`);

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
    '-an',
    outPath
  ];

  const res = spawnSync('/usr/bin/ffmpeg', args);
  if (res.status !== 0) {
    console.error(`Error encoding ${clip.name}:`, res.stderr.toString());
  } else {
    console.log(`  ✓ Saved: ${outPath}`);
    renderedClips.push(outPath);
    fs.copyFileSync(outPath, path.join(USER_VIDEOS_DIR, clip.name));
  }
}

console.log(`\n🎞️ Stitching 6 Clips into Master Video with Crossfades & Full Audio Track...`);

// Measured durations:
// c0: 7.0s
// c1: 7.5s -> offset 6.5
// c2: 9.0s -> offset 6.5 + 7.5 - 0.5 = 13.5
// c3: 9.0s -> offset 13.5 + 9.0 - 0.5 = 22.0
// c4: 8.5s -> offset 22.0 + 9.0 - 0.5 = 30.5
// c5: 9.0s -> offset 30.5 + 8.5 - 0.5 = 38.5
// total video duration = 38.5 + 9.0 = 47.5s.

const filterComplex = [
  `[0:v][1:v]xfade=transition=fade:duration=0.5:offset=6.5[v01]`,
  `[v01][2:v]xfade=transition=fade:duration=0.5:offset=13.5[v02]`,
  `[v02][3:v]xfade=transition=fade:duration=0.5:offset=22.0[v03]`,
  `[v03][4:v]xfade=transition=fade:duration=0.5:offset=30.5[v04]`,
  `[v04][5:v]xfade=transition=fade:duration=0.5:offset=38.5[v_out]`
].join(';');

const tempVideoOnly = path.join(RAW_DIR, 'temp_video_only.mp4');

const stitchArgs = [
  '-y',
  '-i', renderedClips[0],
  '-i', renderedClips[1],
  '-i', renderedClips[2],
  '-i', renderedClips[3],
  '-i', renderedClips[4],
  '-i', renderedClips[5],
  '-filter_complex', filterComplex,
  '-map', '[v_out]',
  '-c:v', 'libx264',
  '-preset', 'fast',
  '-crf', '18',
  '-pix_fmt', 'yuv420p',
  tempVideoOnly
];

console.log('Rendering video montage...');
const stitchRes = spawnSync('/usr/bin/ffmpeg', stitchArgs);
if (stitchRes.status !== 0) {
  console.error('Error during video montage:', stitchRes.stderr.toString());
  process.exit(1);
}

console.log('Mixing Voiceover & Cinematic Piano BGM with Video...');

const voiceoverFile = path.join(RAW_DIR, 'voiceover_master.mp3');
const bgmFile = path.join(RAW_DIR, 'bgm_piano.ogg');
const masterOutWithAudio = path.join(OUT_DIR, 'broll_latar_belakang_master_suara.mp4');
const masterOutSilent = path.join(OUT_DIR, 'broll_latar_belakang_master.mp4');

// Copy silent video as master silent
fs.copyFileSync(tempVideoOnly, masterOutSilent);
fs.copyFileSync(tempVideoOnly, path.join(USER_VIDEOS_DIR, 'broll_latar_belakang_master.mp4'));

// ffmpeg mix: voiceover + BGM at 18% volume with fadeout
const audioFilter = `[1:a]volume=1.2[vocal];[2:a]volume=0.20,afade=t=out:st=45:d=2[bgm];[vocal][bgm]amix=inputs=2:duration=first:dropout_transition=2[a_out]`;

const finalArgs = [
  '-y',
  '-i', tempVideoOnly,
  '-i', voiceoverFile,
  '-i', bgmFile,
  '-filter_complex', audioFilter,
  '-map', '0:v',
  '-map', '[a_out]',
  '-c:v', 'copy',
  '-c:a', 'aac',
  '-b:a', '192k',
  '-shortest',
  masterOutWithAudio
];

const finalRes = spawnSync('/usr/bin/ffmpeg', finalArgs);
if (finalRes.status === 0) {
  console.log(`\n🎉 MASTER B-ROLL WITH AUDIO CREATED: ${masterOutWithAudio}`);
  fs.copyFileSync(masterOutWithAudio, path.join(USER_VIDEOS_DIR, 'broll_latar_belakang_master_suara.mp4'));
} else {
  console.error('Error mixing audio:', finalRes.stderr.toString());
}

console.log('\n✅ All completed successfully!');
