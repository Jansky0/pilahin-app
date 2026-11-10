import { spawnSync } from 'child_process';
import fs from 'fs';
import path from 'path';

const OUT_DIR = '/home/jansky/pilahin-app/public/broll_footages';
const USER_VIDEOS_DIR = '/home/jansky/Videos/broll_latar_belakang';
const RAW_DIR = '/home/jansky/pilahin-app/broll_raw';

// 1. Ensure 05_pemilahan_botol_plastik_pet.mp4 exists
const petOld = path.join(OUT_DIR, '04_pemilahan_botol_plastik_pet.mp4');
const petNew = path.join(OUT_DIR, '05_pemilahan_botol_plastik_pet.mp4');
if (fs.existsSync(petOld) && !fs.existsSync(petNew)) {
  fs.copyFileSync(petOld, petNew);
}

const clips = [
  path.join(OUT_DIR, '01_krisis_gunungan_sampah_tpa.mp4'),
  path.join(OUT_DIR, '02_buang_sampah_sembarangan_lingkungan.mp4'),
  path.join(OUT_DIR, '03_transaksi_warga_setor_sampah.mp4'),
  path.join(OUT_DIR, '04_penimbangan_fisik_timbangan_digital.mp4'),
  path.join(OUT_DIR, '05_pemilahan_botol_plastik_pet.mp4'),
  path.join(OUT_DIR, '06_jemput_motor_tossa_lingkungan.mp4')
];

for (const c of clips) {
  if (!fs.existsSync(c)) {
    console.error(`Missing clip: ${c}`);
    process.exit(1);
  }
  // Copy all 6 individual clips to user videos folder
  fs.copyFileSync(c, path.join(USER_VIDEOS_DIR, path.basename(c)));
}

console.log('✅ All 6 individual clips verified and synced to: ' + USER_VIDEOS_DIR);

// Durations:
// c0: 6.5s -> offset 6.0
// c1: 8.0s -> offset 13.5
// c2: 9.0s -> offset 22.0
// c3: 9.0s -> offset 30.5
// c4: 7.97s -> offset 37.97
// c5: 9.0s -> total = 46.97s.

const filterComplex = [
  `[0:v][1:v]xfade=transition=fade:duration=0.5:offset=6.0[v01]`,
  `[v01][2:v]xfade=transition=fade:duration=0.5:offset=13.5[v02]`,
  `[v02][3:v]xfade=transition=fade:duration=0.5:offset=22.0[v03]`,
  `[v03][4:v]xfade=transition=fade:duration=0.5:offset=30.5[v04]`,
  `[v04][5:v]xfade=transition=fade:duration=0.5:offset=37.97[v_out]`
].join(';');

const tempSilent = path.join(OUT_DIR, 'broll_latar_belakang_master.mp4');

console.log('🎞️ Stitching 6 clips with smooth crossfade transitions...');

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
  '-preset', 'fast',
  '-crf', '18',
  '-pix_fmt', 'yuv420p',
  tempSilent
];

const res1 = spawnSync('/usr/bin/ffmpeg', stitchArgs);
if (res1.status !== 0) {
  console.error('Error during video stitching:', res1.stderr.toString());
  process.exit(1);
}
console.log('✓ Stitched silent video created: ' + tempSilent);
fs.copyFileSync(tempSilent, path.join(USER_VIDEOS_DIR, 'broll_latar_belakang_master.mp4'));

// Now mix audio: voiceover + BGM
const voiceoverFile = path.join(RAW_DIR, 'voiceover_master.mp3');
const bgmFile = path.join(RAW_DIR, 'bgm_piano.ogg');
const masterWithAudio = path.join(OUT_DIR, 'broll_latar_belakang_master_suara.mp4');

console.log('🎵 Mixing Neural Voiceover & Ambient Piano Soundtrack...');

const audioFilter = `[1:a]volume=1.25[vocal];[2:a]volume=0.20,afade=t=out:st=44:d=3[bgm];[vocal][bgm]amix=inputs=2:duration=first:dropout_transition=2[a_out]`;

const mixArgs = [
  '-y',
  '-i', tempSilent,
  '-i', voiceoverFile,
  '-i', bgmFile,
  '-filter_complex', audioFilter,
  '-map', '0:v',
  '-map', '[a_out]',
  '-c:v', 'copy',
  '-c:a', 'aac',
  '-b:a', '192k',
  '-shortest',
  masterWithAudio
];

const res2 = spawnSync('/usr/bin/ffmpeg', mixArgs);
if (res2.status !== 0) {
  console.error('Error mixing audio:', res2.stderr.toString());
  process.exit(1);
}

console.log('✓ Master video with audio created: ' + masterWithAudio);
fs.copyFileSync(masterWithAudio, path.join(USER_VIDEOS_DIR, 'broll_latar_belakang_master_suara.mp4'));

console.log('\n🎉 ALL DONE! Check:');
console.log(' - ' + path.join(USER_VIDEOS_DIR, 'broll_latar_belakang_master_suara.mp4'));
