import os
import subprocess

def create_svg_phase1():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 890" width="1000" height="890" style="background:#ffffff; font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;">
  <defs>
    <marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#000000" />
    </marker>
  </defs>

  <!-- Title -->
  <text x="500" y="32" text-anchor="middle" font-size="16" font-weight="bold" fill="#000000">FASE 1: REGISTRASI, VERIFIKASI OTP &amp; LOGIN</text>
  <text x="500" y="52" text-anchor="middle" font-size="11" fill="#444444">Alur Granular 1 Proses per Kotak — Tanpa Fast Demo — Monochrome</text>

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

  <!-- Connectors from Decision -->
  <!-- Left to Register -->
  <path d="M 420 230 L 230 230 L 230 278" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="315" y="222" text-anchor="middle" font-size="10" fill="#000000">Belum (Daftar)</text>

  <!-- Right to Login -->
  <path d="M 580 230 L 760 230 L 760 278" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="680" y="222" text-anchor="middle" font-size="10" fill="#000000">Sudah (Masuk)</text>

  <!-- ================= LEFT: REGISTER ================= -->
  <!-- Step 1: Role -->
  <rect x="130" y="280" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="230" y="297" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Pilih Peran Akun</text>
  <text x="230" y="311" text-anchor="middle" font-size="9" fill="#444444">Warga Penyetor atau Mitra Bank Sampah</text>

  <line x1="230" y1="320" x2="230" y2="343" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <!-- Step 2: Input Data -->
  <rect x="130" y="345" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="230" y="362" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Input Data Diri &amp; Akun</text>
  <text x="230" y="376" text-anchor="middle" font-size="9" fill="#444444">Nama, No WhatsApp, Kata Sandi</text>

  <line x1="230" y1="385" x2="230" y2="408" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <!-- Decision: Valid? -->
  <polygon points="230,410 295,435 230,460 165,435" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="230" y="432" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Format Data</text>
  <text x="230" y="444" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Valid?</text>

  <!-- Sad: Data invalid -->
  <path d="M 165 435 L 80 435" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="120" y="428" text-anchor="middle" font-size="9" fill="#000000">Tidak</text>
  <rect x="10" y="415" width="70" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="45" y="432" text-anchor="middle" font-size="9" font-weight="bold" fill="#000000">Pesan Eror</text>
  <text x="45" y="444" text-anchor="middle" font-size="8" fill="#444444">Validasi</text>
  <!-- Loop back -->
  <path d="M 45 415 L 45 365 L 128 365" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3" marker-end="url(#arr)"/>

  <!-- Valid: Kirim OTP -->
  <line x1="230" y1="460" x2="230" y2="488" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="245" y="475" font-size="9" fill="#000000">Ya</text>

  <rect x="130" y="490" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="230" y="507" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Kirim Kode OTP ke WhatsApp</text>
  <text x="230" y="521" text-anchor="middle" font-size="9" fill="#444444">Sistem kirim 6 digit verifikasi</text>

  <line x1="230" y1="530" x2="230" y2="553" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <!-- Step 3: Input OTP -->
  <rect x="130" y="555" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="230" y="572" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Input Kode OTP 6 Digit</text>
  <text x="230" y="586" text-anchor="middle" font-size="9" fill="#444444">Ketik kode yang diterima di WA</text>

  <line x1="230" y1="595" x2="230" y2="618" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <!-- Decision: OTP Cocok? -->
  <polygon points="230,620 295,645 230,670 165,645" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="230" y="642" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Kode OTP</text>
  <text x="230" y="654" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Cocok?</text>

  <!-- Sad OTP -->
  <path d="M 165 645 L 80 645" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="120" y="638" text-anchor="middle" font-size="9" fill="#000000">Salah</text>
  <rect x="10" y="625" width="70" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="45" y="642" text-anchor="middle" font-size="9" font-weight="bold" fill="#000000">OTP Salah</text>
  <text x="45" y="654" text-anchor="middle" font-size="8" fill="#444444">Kirim Ulang</text>
  <path d="M 45 625 L 45 510 L 128 510" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3" marker-end="url(#arr)"/>

  <!-- OTP Cocok -->
  <line x1="230" y1="670" x2="230" y2="698" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="245" y="685" font-size="9" fill="#000000">Cocok</text>

  <!-- Step 4: Alamat -->
  <rect x="130" y="700" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="230" y="717" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Input Alamat &amp; Patokan</text>
  <text x="230" y="731" text-anchor="middle" font-size="9" fill="#444444">Jalan, RT/RW, akses motor Tossa</text>

  <line x1="230" y1="740" x2="230" y2="763" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <!-- Step 5: PIN -->
  <rect x="130" y="765" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="230" y="782" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Buat 6 Digit PIN Transaksi</text>
  <text x="230" y="796" text-anchor="middle" font-size="9" fill="#444444">Keamanan belanja &amp; tarik tunai</text>

  <line x1="230" y1="805" x2="230" y2="828" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <!-- Register Success -->
  <rect x="130" y="830" width="200" height="35" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="230" y="852" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Registrasi Berhasil Selesai</text>

  <!-- ================= RIGHT: LOGIN ================= -->
  <!-- Step 1: Input ID -->
  <rect x="660" y="280" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="760" y="297" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Input No. WhatsApp / Email</text>
  <text x="760" y="311" text-anchor="middle" font-size="9" fill="#444444">Ketik identitas akun terdaftar</text>

  <line x1="760" y1="320" x2="760" y2="348" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <!-- Decision: Lupa Pass? -->
  <polygon points="760,350 830,375 760,400 690,375" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="760" y="372" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Lupa Kata</text>
  <text x="760" y="384" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Sandi?</text>

  <!-- Forgot Password Subflow -->
  <path d="M 830 375 L 890 375 L 890 418" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="860" y="367" text-anchor="middle" font-size="9" fill="#000000">Ya (Lupa)</text>

  <rect x="830" y="420" width="120" height="38" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="890" y="436" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Minta OTP Reset</text>
  <text x="890" y="449" text-anchor="middle" font-size="8" fill="#444444">Kirim via WA</text>

  <line x1="890" y1="458" x2="890" y2="483" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="830" y="485" width="120" height="38" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="890" y="501" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Input OTP Reset</text>
  <text x="890" y="514" text-anchor="middle" font-size="8" fill="#444444">Verifikasi kode</text>

  <line x1="890" y1="523" x2="890" y2="548" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="830" y="550" width="120" height="38" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="890" y="566" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Input Sandi Baru</text>
  <text x="890" y="579" text-anchor="middle" font-size="8" fill="#444444">Simpan sandi</text>

  <!-- Loop back to Login ID -->
  <path d="M 950 569 L 980 569 L 980 300 L 862 300" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3" marker-end="url(#arr)"/>
  <text x="965" y="440" font-size="8" fill="#000000" transform="rotate(90 965,440)">Login Sandi Baru</text>

  <!-- Normal Login Subflow -->
  <line x1="730" y1="390" x2="730" y2="433" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="710" y="415" font-size="9" fill="#000000">Ingat</text>

  <rect x="650" y="435" width="160" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="730" y="452" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Input Kata Sandi</text>
  <text x="730" y="466" text-anchor="middle" font-size="9" fill="#444444">Ketik kata sandi akun</text>

  <line x1="730" y1="475" x2="730" y2="503" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <!-- Decision: Auth Match? -->
  <polygon points="730,505 795,530 730,555 665,530" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="730" y="527" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Kredensial</text>
  <text x="730" y="539" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Cocok?</text>

  <!-- Sad Auth -->
  <path d="M 665 530 L 600 530" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="635" y="522" text-anchor="middle" font-size="9" fill="#000000">Salah</text>
  <rect x="520" y="510" width="80" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="560" y="527" text-anchor="middle" font-size="9" font-weight="bold" fill="#000000">Sandi Salah</text>
  <text x="560" y="539" text-anchor="middle" font-size="8" fill="#444444">Ketik Ulang</text>
  <path d="M 560 510 L 560 455 L 648 455" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3" marker-end="url(#arr)"/>

  <!-- Happy Auth -->
  <line x1="730" y1="555" x2="730" y2="608" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="745" y="585" font-size="9" fill="#000000">Cocok</text>

  <rect x="640" y="610" width="180" height="35" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="730" y="632" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Login Berhasil Masuk</text>

  <!-- CONVERGENCE TO END -->
  <path d="M 230 865 L 230 875 L 408 875" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <path d="M 730 645 L 730 875 L 592 875" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="410" y="855" width="180" height="34" rx="17" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
  <text x="500" y="876" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Masuk ke Beranda</text>
</svg>'''
    return svg


def create_svg_phase2():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 680" width="920" height="680" style="background:#ffffff; font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;">
  <defs>
    <marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#000000" />
    </marker>
  </defs>

  <text x="460" y="32" text-anchor="middle" font-size="16" font-weight="bold" fill="#000000">FASE 2: BERANDA WARGA &amp; DETEKSI SAMPAH (SNAPSORT AI)</text>
  <text x="460" y="52" text-anchor="middle" font-size="11" fill="#444444">Pemantauan Saldo Mengendap &amp; Klasifikasi Material Kamera — Monochrome</text>

  <rect x="370" y="70" width="180" height="34" rx="17" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
  <text x="460" y="92" text-anchor="middle" font-size="12" font-weight="bold" fill="#000000">Mulai: Beranda Warga</text>

  <line x1="460" y1="104" x2="460" y2="128" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="340" y="130" width="240" height="42" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="460" y="148" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Cek Saldo Mengendap &amp; Riwayat</text>
  <text x="460" y="162" text-anchor="middle" font-size="9" fill="#444444">Pantau saldo rupiah siap tarik &amp; panduan pilah</text>

  <line x1="460" y1="172" x2="460" y2="198" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <polygon points="460,200 540,230 460,260 380,230" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="460" y="227" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Gunakan AI</text>
  <text x="460" y="239" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Scanner?</text>

  <!-- Left: Manual -->
  <path d="M 380 230 L 220 230 L 220 288" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="290" y="222" text-anchor="middle" font-size="10" fill="#000000">Tidak (Manual)</text>

  <rect x="120" y="290" width="200" height="42" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="220" y="308" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Buka Tab 'Setor Sampah'</text>
  <text x="220" y="322" text-anchor="middle" font-size="9" fill="#444444">Lanjut pilih sampah secara manual</text>

  <!-- Right: AI -->
  <path d="M 540 230 L 680 230 L 680 288" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="610" y="222" text-anchor="middle" font-size="10" fill="#000000">Ya (SnapSort AI)</text>

  <rect x="580" y="290" width="200" height="42" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="680" y="308" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Buka Tab 'SnapSort AI'</text>
  <text x="680" y="322" text-anchor="middle" font-size="9" fill="#444444">Akses kamera pemindai sampah</text>

  <line x1="680" y1="332" x2="680" y2="358" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="580" y="360" width="200" height="42" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="680" y="378" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Arahkan Kamera &amp; Ambil Foto</text>
  <text x="680" y="392" text-anchor="middle" font-size="9" fill="#444444">Posisikan sampah di frame &amp; klik pindai</text>

  <line x1="680" y1="402" x2="680" y2="428" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <!-- Decision: Hasil Deteksi -->
  <polygon points="680,430 760,455 680,480 600,455" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="680" y="452" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Hasil Analisis</text>
  <text x="680" y="464" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Material?</text>

  <!-- Sad 1: B3 -->
  <path d="M 760 455 L 830 455 L 830 508" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="795" y="447" text-anchor="middle" font-size="9" fill="#000000">Tercemar/B3</text>
  <rect x="760" y="510" width="140" height="42" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="830" y="528" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Limbah B3</text>
  <text x="830" y="541" text-anchor="middle" font-size="8" fill="#444444">Tolak, buang ke TPS B3</text>

  <!-- Sad 2: Blur -->
  <path d="M 600 455 L 510 455 L 510 508" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="555" y="447" text-anchor="middle" font-size="9" fill="#000000">Buram/Gelap</text>
  <rect x="440" y="510" width="140" height="42" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="510" y="528" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Objek Tak Terbaca</text>
  <text x="510" y="541" text-anchor="middle" font-size="8" fill="#444444">Ambil foto ulang</text>
  <path d="M 440 531 L 410 531 L 410 381 L 578 381" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3" marker-end="url(#arr)"/>

  <!-- Valid Material -->
  <line x1="680" y1="480" x2="680" y2="508" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="695" y="498" font-size="9" fill="#000000">Layak</text>

  <rect x="600" y="510" width="150" height="42" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="675" y="528" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Deteksi Material Valid</text>
  <text x="675" y="541" text-anchor="middle" font-size="8" fill="#444444">PET 96%, Rp 3.500/kg</text>

  <line x1="675" y1="552" x2="675" y2="578" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="580" y="580" width="190" height="38" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="675" y="597" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Klik 'Langsung Setor'</text>
  <text x="675" y="609" text-anchor="middle" font-size="8" fill="#444444">Auto-centang kategori di Tab Setor</text>

  <!-- Convergence to End -->
  <path d="M 220 332 L 220 645 L 348 645" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <path d="M 675 618 L 675 645 L 572 645" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="350" y="630" width="220" height="34" rx="17" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
  <text x="460" y="652" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Lanjut ke Halaman Setor Sampah</text>
</svg>'''
    return svg


def create_svg_phase3():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 740" width="950" height="740" style="background:#ffffff; font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;">
  <defs>
    <marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#000000" />
    </marker>
  </defs>

  <text x="475" y="32" text-anchor="middle" font-size="16" font-weight="bold" fill="#000000">FASE 3: PENGAJUAN PENYETORAN SAMPAH</text>
  <text x="475" y="52" text-anchor="middle" font-size="11" fill="#444444">Kalkulasi Ongkir Jemput Tossa 10% vs Drop-off 0% Mandiri — Monochrome</text>

  <rect x="375" y="70" width="200" height="34" rx="17" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
  <text x="475" y="92" text-anchor="middle" font-size="12" font-weight="bold" fill="#000000">Mulai: Tab Setor Sampah</text>

  <line x1="475" y1="104" x2="475" y2="128" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="360" y="130" width="230" height="42" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="475" y="148" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Pilih Kategori &amp; Atur Berat (kg)</text>
  <text x="475" y="162" text-anchor="middle" font-size="9" fill="#444444">Centang sampah &amp; sesuaikan stepper kg</text>

  <line x1="475" y1="172" x2="475" y2="198" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <polygon points="475,200 555,225 475,250 395,225" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="475" y="222" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Kategori &amp; Berat</text>
  <text x="475" y="234" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Valid?</text>

  <!-- Sad: Empty -->
  <path d="M 395 225 L 300 225" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="350" y="217" text-anchor="middle" font-size="9" fill="#000000">Tidak</text>
  <rect x="150" y="205" width="150" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="225" y="222" text-anchor="middle" font-size="9" font-weight="bold" fill="#000000">Pesan: Pilih Sampah</text>
  <text x="225" y="235" text-anchor="middle" font-size="8" fill="#444444">Tentukan berat minimal</text>
  <path d="M 225 205 L 225 151 L 358 151" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3" marker-end="url(#arr)"/>

  <!-- Decision: Method -->
  <line x1="475" y1="250" x2="475" y2="278" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="490" y="268" font-size="9" fill="#000000">Ya</text>

  <polygon points="475,280 555,310 475,340 395,310" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="475" y="307" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Pilih Metode</text>
  <text x="475" y="319" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Setor?</text>

  <!-- ================= LEFT: JEMPUT TOSSA ================= -->
  <path d="M 395 310 L 240 310 L 240 358" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="310" y="302" text-anchor="middle" font-size="10" fill="#000000">Jemput Armada Tossa</text>

  <rect x="140" y="360" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="240" y="377" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Kalkulasi Ongkir Jemput 10%</text>
  <text x="240" y="391" text-anchor="middle" font-size="9" fill="#444444">Gross total - 10% operasional armada</text>

  <line x1="240" y1="400" x2="240" y2="428" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="140" y="430" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="240" y="447" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Pilih Alamat &amp; Cek Patokan</text>
  <text x="240" y="461" text-anchor="middle" font-size="9" fill="#444444">Pastikan akses teras dapat dilalui motor</text>

  <line x1="240" y1="470" x2="240" y2="498" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <polygon points="240,500 305,525 240,550 175,525" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="240" y="522" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Alamat</text>
  <text x="240" y="534" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Lengkap?</text>

  <!-- Edit address -->
  <path d="M 175 525 L 90 525" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="130" y="517" text-anchor="middle" font-size="9" fill="#000000">Kurang</text>
  <rect x="10" y="505" width="80" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="50" y="522" text-anchor="middle" font-size="9" font-weight="bold" fill="#000000">Ubah Alamat</text>
  <text x="50" y="535" text-anchor="middle" font-size="8" fill="#444444">Ketik patokan</text>
  <path d="M 50 505 L 50 450 L 138 450" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3" marker-end="url(#arr)"/>

  <!-- Submit Tossa -->
  <line x1="240" y1="550" x2="240" y2="578" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="255" y="568" font-size="9" fill="#000000">Lengkap</text>

  <rect x="140" y="580" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="240" y="597" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Klik 'Ajukan Penjemputan'</text>
  <text x="240" y="611" text-anchor="middle" font-size="9" fill="#444444">Kirim jadwal jemputan ke kurir</text>

  <!-- ================= RIGHT: DROP-OFF ================= -->
  <path d="M 555 310 L 710 310 L 710 358" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="640" y="302" text-anchor="middle" font-size="10" fill="#000000">Antar Sendiri (Drop-off)</text>

  <rect x="610" y="360" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="710" y="377" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Kalkulasi Drop-off (0% Ongkir)</text>
  <text x="710" y="391" text-anchor="middle" font-size="9" fill="#444444">Ongkos kirim Rp 0 (100% saldo utuh)</text>

  <line x1="710" y1="400" x2="710" y2="448" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="610" y="450" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="710" y="467" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Pilih Pos / Drop Point Mitra</text>
  <text x="710" y="481" text-anchor="middle" font-size="9" fill="#444444">Bank Sampah / TPS3R terdekat</text>

  <line x1="710" y1="490" x2="710" y2="578" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="610" y="580" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="710" y="597" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Klik 'Buat Tiket Mandiri'</text>
  <text x="710" y="611" text-anchor="middle" font-size="9" fill="#444444">Penerbitan tiket drop-off ke pos</text>

  <!-- ================= MERGE: TIKET TERBIT ================= -->
  <path d="M 240 620 L 240 655 L 368 655" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <path d="M 710 620 L 710 655 L 582 655" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="370" y="635" width="210" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="475" y="652" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Tiket Digital QR Terbit</text>
  <text x="475" y="666" text-anchor="middle" font-size="9" fill="#444444">ID: PLH-XXXXXX, Status: Menunggu</text>

  <line x1="475" y1="675" x2="475" y2="703" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="365" y="705" width="220" height="30" rx="15" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
  <text x="475" y="725" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Selesai: Siap Ditimbang</text>
</svg>'''
    return svg


def create_svg_phase4():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 740" width="950" height="740" style="background:#ffffff; font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;">
  <defs>
    <marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#000000" />
    </marker>
  </defs>

  <text x="475" y="32" text-anchor="middle" font-size="16" font-weight="bold" fill="#000000">FASE 4: OPERASIONAL TIMBANG LAPANGAN &amp; VERIFIKASI MITRA</text>
  <text x="475" y="52" text-anchor="middle" font-size="11" fill="#444444">Penimbangan Digital Bersama &amp; Validasi Tiket di Portal Mitra Pengelola — Monochrome</text>

  <rect x="375" y="70" width="200" height="34" rx="17" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
  <text x="475" y="92" text-anchor="middle" font-size="12" font-weight="bold" fill="#000000">Mulai: Tiket Digital Aktif</text>

  <line x1="475" y1="104" x2="475" y2="128" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <polygon points="475,130 555,160 475,190 395,160" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="475" y="157" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Jenis Penyetoran</text>
  <text x="475" y="169" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Lapangan?</text>

  <!-- Left: Jemput Tossa -->
  <path d="M 395 160 L 240 160 L 240 208" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="315" y="152" text-anchor="middle" font-size="10" fill="#000000">Jemput Tossa</text>

  <rect x="140" y="210" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="240" y="227" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Motor Tossa Tiba di Alamat</text>
  <text x="240" y="241" text-anchor="middle" font-size="9" fill="#444444">Kurir cek patokan &amp; kontak WA</text>

  <line x1="240" y1="250" x2="240" y2="278" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <polygon points="240,280 305,305 240,330 175,305" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="240" y="302" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Warga Ada di</text>
  <text x="240" y="314" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Lokasi?</text>

  <path d="M 175 305 L 90 305" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="130" y="297" text-anchor="middle" font-size="9" fill="#000000">Tidak</text>
  <rect x="10" y="285" width="80" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="50" y="302" text-anchor="middle" font-size="9" font-weight="bold" fill="#000000">Jadwal Ulang</text>
  <text x="50" y="315" text-anchor="middle" font-size="8" fill="#444444">Tiket tetap aktif</text>

  <line x1="240" y1="330" x2="240" y2="358" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="255" y="348" font-size="9" fill="#000000">Ada</text>

  <rect x="140" y="360" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="240" y="377" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Timbang Digital di Teras</text>
  <text x="240" y="391" text-anchor="middle" font-size="9" fill="#444444">Timbangan gantung disaksikan bersama</text>

  <!-- Right: Drop-off Mandiri -->
  <path d="M 555 160 L 710 160 L 710 208" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="635" y="152" text-anchor="middle" font-size="10" fill="#000000">Antar Sendiri</text>

  <rect x="610" y="210" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="710" y="227" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Warga Bawa Sampah ke Pos</text>
  <text x="710" y="241" text-anchor="middle" font-size="9" fill="#444444">Tiba di Bank Sampah / TPS3R Mitra</text>

  <line x1="710" y1="250" x2="710" y2="278" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <polygon points="710,280 775,305 710,330 645,305" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="710" y="302" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Pos Sedang</text>
  <text x="710" y="314" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Buka?</text>

  <path d="M 775 305 L 850 305" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="810" y="297" text-anchor="middle" font-size="9" fill="#000000">Tutup</text>
  <rect x="850" y="285" width="90" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="895" y="302" text-anchor="middle" font-size="9" font-weight="bold" fill="#000000">Pos Tutup</text>
  <text x="895" y="315" text-anchor="middle" font-size="8" fill="#444444">Kembali besok</text>

  <line x1="710" y1="330" x2="710" y2="358" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="725" y="348" font-size="9" fill="#000000">Buka</text>

  <rect x="610" y="360" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="710" y="377" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Petugas Timbang di Pos</text>
  <text x="710" y="391" text-anchor="middle" font-size="9" fill="#444444">Pengukuran timbangan digital pos</text>

  <!-- ================= PORTAL MITRA ================= -->
  <path d="M 240 400 L 240 435 L 368 435" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <path d="M 710 400 L 710 435 L 582 435" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="370" y="415" width="210" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="475" y="432" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Buka Portal Mitra Pengelola</text>
  <text x="475" y="446" text-anchor="middle" font-size="9" fill="#444444">Petugas masuk ke dasbor operator</text>

  <line x1="475" y1="455" x2="475" y2="483" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="370" y="485" width="210" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="475" y="502" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Input Nomor Tiket &amp; Bobot Riil</text>
  <text x="475" y="516" text-anchor="middle" font-size="9" fill="#444444">Ketik PLH-XXXXXX &amp; kg timbangan</text>

  <line x1="475" y1="525" x2="475" y2="553" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="370" y="555" width="210" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="475" y="572" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Verifikasi Data Penimbangan</text>
  <text x="475" y="586" text-anchor="middle" font-size="9" fill="#444444">Sistem kalkulasi nilai rupiah bersih</text>

  <line x1="475" y1="595" x2="475" y2="623" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="355" y="625" width="240" height="42" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="475" y="642" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Saldo Tunai Masuk ke Dompet</text>
  <text x="475" y="656" text-anchor="middle" font-size="9" fill="#444444">Kredit instan bertambah &amp; tiket berstatus selesai</text>

  <line x1="475" y1="667" x2="475" y2="698" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="365" y="700" width="220" height="30" rx="15" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
  <text x="475" y="720" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Selesai: Saldo Siap Dipakai</text>
</svg>'''
    return svg


def create_svg_phase5():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 750" width="950" height="750" style="background:#ffffff; font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;">
  <defs>
    <marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#000000" />
    </marker>
  </defs>

  <text x="475" y="32" text-anchor="middle" font-size="16" font-weight="bold" fill="#000000">FASE 5: PEMANFAATAN SALDO LIKUID WARGA</text>
  <text x="475" y="52" text-anchor="middle" font-size="11" fill="#444444">Belanja Pupuk Kompos Sirkular vs Tarik Tunai Uang Asli ke GoPay/DANA — Monochrome</text>

  <rect x="365" y="70" width="220" height="34" rx="17" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
  <text x="475" y="92" text-anchor="middle" font-size="12" font-weight="bold" fill="#000000">Mulai: Saldo di Dompet</text>

  <line x1="475" y1="104" x2="475" y2="128" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <polygon points="475,130 555,160 475,190 395,160" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="475" y="157" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Pemanfaatan</text>
  <text x="475" y="169" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Saldo?</text>

  <!-- ================= LEFT: BELANJA TOKO ================= -->
  <path d="M 395 160 L 240 160 L 240 208" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="310" y="152" text-anchor="middle" font-size="10" fill="#000000">Belanja Upcycle</text>

  <rect x="140" y="210" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="240" y="227" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Buka Tab 'Toko Sirkular'</text>
  <text x="240" y="241" text-anchor="middle" font-size="9" fill="#444444">Katalog produk olahan pupuk warga</text>

  <line x1="240" y1="250" x2="240" y2="278" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="140" y="280" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="240" y="297" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Pilih Pupuk Kompos (Rp 18k)</text>
  <text x="240" y="311" text-anchor="middle" font-size="9" fill="#444444">Pupuk kompos super 5kg olahan mitra</text>

  <line x1="240" y1="320" x2="240" y2="348" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <polygon points="240,350 305,375 240,400 175,375" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="240" y="372" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Saldo Cukup</text>
  <text x="240" y="384" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">(&gt;= 18k)?</text>

  <path d="M 175 375 L 100 375" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="140" y="367" text-anchor="middle" font-size="9" fill="#000000">Tidak</text>
  <rect x="10" y="355" width="90" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="55" y="372" text-anchor="middle" font-size="9" font-weight="bold" fill="#000000">Saldo Kurang</text>
  <text x="55" y="385" text-anchor="middle" font-size="8" fill="#444444">Setor lagi</text>

  <line x1="240" y1="400" x2="240" y2="428" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="255" y="418" font-size="9" fill="#000000">Cukup</text>

  <rect x="140" y="430" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="240" y="447" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Input PIN Transaksi 6 Digit</text>
  <text x="240" y="461" text-anchor="middle" font-size="9" fill="#444444">Otorisasi pemotongan saldo belanja</text>

  <line x1="240" y1="470" x2="240" y2="498" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="140" y="500" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="240" y="517" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Pembelian Kompos Selesai</text>
  <text x="240" y="531" text-anchor="middle" font-size="9" fill="#444444">Saldo dipotong Rp 18k (Sirkular)</text>

  <!-- ================= RIGHT: TARIK TUNAI ================= -->
  <path d="M 555 160 L 710 160 L 710 208" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="635" y="152" text-anchor="middle" font-size="10" fill="#000000">Tarik Tunai</text>

  <rect x="610" y="210" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="710" y="227" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Buka Tab 'Dompet' (Tarik)</text>
  <text x="710" y="241" text-anchor="middle" font-size="9" fill="#444444">Menu pencairan saldo ke e-wallet</text>

  <line x1="710" y1="250" x2="710" y2="278" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="610" y="280" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="710" y="297" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Pilih E-Wallet &amp; Nominal</text>
  <text x="710" y="311" text-anchor="middle" font-size="9" fill="#444444">GoPay/DANA, Rp 50.000 &amp; nomor HP</text>

  <line x1="710" y1="320" x2="710" y2="348" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <polygon points="710,350 775,375 710,400 645,375" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="710" y="372" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Nominal Valid</text>
  <text x="710" y="384" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">(&gt;= 10k)?</text>

  <path d="M 775 375 L 850 375" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="810" y="367" text-anchor="middle" font-size="9" fill="#000000">Tidak</text>
  <rect x="850" y="355" width="90" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="895" y="372" text-anchor="middle" font-size="9" font-weight="bold" fill="#000000">Format Salah</text>
  <text x="895" y="385" text-anchor="middle" font-size="8" fill="#444444">Min Rp 10.000</text>
  <path d="M 895 355 L 895 300 L 812 300" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3" marker-end="url(#arr)"/>

  <line x1="710" y1="400" x2="710" y2="428" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="725" y="418" font-size="9" fill="#000000">Valid</text>

  <polygon points="710,430 775,455 710,480 645,455" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="710" y="452" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">Saldo Cukup</text>
  <text x="710" y="464" text-anchor="middle" font-size="10" font-weight="bold" fill="#000000">(&gt;= 50k)?</text>

  <path d="M 775 455 L 850 455" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="810" y="447" text-anchor="middle" font-size="9" fill="#000000">Kurang</text>
  <rect x="850" y="435" width="90" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="895" y="452" text-anchor="middle" font-size="9" font-weight="bold" fill="#000000">Saldo Kurang</text>
  <text x="895" y="465" text-anchor="middle" font-size="8" fill="#444444">Batalkan</text>

  <line x1="710" y1="480" x2="710" y2="508" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="725" y="498" font-size="9" fill="#000000">Cukup</text>

  <rect x="610" y="510" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="710" y="527" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Input PIN Transaksi 6 Digit</text>
  <text x="710" y="541" text-anchor="middle" font-size="9" fill="#444444">Otorisasi pencairan dana e-wallet</text>

  <line x1="710" y1="550" x2="710" y2="578" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="610" y="580" width="200" height="40" rx="4" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="710" y="597" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Uang Cair ke E-Wallet</text>
  <text x="710" y="611" text-anchor="middle" font-size="9" fill="#444444">Saldo terpotong Rp 50k (0% admin)</text>

  <!-- ================= CONVERGENCE ================= -->
  <path d="M 240 540 L 240 685 L 368 685" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>
  <path d="M 710 620 L 710 685 L 582 685" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arr)"/>

  <rect x="370" y="668" width="210" height="34" rx="17" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
  <text x="475" y="690" text-anchor="middle" font-size="11" font-weight="bold" fill="#000000">Selesai: Dampak Nyata</text>
</svg>'''
    return svg


def main():
    img_dir = "/home/jansky/pilahin-app/flow_screenshots"
    os.makedirs(img_dir, exist_ok=True)

    generators = [
        ("fase_1_registrasi_dan_login", create_svg_phase1, 1000, 890),
        ("fase_2_beranda_dan_snapsort_ai", create_svg_phase2, 920, 680),
        ("fase_3_pengajuan_setor_sampah", create_svg_phase3, 950, 740),
        ("fase_4_timbang_lapangan_dan_mitra", create_svg_phase4, 950, 740),
        ("fase_5_belanja_toko_dan_tarik_tunai", create_svg_phase5, 950, 750),
    ]

    for name, func, w, h in generators:
        svg_content = func()
        svg_file = os.path.join(img_dir, f"{name}.svg")
        png_file = os.path.join(img_dir, f"{name}.png")
        html_file = os.path.join(img_dir, f"{name}.html")

        with open(svg_file, "w", encoding="utf-8") as f:
            f.write(svg_content)

        # Wrap in a clean HTML page for 1-click screenshotting & Chromium capture
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

        # Render PNG with Chromium
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

if __name__ == "__main__":
    main()
