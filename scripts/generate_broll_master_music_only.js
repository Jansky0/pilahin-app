import { spawnSync } from 'child_process';
import fs from 'fs';
import path from 'path';

const PUBLIC_DIR = '/home/jansky/pilahin-app/public/broll_footages';
const USER_VIDEOS_DIR = '/home/jansky/Videos/broll_latar_belakang';
const RAW_DIR = '/home/jansky/pilahin-app/broll_raw';

fs.mkdirSync(PUBLIC_DIR, { recursive: true });
fs.mkdirSync(USER_VIDEOS_DIR, { recursive: true });

console.log('🎬 Assembling Clean 1080p B-Roll Master Video (Music Only - No Voiceover)...\n');

// 6 HD 1080p clips
const clips = [
  path.join(PUBLIC_DIR, '01_krisis_gunungan_sampah_tpa.mp4'),
  path.join(PUBLIC_DIR, '02_buang_sampah_sembarangan_lingkungan.mp4'),
  path.join(PUBLIC_DIR, '03_realita_tumpukan_sampah_indonesia.mp4'),
  path.join(PUBLIC_DIR, '04_pemilahan_botol_plastik_pet.mp4'),
  path.join(PUBLIC_DIR, '05_fasilitas_sortir_daur_ulang.mp4'),
  path.join(PUBLIC_DIR, '06_jemput_motor_tossa_lingkungan.mp4')
];

for (const c of clips) {
  if (!fs.existsSync(c)) {
    console.error(`❌ Clip not found: ${c}`);
    process.exit(1);
  }
  const basename = path.basename(c);
  fs.copyFileSync(c, path.join(USER_VIDEOS_DIR, basename));
  console.log(`  ✓ Synced clip: ${basename}`);
}

// Seamless crossfade offsets:
// c0 (6.5s) -> offset 6.0
// c1 (8.0s) -> offset 13.5
// c2 (8.0s) -> offset 21.0
// c3 (8.0s) -> offset 28.5
// c4 (8.0s) -> offset 36.0
// c5 (9.0s) -> total duration = 45.0s

const filterComplex = [
  `[0:v][1:v]xfade=transition=fade:duration=0.5:offset=6.0[v01]`,
  `[v01][2:v]xfade=transition=fade:duration=0.5:offset=13.5[v02]`,
  `[v02][3:v]xfade=transition=fade:duration=0.5:offset=21.0[v03]`,
  `[v03][4:v]xfade=transition=fade:duration=0.5:offset=28.5[v04]`,
  `[v04][5:v]xfade=transition=fade:duration=0.5:offset=36.0[v_out]`
].join(';');

const tempMontageVideo = path.join(RAW_DIR, 'temp_broll_montage_45s.mp4');

console.log('\n🎞️ Stitching 6 HD clips with 0.5s xfade crossfades...');
const stitchArgs = [
  '-y',
  '-i', clips[0],
  '-i', clips[1],
  '-i', clips[2],
  '-i', clips[3],
  '-i', clips[4],
  '-i', clips[5],
  '-filter_complex', filterComplex,
  '-map', '[v_out]',
  '-c:v', 'libx264',
  '-preset', 'slow',
  '-crf', '18',
  '-pix_fmt', 'yuv420p',
  tempMontageVideo
];

const stitchRes = spawnSync('/usr/bin/ffmpeg', stitchArgs);
if (stitchRes.status !== 0) {
  console.error('Error during video montage:', stitchRes.stderr.toString());
  process.exit(1);
}
console.log('✓ Video montage rendered successfully (45.0s)');

// Save silent copy
const silentMaster = path.join(PUBLIC_DIR, 'broll_latar_belakang_master_silent.mp4');
fs.copyFileSync(tempMontageVideo, silentMaster);
fs.copyFileSync(tempMontageVideo, path.join(USER_VIDEOS_DIR, 'broll_latar_belakang_master_silent.mp4'));

// Now mix Ambient Piano BGM exclusively (Music only, volume 0.90 with fade in/out, NO voiceover)
const bgmFile = path.join(RAW_DIR, 'bgm_piano.ogg');
if (!fs.existsSync(bgmFile)) {
  console.error(`BGM audio missing at ${bgmFile}`);
  process.exit(1);
}

const masterWithMusic = path.join(PUBLIC_DIR, 'broll_latar_belakang_master_music.mp4');
const audioFilter = `afade=t=in:st=0:d=1,afade=t=out:st=42.5:d=2.5,volume=0.92`;

console.log('\n🎵 Mixing Ambient Neoclassical Piano BGM (Music Only - No Voiceover)...');
const mixArgs = [
  '-y',
  '-i', tempMontageVideo,
  '-i', bgmFile,
  '-af', audioFilter,
  '-c:v', 'copy',
  '-c:a', 'aac',
  '-b:a', '256k',
  '-shortest',
  masterWithMusic
];

const mixRes = spawnSync('/usr/bin/ffmpeg', mixArgs);
if (mixRes.status !== 0) {
  console.error('Error mixing music:', mixRes.stderr.toString());
  process.exit(1);
}

// Copy to user folder and create standard aliases
fs.copyFileSync(masterWithMusic, path.join(USER_VIDEOS_DIR, 'broll_latar_belakang_master_music.mp4'));
fs.copyFileSync(masterWithMusic, path.join(PUBLIC_DIR, 'broll_latar_belakang_master.mp4'));
fs.copyFileSync(masterWithMusic, path.join(USER_VIDEOS_DIR, 'broll_latar_belakang_master.mp4'));

console.log('\n🎉 ALL DELIVERABLES GENERATED SUCCESSFULLY!');
console.log('Visual clips & Master Music Video:');
console.log(` - Master with Music: ${path.join(USER_VIDEOS_DIR, 'broll_latar_belakang_master_music.mp4')}`);
console.log(` - Master Silent:     ${path.join(USER_VIDEOS_DIR, 'broll_latar_belakang_master_silent.mp4')}`);
console.log(` - Public Web App:    ${masterWithMusic}`);
