import os
import subprocess
import shutil

def create_svg_phase1():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 920" width="1000" height="920" style="background:#ffffff; font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;">
  <defs>
    <marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#000000" />
    </marker>
  </defs>

  <!-- Title -->
  <text x="500" y="32" text-anchor="middle" font-size="16" font-weight="bold" fill="#000000">FASE 1: REGISTRASI, VERIFIKASI OTP &amp; LOGIN</text>
  <text x="500" y="52" text-anchor="middle" font-size="11" fill="#444444">Alur Granular 1 Proses per Kotak — Penanganan Sad Path Validasi &amp; OTP — Monokrom</text>

  <!-- Start -->
  <rect x="410" y="70" width="180" height="34" rx="17" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
  <text x="500" y="92" text-anchor="middle" font-size="12" font-weight="bold" fill="#000000">Mulai: Buka Pilah.in</text>

  <!-- Connector -->
  <line x1="500" y1="104" x2="500" y2="128" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <!-- Landing -->
  <rect x="380" y="130" width="240" height="42" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="500" y="148" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Buka Halaman Utama (Landing)</text>
  <text x="500" y="162" text-anchor="middle" font-size="9" fill="#444444">Pelajari sistem sirkular &amp; harga sampah</text>

  <!-- Connector -->
  <line x1="500" y1="172" x2="500" y2="198" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <!-- Decision: Has Account -->
  <polygon points="500,200 580,230 500,260 420,230" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="500" y="227" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Sudah Punya</text>
  <text x="500" y="239" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Akun?</text>

  <!-- Left: Register -->
  <path d="M 420 230 L 230 230 L 230 278" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="315" y="222" text-anchor="middle" font-size="10" fill="#000000">Belum (Daftar)</text>

  <!-- Right: Login -->
  <path d="M 580 230 L 760 230 L 760 278" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="680" y="222" text-anchor="middle" font-size="10" fill="#000000">Sudah (Masuk)</text>

  <!-- REGISTER -->
  <rect x="130" y="280" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="230" y="297" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Pilih Peran Akun</text>
  <text x="230" y="311" text-anchor="middle" font-size="9" fill="#444444">Warga Penyetor atau Mitra Bank Sampah</text>

  <line x1="230" y1="320" x2="230" y2="343" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="130" y="345" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="230" y="362" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Input Data Diri &amp; Akun</text>
  <text x="230" y="376" text-anchor="middle" font-size="9" fill="#444444">Nama, No WhatsApp, Kata Sandi</text>

  <line x1="230" y1="385" x2="230" y2="408" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <polygon points="230,410 295,435 230,460 165,435" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="230" y="432" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Format Data</text>
  <text x="230" y="444" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Valid?</text>

  <!-- Sad Path 1: Format Error -->
  <path d="M 165 435 L 90 435" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="125" y="428" text-anchor="middle" font-size="9" fill="#000000">Tidak</text>
  <rect x="10" y="415" width="80" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="50" y="430" text-anchor="middle" font-size="8" font-weight="bold" fill="#000000">SISTEM MENOLAK</text>
  <text x="50" y="443" text-anchor="middle" font-size="7" fill="#444444">Format Salah (Sad Path)</text>
  <path d="M 50 415 L 50 365 L 128 365" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3" marker-end="url(#arr)"/>

  <!-- Valid OTP -->
  <line x1="230" y1="460" x2="230" y2="488" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="245" y="475" font-size="9" fill="#000000">Ya</text>

  <rect x="130" y="490" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="230" y="507" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Kirim Kode OTP ke WhatsApp</text>
  <text x="230" y="521" text-anchor="middle" font-size="9" fill="#444444">Sistem kirim 6 digit verifikasi resmi</text>

  <line x1="230" y1="530" x2="230" y2="553" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="130" y="555" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="230" y="572" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Input Kode OTP 6 Digit</text>
  <text x="230" y="586" text-anchor="middle" font-size="9" fill="#444444">Ketik kode yang diterima di WhatsApp</text>

  <line x1="230" y1="595" x2="230" y2="618" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <polygon points="230,620 295,645 230,670 165,645" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="230" y="642" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Kode OTP</text>
  <text x="230" y="654" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Cocok?</text>

  <!-- Sad Path 2: OTP Salah -->
  <path d="M 165 645 L 90 645" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="125" y="638" text-anchor="middle" font-size="9" fill="#000000">Salah</text>
  <rect x="10" y="625" width="80" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="50" y="640" text-anchor="middle" font-size="8" font-weight="bold" fill="#000000">SISTEM MENOLAK</text>
  <text x="50" y="653" text-anchor="middle" font-size="7" fill="#444444">OTP Salah (Sad Path)</text>
  <path d="M 50 625 L 50 510 L 128 510" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3" marker-end="url(#arr)"/>

  <line x1="230" y1="670" x2="230" y2="698" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="245" y="685" font-size="9" fill="#000000">Cocok</text>

  <rect x="130" y="700" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="230" y="717" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Input Alamat &amp; Titik Jemput</text>
  <text x="230" y="731" text-anchor="middle" font-size="9" fill="#444444">Jalan, RT/RW &amp; patokan teras warga</text>

  <line x1="230" y1="740" x2="230" y2="768" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="130" y="770" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="230" y="787" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Buat 6 Digit PIN Transaksi</text>
  <text x="230" y="801" text-anchor="middle" font-size="9" fill="#444444">Keamanan belanja sirkular &amp; kas tunai</text>

  <line x1="230" y1="810" x2="230" y2="838" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="130" y="840" width="200" height="35" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="230" y="862" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Registrasi Berhasil</text>

  <!-- LOGIN -->
  <rect x="660" y="280" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="760" y="297" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Input No. WhatsApp / Email</text>
  <text x="760" y="311" text-anchor="middle" font-size="9" fill="#444444">Ketik nomor akun terdaftar di Pilah.in</text>

  <line x1="760" y1="320" x2="760" y2="348" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <polygon points="760,350 825,375 760,400 695,375" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="760" y="372" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Lupa Kata</text>
  <text x="760" y="384" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Sandi?</text>

  <!-- Lupa Sandi Branch -->
  <path d="M 825 375 L 890 375 L 890 418" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="855" y="367" text-anchor="middle" font-size="9" fill="#000000">Ya</text>

  <rect x="835" y="420" width="130" height="38" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="900" y="437" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Klik 'Lupa Password'</text>
  <text x="900" y="449" text-anchor="middle" font-size="8" fill="#444444">Kirim OTP reset via WA</text>

  <line x1="900" y1="458" x2="900" y2="483" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="835" y="485" width="130" height="38" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="900" y="502" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Input OTP Reset WA</text>
  <text x="900" y="514" text-anchor="middle" font-size="8" fill="#444444">Verifikasi identitas nomor</text>

  <line x1="900" y1="523" x2="900" y2="548" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="835" y="550" width="130" height="38" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="900" y="567" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Input Kata Sandi Baru</text>
  <text x="900" y="579" text-anchor="middle" font-size="8" fill="#444444">Simpan sandi pengganti</text>
  <path d="M 900 588 L 900 610 L 820 610 L 820 445 L 820 300 L 862 300" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3" marker-end="url(#arr)"/>

  <!-- Normal Login -->
  <line x1="760" y1="400" x2="760" y2="428" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="775" y="415" font-size="9" fill="#000000">Ingat</text>

  <rect x="680" y="430" width="160" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="760" y="447" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Input Kata Sandi Akun</text>
  <text x="760" y="461" text-anchor="middle" font-size="9" fill="#444444">Ketik kata sandi akun terdaftar</text>

  <line x1="760" y1="470" x2="760" y2="498" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <polygon points="760,500 825,525 760,550 695,525" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="760" y="522" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Kredensial</text>
  <text x="760" y="534" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Cocok?</text>

  <!-- Sad Path 3: Kredensial Salah -->
  <path d="M 695 525 L 630 525" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="660" y="517" text-anchor="middle" font-size="9" fill="#000000">Salah</text>
  <rect x="530" y="505" width="100" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="580" y="520" text-anchor="middle" font-size="8" font-weight="bold" fill="#000000">SISTEM MENOLAK</text>
  <text x="580" y="533" text-anchor="middle" font-size="7" fill="#444444">Sandi Salah (Sad Path)</text>
  <path d="M 580 505 L 580 450 L 678 450" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3" marker-end="url(#arr)"/>

  <line x1="760" y1="550" x2="760" y2="578" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="775" y="565" font-size="9" fill="#000000">Cocok</text>

  <rect x="670" y="580" width="180" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="760" y="597" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Login Berhasil</text>
  <text x="760" y="611" text-anchor="middle" font-size="9" fill="#444444">Sesi masuk aktif &amp; token terbit</text>

  <!-- END CONVERGENCE -->
  <path d="M 230 875 L 230 895 L 398 895" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <path d="M 760 620 L 760 895 L 602 895" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="400" y="878" width="200" height="34" rx="17" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
  <text x="500" y="900" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Selesai: Masuk Beranda</text>
</svg>'''


def create_svg_phase2():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 700" width="950" height="700" style="background:#ffffff; font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;">
  <defs>
    <marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#000000" />
    </marker>
  </defs>

  <text x="475" y="32" text-anchor="middle" font-size="16" font-weight="bold" fill="#000000">FASE 2: BERANDA WARGA &amp; DETEKSI SAMPAH (SNAPSORT AI)</text>
  <text x="475" y="52" text-anchor="middle" font-size="11" fill="#444444">Pengecekan Saldo Mengendap, Deteksi Kamera AI &amp; Sad Path Limbah B3 / Buram — Monokrom</text>

  <rect x="375" y="70" width="200" height="34" rx="17" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
  <text x="475" y="92" text-anchor="middle" font-size="12" font-weight="bold" fill="#000000">Mulai: Beranda Warga</text>

  <line x1="475" y1="104" x2="475" y2="128" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="350" y="130" width="250" height="42" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="475" y="148" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Pantau Saldo Mengendap &amp; Tiket</text>
  <text x="475" y="162" text-anchor="middle" font-size="9" fill="#444444">Saldo rupiah nyata siap cair &amp; status jemputan</text>

  <line x1="475" y1="172" x2="475" y2="198" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <polygon points="475,200 555,225 475,250 395,225" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="475" y="222" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Gunakan Pindai</text>
  <text x="475" y="234" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">SnapSort AI?</text>

  <!-- Left: Manual -->
  <path d="M 395 225 L 220 225 L 220 288" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="290" y="217" text-anchor="middle" font-size="10" fill="#000000">Tidak (Manual)</text>

  <rect x="120" y="290" width="200" height="42" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="220" y="308" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Buka Tab 'Setor Sampah'</text>
  <text x="220" y="322" text-anchor="middle" font-size="9" fill="#444444">Pemilihan kategori manual</text>

  <!-- Right: AI -->
  <path d="M 555 225 L 700 225 L 700 288" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="635" y="217" text-anchor="middle" font-size="10" fill="#000000">Ya (Buka AI)</text>

  <rect x="600" y="290" width="200" height="42" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="700" y="308" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Buka Tab 'SnapSort AI'</text>
  <text x="700" y="322" text-anchor="middle" font-size="9" fill="#444444">Kamera pemindai jenis sampah</text>

  <line x1="700" y1="332" x2="700" y2="358" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="600" y="360" width="200" height="42" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="700" y="378" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Arahkan Kamera &amp; Foto</text>
  <text x="700" y="392" text-anchor="middle" font-size="9" fill="#444444">Posisikan material sampah di tengah</text>

  <line x1="700" y1="402" x2="700" y2="428" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <polygon points="700,430 780,455 700,480 620,455" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="700" y="452" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Hasil Analisis</text>
  <text x="700" y="464" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Kamera AI?</text>

  <!-- Sad Path 1: B3 (SISTEM MENOLAK) -->
  <path d="M 780 455 L 850 455 L 850 508" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="815" y="447" text-anchor="middle" font-size="9" fill="#000000">B3/Medis</text>
  <rect x="780" y="510" width="140" height="44" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="850" y="527" text-anchor="middle" font-size="9" font-weight="bold" fill="#000000">SISTEM MENOLAK</text>
  <text x="850" y="541" text-anchor="middle" font-size="8" fill="#444444">Limbah B3 Dilarang! (Sad)</text>

  <!-- Sad Path 2: Buram (SISTEM MENOLAK) -->
  <path d="M 620 455 L 520 455 L 520 508" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="565" y="447" text-anchor="middle" font-size="9" fill="#000000">Buram/Gelap</text>
  <rect x="450" y="510" width="140" height="44" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="520" y="527" text-anchor="middle" font-size="9" font-weight="bold" fill="#000000">SISTEM MENOLAK</text>
  <text x="520" y="541" text-anchor="middle" font-size="8" fill="#444444">Objek Buram, Foto Ulang</text>
  <path d="M 520 510 L 520 381 L 598 381" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3" marker-end="url(#arr)"/>

  <!-- Valid Material (Happy Path) -->
  <line x1="700" y1="480" x2="700" y2="508" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="715" y="498" font-size="9" fill="#000000">Lolos</text>

  <rect x="620" y="510" width="160" height="42" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="700" y="528" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Deteksi Material Valid</text>
  <text x="700" y="541" text-anchor="middle" font-size="8" fill="#444444">Botol PET 96%, Rp 3.500/kg</text>

  <line x1="700" y1="552" x2="700" y2="578" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="605" y="580" width="190" height="38" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="700" y="597" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Klik 'Langsung Setor'</text>
  <text x="700" y="609" text-anchor="middle" font-size="8" fill="#444444">Auto-centang kategori di Tab Setor</text>

  <!-- Convergence to End -->
  <path d="M 220 332 L 220 645 L 348 645" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <path d="M 700 618 L 700 645 L 572 645" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="350" y="630" width="220" height="34" rx="17" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
  <text x="460" y="652" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Lanjut ke Halaman Setor Sampah</text>
</svg>'''


def create_svg_phase3():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 840" width="1000" height="840" style="background:#ffffff; font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;">
  <defs>
    <marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#000000" />
    </marker>
  </defs>

  <text x="500" y="32" text-anchor="middle" font-size="16" font-weight="bold" fill="#000000">FASE 3: PENGAJUAN PENYETORAN SAMPAH</text>
  <text x="500" y="52" text-anchor="middle" font-size="11" fill="#444444">Kalkulasi Jemput 10% vs Drop-off 0% &amp; Sad Path Sistem Menolak (Di Luar Radius > 3 km) — Monokrom</text>

  <rect x="400" y="70" width="200" height="34" rx="17" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
  <text x="500" y="92" text-anchor="middle" font-size="12" font-weight="bold" fill="#000000">Mulai: Tab Setor Sampah</text>

  <line x1="500" y1="104" x2="500" y2="128" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="385" y="130" width="230" height="42" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="500" y="148" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Pilih Kategori &amp; Atur Berat (kg)</text>
  <text x="500" y="162" text-anchor="middle" font-size="9" fill="#444444">Centang sampah &amp; sesuaikan stepper kg</text>

  <line x1="500" y1="172" x2="500" y2="198" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <polygon points="500,200 580,225 500,250 420,225" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="500" y="222" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Kategori &amp; Berat</text>
  <text x="500" y="234" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Valid?</text>

  <!-- Sad Path: Belum pilih item -->
  <path d="M 420 225 L 320 225" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="370" y="217" text-anchor="middle" font-size="9" fill="#000000">Tidak</text>
  <rect x="170" y="205" width="150" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="245" y="222" text-anchor="middle" font-size="9" font-weight="bold" fill="#000000">SISTEM MENOLAK</text>
  <text x="245" y="235" text-anchor="middle" font-size="8" fill="#444444">Pilih min. 1 jenis sampah</text>
  <path d="M 245 205 L 245 151 L 383 151" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3" marker-end="url(#arr)"/>

  <!-- Decision: Method -->
  <line x1="500" y1="250" x2="500" y2="278" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="515" y="268" font-size="9" fill="#000000">Ya</text>

  <polygon points="500,280 580,310 500,340 420,310" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="500" y="307" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Pilih Metode</text>
  <text x="500" y="319" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Setor?</text>

  <!-- JEMPUT TOSSA -->
  <path d="M 420 310 L 250 310 L 250 358" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="320" y="302" text-anchor="middle" font-size="10" fill="#000000">Jemput Armada Tossa</text>

  <rect x="150" y="360" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="250" y="377" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Kalkulasi Ongkir Jemput 10%</text>
  <text x="250" y="391" text-anchor="middle" font-size="9" fill="#444444">Gross total - 10% operasional armada</text>

  <line x1="250" y1="400" x2="250" y2="428" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="150" y="430" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="250" y="447" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Pilih Alamat Jemput</text>
  <text x="250" y="461" text-anchor="middle" font-size="9" fill="#444444">Alamat tersimpan &amp; patokan teras</text>

  <line x1="250" y1="470" x2="250" y2="498" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <!-- Decision: Radius Check (SAD PATH) -->
  <polygon points="250,500 320,525 250,550 180,525" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="250" y="522" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Radius</text>
  <text x="250" y="534" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">&lt;= 3 km?</text>

  <!-- Sad Path: Luar Radius -->
  <path d="M 180 525 L 120 525" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="150" y="517" text-anchor="middle" font-size="9" fill="#000000">&gt; 3 km</text>
  <rect x="10" y="505" width="110" height="42" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="65" y="522" text-anchor="middle" font-size="8" font-weight="bold" fill="#000000">SISTEM MENOLAK</text>
  <text x="65" y="535" text-anchor="middle" font-size="7" fill="#444444">Di Luar Radius (Sad Path)</text>
  <path d="M 65 547 L 65 590 L 148 590" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="150" y="570" width="170" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="235" y="587" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Arahkan ke Drop-off</text>
  <text x="235" y="599" text-anchor="middle" font-size="8" fill="#444444">Beralih ke pos mitra terdekat</text>
  <path d="M 320 590 L 730 590 L 730 402" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3" marker-end="url(#arr)"/>

  <!-- Happy Radius -->
  <line x1="250" y1="550" x2="250" y2="638" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="265" y="575" font-size="9" fill="#000000">&lt;= 3 km</text>

  <rect x="150" y="640" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="250" y="657" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Klik 'Ajukan Penjemputan Tossa'</text>
  <text x="250" y="671" text-anchor="middle" font-size="9" fill="#444444">Armada roda 3 RW dijadwalkan</text>

  <!-- DROP-OFF MANDIRI -->
  <path d="M 580 310 L 730 310 L 730 358" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="660" y="302" text-anchor="middle" font-size="10" fill="#000000">Antar Sendiri (0% Ongkir)</text>

  <rect x="630" y="360" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="730" y="377" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Kalkulasi Drop-off (0% Ongkir)</text>
  <text x="730" y="391" text-anchor="middle" font-size="9" fill="#444444">Ongkos kirim Rp 0, saldo 100% utuh</text>

  <line x1="730" y1="400" x2="730" y2="428" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="630" y="430" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="730" y="447" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Pilih Pos / Drop Point Mitra</text>
  <text x="730" y="461" text-anchor="middle" font-size="9" fill="#444444">TPS3R RW 05 / Bank Sampah terdekat</text>

  <line x1="730" y1="470" x2="730" y2="498" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="630" y="500" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="730" y="517" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Klik 'Buat Tiket Mandiri'</text>
  <text x="730" y="531" text-anchor="middle" font-size="9" fill="#444444">Terbitkan tiket drop-off ke pos mitra</text>

  <!-- MERGE: TIKET TERBIT -->
  <path d="M 250 680 L 250 715 L 398 715" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <path d="M 730 540 L 730 715 L 602 715" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="400" y="695" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="500" y="712" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Tiket Digital QR Terbit</text>
  <text x="500" y="726" text-anchor="middle" font-size="9" fill="#444444">ID: PLH-XXXXXX, Siap Ditimbang</text>

  <line x1="500" y1="735" x2="500" y2="763" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="390" y="765" width="220" height="34" rx="17" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
  <text x="500" y="787" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Selesai: Menunggu Timbangan</text>
</svg>'''


def create_svg_phase4():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 860" width="1000" height="860" style="background:#ffffff; font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;">
  <defs>
    <marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#000000" />
    </marker>
  </defs>

  <text x="500" y="32" text-anchor="middle" font-size="16" font-weight="bold" fill="#000000">FASE 4: OPERASIONAL TIMBANG LAPANGAN &amp; VERIFIKASI MITRA</text>
  <text x="500" y="52" text-anchor="middle" font-size="11" fill="#444444">Timbang Digital Bersama &amp; SAD PATH: SISTEM MENOLAK (KURASI FISIK GAGAL) — Monokrom</text>

  <rect x="400" y="70" width="200" height="34" rx="17" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
  <text x="500" y="92" text-anchor="middle" font-size="12" font-weight="bold" fill="#000000">Mulai: Tiket Digital Aktif</text>

  <line x1="500" y1="104" x2="500" y2="128" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <polygon points="500,130 580,160 500,190 420,160" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="500" y="157" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Jenis Penyetoran</text>
  <text x="500" y="169" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Lapangan?</text>

  <!-- Left: Jemput Tossa -->
  <path d="M 420 160 L 250 160 L 250 208" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="325" y="152" text-anchor="middle" font-size="10" fill="#000000">Jemput Tossa</text>

  <rect x="150" y="210" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="250" y="227" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Motor Tossa Tiba di Alamat</text>
  <text x="250" y="241" text-anchor="middle" font-size="9" fill="#444444">Kurir cek patokan &amp; kontak WA</text>

  <line x1="250" y1="250" x2="250" y2="278" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <polygon points="250,280 315,305 250,330 185,305" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="250" y="302" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Warga Ada di</text>
  <text x="250" y="314" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Lokasi?</text>

  <!-- Sad Path: Warga tidak ada -->
  <path d="M 185 305 L 100 305" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="140" y="297" text-anchor="middle" font-size="9" fill="#000000">Tidak</text>
  <rect x="10" y="285" width="90" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="55" y="302" text-anchor="middle" font-size="9" font-weight="bold" fill="#000000">Jadwal Ulang</text>
  <text x="55" y="315" text-anchor="middle" font-size="8" fill="#444444">Tiket tetap aktif</text>

  <line x1="250" y1="330" x2="250" y2="358" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="265" y="348" font-size="9" fill="#000000">Ada</text>

  <rect x="150" y="360" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="250" y="377" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Timbang Digital di Teras</text>
  <text x="250" y="391" text-anchor="middle" font-size="9" fill="#444444">Timbangan gantung disaksikan bersama</text>

  <!-- Right: Drop-off Mandiri -->
  <path d="M 580 160 L 750 160 L 750 208" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="665" y="152" text-anchor="middle" font-size="10" fill="#000000">Antar Sendiri</text>

  <rect x="650" y="210" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="750" y="227" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Warga Bawa Sampah ke Pos</text>
  <text x="750" y="241" text-anchor="middle" font-size="9" fill="#444444">Tiba di Bank Sampah / TPS3R Mitra</text>

  <line x1="750" y1="250" x2="750" y2="278" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <polygon points="750,280 815,305 750,330 685,305" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="750" y="302" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Pos Sedang</text>
  <text x="750" y="314" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Buka?</text>

  <!-- Sad Path: Pos Tutup -->
  <path d="M 815 305 L 890 305" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="850" y="297" text-anchor="middle" font-size="9" fill="#000000">Tutup</text>
  <rect x="890" y="285" width="90" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="935" y="302" text-anchor="middle" font-size="9" font-weight="bold" fill="#000000">Pos Tutup</text>
  <text x="935" y="315" text-anchor="middle" font-size="8" fill="#444444">Kembali besok</text>

  <line x1="750" y1="330" x2="750" y2="358" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="765" y="348" font-size="9" fill="#000000">Buka</text>

  <rect x="650" y="360" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="750" y="377" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Petugas Timbang di Pos</text>
  <text x="750" y="391" text-anchor="middle" font-size="9" fill="#444444">Pengukuran timbangan digital pos</text>

  <!-- PORTAL MITRA -->
  <path d="M 250 400 L 250 435 L 398 435" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <path d="M 750 400 L 750 435 L 602 435" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="400" y="415" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="500" y="432" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Buka Portal Mitra Pengelola</text>
  <text x="500" y="446" text-anchor="middle" font-size="9" fill="#444444">Petugas masuk dasbor operasional</text>

  <line x1="500" y1="455" x2="500" y2="483" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="400" y="485" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="500" y="502" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Input No Tiket &amp; Bobot Riil</text>
  <text x="500" y="516" text-anchor="middle" font-size="9" fill="#444444">Ketik PLH-XXXXXX &amp; kg timbangan</text>

  <line x1="500" y1="525" x2="500" y2="553" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <!-- DECISION: KURASI FISIK LOLOS STANDAR? -->
  <polygon points="500,555 580,585 500,615 420,585" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="500" y="582" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Kurasi Fisik</text>
  <text x="500" y="594" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Lolos Standar?</text>

  <!-- SAD PATH: KURASI GAGAL (SISTEM MENOLAK) -->
  <path d="M 420 585 L 310 585" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="365" y="577" text-anchor="middle" font-size="9" fill="#000000">Tolak (Gagal)</text>

  <rect x="130" y="565" width="180" height="44" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="220" y="582" text-anchor="middle" font-size="9" font-weight="bold" fill="#000000">SISTEM MENOLAK (SAD PATH)</text>
  <text x="220" y="596" text-anchor="middle" font-size="8" fill="#444444">Kardus Basah / Minyak / B3</text>

  <line x1="220" y1="609" x2="220" y2="633" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="130" y="635" width="180" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="220" y="652" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Tiket Ditolak &amp; Saldo Rp 0</text>
  <text x="220" y="666" text-anchor="middle" font-size="8" fill="#444444">Petugas klik 'Tolak Sampah'</text>

  <line x1="220" y1="675" x2="220" y2="703" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="130" y="705" width="180" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="220" y="722" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Kirim Edukasi Pilah ke Warga</text>
  <text x="220" y="736" text-anchor="middle" font-size="8" fill="#444444">Banner merah &amp; tombol Setor Ulang</text>

  <!-- HAPPY PATH: LOLOS KURASI -->
  <line x1="580" y1="585" x2="688" y2="585" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="635" y="577" text-anchor="middle" font-size="9" fill="#000000">Lolos</text>

  <rect x="690" y="565" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="790" y="582" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Verifikasi &amp; Hitung Nilai</text>
  <text x="790" y="596" text-anchor="middle" font-size="9" fill="#444444">Kalkulasi total nilai rupiah bersih</text>

  <line x1="790" y1="605" x2="790" y2="633" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="680" y="635" width="220" height="42" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="790" y="652" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Saldo Tunai Masuk ke Dompet</text>
  <text x="790" y="666" text-anchor="middle" font-size="9" fill="#444444">Kredit instan bertambah &amp; tiket selesai</text>

  <line x1="790" y1="677" x2="790" y2="713" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="680" y="715" width="220" height="34" rx="17" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
  <text x="790" y="737" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Selesai: Saldo Siap Dipakai</text>
</svg>'''


def create_svg_phase5():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 860" width="1000" height="860" style="background:#ffffff; font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;">
  <defs>
    <marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#000000" />
    </marker>
  </defs>

  <text x="500" y="32" text-anchor="middle" font-size="16" font-weight="bold" fill="#000000">FASE 5: PEMANFAATAN SALDO LIKUID WARGA</text>
  <text x="500" y="52" text-anchor="middle" font-size="11" fill="#444444">Belanja Upcycle Kompos vs E-Wallet &amp; SAD PATH: PIN Salah 3x / Saldo Kurang — Monokrom</text>

  <rect x="400" y="70" width="200" height="34" rx="17" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
  <text x="500" y="92" text-anchor="middle" font-size="12" font-weight="bold" fill="#000000">Mulai: Saldo di Dompet</text>

  <line x1="500" y1="104" x2="500" y2="128" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <polygon points="500,130 580,160 500,190 420,160" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="500" y="157" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Pemanfaatan</text>
  <text x="500" y="169" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Saldo?</text>

  <!-- Left: Belanja Produk -->
  <path d="M 420 160 L 250 160 L 250 208" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="325" y="152" text-anchor="middle" font-size="10" fill="#000000">Belanja Upcycle</text>

  <rect x="150" y="210" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="250" y="227" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Buka Tab 'Toko Sirkular'</text>
  <text x="250" y="241" text-anchor="middle" font-size="9" fill="#444444">Katalog pupuk kompos mitra RW</text>

  <line x1="250" y1="250" x2="250" y2="278" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="150" y="280" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="250" y="297" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Pilih Pupuk Kompos (Rp 18k)</text>
  <text x="250" y="311" text-anchor="middle" font-size="9" fill="#444444">Klik tombol 'Beli Produk'</text>

  <line x1="250" y1="320" x2="250" y2="348" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <polygon points="250,350 320,375 250,400 180,375" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="250" y="372" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Saldo &gt;=</text>
  <text x="250" y="384" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Rp 18.000?</text>

  <!-- Sad Path: Saldo Kurang Belanja -->
  <path d="M 180 375 L 100 375" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="140" y="367" text-anchor="middle" font-size="9" fill="#000000">Kurang</text>
  <rect x="10" y="355" width="90" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="55" y="370" text-anchor="middle" font-size="8" font-weight="bold" fill="#000000">SISTEM MENOLAK</text>
  <text x="55" y="383" text-anchor="middle" font-size="7" fill="#444444">Saldo Kurang (Sad)</text>

  <line x1="250" y1="400" x2="250" y2="428" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="265" y="415" font-size="9" fill="#000000">Cukup</text>

  <rect x="150" y="430" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="250" y="447" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Input PIN Transaksi 6 Digit</text>
  <text x="250" y="461" text-anchor="middle" font-size="9" fill="#444444">Otorisasi pemotongan saldo belanja</text>

  <line x1="250" y1="470" x2="250" y2="498" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <polygon points="250,500 320,525 250,550 180,525" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="250" y="522" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">PIN 6-Digit</text>
  <text x="250" y="534" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Valid?</text>

  <!-- Sad Path PIN Belanja Salah 3x -->
  <path d="M 180 525 L 100 525" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="140" y="517" text-anchor="middle" font-size="9" fill="#000000">Salah 3x</text>
  <rect x="10" y="505" width="90" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="55" y="520" text-anchor="middle" font-size="8" font-weight="bold" fill="#000000">SISTEM MENOLAK</text>
  <text x="55" y="533" text-anchor="middle" font-size="7" fill="#444444">Akun Kunci 15 mnt</text>

  <line x1="250" y1="550" x2="250" y2="578" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="265" y="565" font-size="9" fill="#000000">Benar</text>

  <rect x="150" y="580" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="250" y="597" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Pembelian Kompos Selesai</text>
  <text x="250" y="611" text-anchor="middle" font-size="9" fill="#444444">Saldo terpotong Rp 18.000 bersih</text>

  <!-- Right: Tarik Tunai E-Wallet -->
  <path d="M 580 160 L 750 160 L 750 208" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="665" y="152" text-anchor="middle" font-size="10" fill="#000000">Tarik Tunai E-Wallet</text>

  <rect x="650" y="210" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="750" y="227" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Buka Tab 'Dompet'</text>
  <text x="750" y="241" text-anchor="middle" font-size="9" fill="#444444">Formulir penarikan saldo ke e-wallet</text>

  <line x1="750" y1="250" x2="750" y2="278" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="650" y="280" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="750" y="297" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Pilih E-Wallet &amp; Nominal</text>
  <text x="750" y="311" text-anchor="middle" font-size="9" fill="#444444">GoPay/DANA &amp; nominal Rp 50.000</text>

  <line x1="750" y1="320" x2="750" y2="348" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <polygon points="750,350 820,375 750,400 680,375" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="750" y="372" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Saldo &gt;=</text>
  <text x="750" y="384" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Nominal?</text>

  <!-- Sad Path: Saldo Kurang Tarik -->
  <path d="M 820 375 L 890 375" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="855" y="367" text-anchor="middle" font-size="9" fill="#000000">Kurang</text>
  <rect x="890" y="355" width="100" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="940" y="370" text-anchor="middle" font-size="8" font-weight="bold" fill="#000000">SISTEM MENOLAK</text>
  <text x="940" y="383" text-anchor="middle" font-size="7" fill="#444444">Saldo Tidak Cukup</text>

  <line x1="750" y1="400" x2="750" y2="428" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="765" y="415" font-size="9" fill="#000000">Cukup</text>

  <rect x="650" y="430" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="750" y="447" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Input PIN Transaksi 6 Digit</text>
  <text x="750" y="461" text-anchor="middle" font-size="9" fill="#444444">Otorisasi pencairan dana e-wallet</text>

  <line x1="750" y1="470" x2="750" y2="498" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <polygon points="750,500 820,525 750,550 680,525" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="750" y="522" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">PIN 6-Digit</text>
  <text x="750" y="534" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Valid?</text>

  <!-- Sad Path PIN Tarik Salah 3x -->
  <path d="M 820 525 L 890 525" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="855" y="517" text-anchor="middle" font-size="9" fill="#000000">Salah 3x</text>
  <rect x="890" y="505" width="100" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="940" y="520" text-anchor="middle" font-size="8" font-weight="bold" fill="#000000">SISTEM MENOLAK</text>
  <text x="940" y="533" text-anchor="middle" font-size="7" fill="#444444">Akun Kunci 15 mnt</text>

  <line x1="750" y1="550" x2="750" y2="578" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="765" y="565" font-size="9" fill="#000000">Benar</text>

  <rect x="650" y="580" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="750" y="597" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Uang Cair ke E-Wallet</text>
  <text x="750" y="611" text-anchor="middle" font-size="9" fill="#444444">Saldo terpotong Rp 50k (0% admin)</text>

  <!-- MERGE CONVERGENCE -->
  <path d="M 250 620 L 250 715 L 398 715" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <path d="M 750 620 L 750 715 L 602 715" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="400" y="698" width="200" height="34" rx="17" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
  <text x="500" y="720" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Selesai: Dampak Nyata</text>
</svg>'''


def main():
    img_dir = "/home/jansky/pilahin-app/flow_screenshots"
    public_dir = "/home/jansky/pilahin-app/public/flow_screenshots"
    brain_dir = "/home/jansky/.gemini/antigravity-cli/brain/aee97e02-8282-4ad4-be88-03497eee84f2"
    os.makedirs(img_dir, exist_ok=True)
    os.makedirs(public_dir, exist_ok=True)
    os.makedirs(brain_dir, exist_ok=True)

    generators = [
        ("fase_1_registrasi_dan_login", create_svg_phase1, 1000, 920),
        ("fase_2_beranda_dan_snapsort_ai", create_svg_phase2, 950, 700),
        ("fase_3_pengajuan_setor_sampah", create_svg_phase3, 1000, 840),
        ("fase_4_timbang_lapangan_dan_mitra", create_svg_phase4, 1000, 860),
        ("fase_5_belanja_toko_dan_tarik_tunai", create_svg_phase5, 1000, 860),
    ]

    for name, func, w, h in generators:
        svg_content = func()
        svg_file = os.path.join(img_dir, f"{name}.svg")
        png_file = os.path.join(img_dir, f"{name}.png")
        html_file = os.path.join(img_dir, f"{name}.html")

        with open(svg_file, "w", encoding="utf-8") as f:
            f.write(svg_content)

        html_content = f'''<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>{name}</title>
  <style>
    body {{
      margin: 0;
      padding: 20px;
      background: #ffffff;
      display: flex;
      justify-content: center;
      align-items: center;
    }}
    svg {{
      border: 1px solid #e2e8f0;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }}
  </style>
</head>
<body>
  {svg_content}
</body>
</html>'''
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html_content)

        cmd = [
            "/home/jansky/.local/bin/google-chrome",
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            f"--window-size={w+60},{h+80}",
            f"--screenshot={png_file}",
            html_file
        ]
        subprocess.run(cmd, check=True)
        print(f"Generated clean PNG screenshot: {png_file}")

        # Copy to public/flow_screenshots & brain directory
        shutil.copy(png_file, os.path.join(public_dir, f"{name}.png"))
        shutil.copy(svg_file, os.path.join(public_dir, f"{name}.svg"))
        shutil.copy(png_file, os.path.join(brain_dir, f"{name}.png"))

    print("All screenshots successfully regenerated, copied to public, and saved to brain directory!")

if __name__ == "__main__":
    main()
