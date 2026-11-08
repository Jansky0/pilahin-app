# Bab 3.3 Perancangan Wireframe Antarmuka Pengguna (UI Wireframe)

Bagian ini menguraikan secara mendalam mengenai rancangan kerangka antarmuka (*wireframe*) sistem **Pilah.in**, mencakup **arsitektur tata letak (*layout*)**, **hierarki visual**, serta **fungsi operasional dari setiap komponen antarmuka**.

Wireframe ini dirancang dengan prinsip **Mobile-First Responsive Design** dan **Human-Centered Design (HCD)** untuk memastikan kemudahan adopsi oleh warga dari berbagai kelompok usia.

---

````carousel
![Wireframe 1: Layar Masuk / Login](/home/jansky/.gemini/antigravity-cli/brain/aee97e02-8282-4ad4-be88-03497eee84f2/uploaded_media_0_1793538147380.jpg)
<!-- slide -->
![Wireframe 2: Pendaftaran Akun - Langkah 1](/home/jansky/.gemini/antigravity-cli/brain/aee97e02-8282-4ad4-be88-03497eee84f2/uploaded_media_1_1793538147380.jpg)
<!-- slide -->
![Wireframe 3: Modal Verifikasi OTP WhatsApp](/home/jansky/.gemini/antigravity-cli/brain/aee97e02-8282-4ad4-be88-03497eee84f2/uploaded_media_2_1793538147380.jpg)
<!-- slide -->
![Wireframe 4: Pembuatan PIN Saldo 6-Digit - Langkah 2](/home/jansky/.gemini/antigravity-cli/brain/aee97e02-8282-4ad4-be88-03497eee84f2/uploaded_media_3_1793538147380.jpg)
<!-- slide -->
![Wireframe 5: Beranda Utama Warga (Citizen Dashboard)](/home/jansky/.gemini/antigravity-cli/brain/aee97e02-8282-4ad4-be88-03497eee84f2/uploaded_media_4_1793538147380.jpg)
````

---

## 3.3.1 Layar Masuk (Login Screen)

### A. Struktur dan Tata Letak (Layout)
Layar masuk menggunakan tata letak **Single-Column Center-Aligned** yang berorientasi vertikal. Konten ditempatkan di tengah layar dengan margin samping yang konsisten untuk memberikan kenyamanan fokus visual (*visual focus*) saat pengguna mengetik kredensial.

### B. Elemen Desain dan Fungsinya
1. **Top Navigation Bar:**
   - *Logo Pilah.in:* Menegaskan identitas merek (*brand identity*).
   - *Tombol "Bantuan?":* Membuka panduan bantuan cepat jika pengguna mengalami kendala teknis saat masuk.
2. **Hero Identity & Segmented Control:**
   - *Placeholder Ilustrasi/Avatar:* Elemen visual ramah pengguna.
   - *Judul "Masuk ke Pilah.in":* Menandai fungsi halaman secara eksplisit.
   - *Tab Segmentasi [Nomor HP] \| [Email]:* Memberikan fleksibilitas metode identifikasi akun (default mengarah ke Nomor HP WhatsApp).
3. **Formulir Kredensial:**
   - *Input Nomor WhatsApp / HP:* Dilengkapi kode negara `+62` dan penanda status `Wajib` untuk memitigasi kesalahan format pengetikan nomor.
   - *Input PIN Transaksi 6-Digit:* Menyamarkan input karakter (`••••••`) demi privasi dan dilengkapi tautan `Lupa PIN?` sebagai alur pemulihan (*recovery flow*).
4. **Call-to-Action (CTA) Hierarchy:**
   - *Tombol Utama [Masuk] (Solid Dark):* Tombol aksi primer berkontras tinggi untuk mengirimkan data autentikasi.
   - *Tombol Sekunder [Masuk via WhatsApp OTP] (Outline Button):* Pilihan masuk alternatif tanpa perlu mengingat PIN bagi pengguna awam.
5. **Conversion Card & Footer:**
   - *Tautan Pendaftaran Mitra:* Gerbang pemisahan bagi pihak pengelola sampah/pengepul.
   - *Kartu Ajakan Daftar:* Kotak terpisah `Belum punya akun Pilah.in? [Daftar]` untuk mengonversi warga baru.
   - *Legal & Information Links:* Tautan kebijakan privasi, syarat ketentuan, dan FAQ.

---

## 3.3.2 Layar Pendaftaran Akun — Langkah 1: Informasi Pengguna

### A. Struktur dan Tata Letak (Layout)
Mengadopsi pola **Progressive Disclosure (Form Wizard 2-Langkah)**. Pendekatan ini memecah formulir pendaftaran panjang menjadi dua tahap terpisah agar tidak membebani kapasitas kognitif pengguna (*prevent form fatigue*).

### B. Elemen Desain dan Fungsinya
1. **Step Indicator Header:**
   - *Badge "Langkah 1 dari 2":* Menampilkan transparansi tahapan registrasi.
   - *Tombol Tutup (X):* Memberi kontrol penuh kepada pengguna untuk membatalkan pendaftaran.
   - *Subjudul:* "Registrasi Warga TPS3R & Bank Sampah Digital" menegaskan keterkaitan sistem dengan fasilitas pengolahan sampah lingkungan.
2. **Card Kontainer "1. INFORMASI PENGGUNA":**
   - *Nama Lengkap Sesuai KTP:* Memastikan validitas nama warga demi keamanan pencairan saldo rekening bank/e-wallet nantinya.
   - *Nomor WhatsApp Aktif:* Menjadi saluran verifikasi OTP dan komunikasi kurir armada jemput.
   - *Alamat Email Aktif:* Opsional sebagai kanal bukti transaksi digital (*e-receipt*).
   - *Alamat Domisili / Tempat Tinggal (Text Area):* Mengumpulkan data lokasi tempat tinggal warga secara presisi untuk mempermudah navigasi penjemputan armada Tossa.
3. **Persetujuan Regulasi & Tombol Aksi:**
   - *Checkbox Syarat & Ketentuan:* Memenuhi kepatuhan perlindungan data pribadi.
   - *Tombol Utama [Lanjut ke Pembuatan PIN →]:* Tombol aksi tebal yang membawa pengguna ke proses verifikasi OTP sebelum menuju langkah 2.
   - *Tautan Kembali ke Login:* Navigasi cepat jika pengguna ternyata sudah memiliki akun.

---

## 3.3.3 Modal Verifikasi Nomor WhatsApp (OTP Bottom Sheet)

### A. Struktur dan Tata Letak (Layout)
Menggunakan komponen **Bottom Sheet Modal** dengan efek *dimmed background overlay* (scrim). Struktur ini mempertahankan konteks layar formulir di latar belakang, sehingga pengguna memahami bahwa proses verifikasi ini adalah bagian langsung dari tahapan pengisian data sebelumnya.

### B. Elemen Desain dan Fungsinya
1. **Sheet Header:**
   - *Drag Handle Bar:* Indikator visual interaksi modal responsif.
   - *Ikon & Tombol Tutup (X):* Memungkinkan pembatalan kembali ke pengubahan data.
2. **Instruksi Pengiriman OTP:**
   - Menampilkan nomor telepon target secara eksplisit (`+62 812-3456-7890`) agar pengguna dapat langsung memverifikasi kebenaran nomor yang dituju.
3. **6-Digit OTP Box Grid:**
   - 6 kotak input angka terpisah dengan *auto-advance focus* saat angka diketikkan, mempermudah keterbacaan kode verifikasi.
4. **State Feedback & Countdown Timer:**
   - *Label "Kirim ulang dalam 00:45":* Mencegah spam permintaan OTP berulang (*rate-limiting protection*).
   - *Tautan "Salah nomor? Ubah Nomor WhatsApp":* Jalur darurat jika pengguna keliru menginput nomor handphone di layar awal.
5. **Tombol CTA [Verifikasi & Lanjutkan →]:**
   - Memvalidasi kode ke sistem server dan otomatis mengarahkan ke Langkah 2 jika valid.

---

## 3.3.4 Layar Pembuatan PIN Transaksi — Langkah 2 dari 2

### A. Struktur dan Tata Letak (Layout)
Menggunakan **Custom Numeric Keypad Layout** yang terisolasi dari keyboard bawaan OS. Hal ini dirancang untuk memberikan pengalaman transaksi finansial yang aman, konsisten, dan meminimalkan interferensi *autofill* yang tidak diinginkan.

### B. Elemen Desain dan Fungsinya
1. **Security Context Callout:**
   - *Kartu "Proteksi Finansial Sirkular" (Ikon Gembok):* Memberi pemahaman kritis kepada pengguna bahwa PIN 6 digit ini bertindak sebagai otorisasi pemotongan dan penarikan saldo rupiah nyata (bukan sekadar kata sandi akun).
2. **Masked PIN Indicator:**
   - 6 lingkaran status (*bullet indicators*) yang terisi secara visual seiring angka ditekan.
   - *Helper text:* Peringatan edukatif untuk tidak menggunakan kombinasi tanggal lahir.
3. **Custom On-Screen Keypad (0-9):**
   - Tombol-tombol numerik berukuran besar (*large touch target*) sesuai standar ergonomi sentuhan jari (*thumb-friendly*).
   - Dilengkapi slot integrasi *Biometrik (Sidik Jari)* di pojok kiri bawah dan tombol *Backspace (Hapus)* di pojok kanan bawah.
4. **Tombol Final [Selesaikan & Buat Akun →]:**
   - Mengenkripsi PIN secara satu arah (*one-way hash*), merampungkan sesi pendaftaran, dan langsung menerbitkan sesi aktif menuju beranda.

---

## 3.3.5 Beranda Utama Warga (Citizen Dashboard Home Feed)

### A. Struktur dan Tata Letak (Layout)
Menerapkan arsitektur **Vertical Content Flow** yang dipadukan dengan **Sticky Bottom Navigation Bar**. Tata letak ini membagi dasbor menjadi beberapa zona prioritas hierarkis: *Hero Balance $\rightarrow$ Quick Actions $\rightarrow$ AI Access $\rightarrow$ Live Tracking $\rightarrow$ Commodity Index $\rightarrow$ Ecological Impact*.

### B. Elemen Desain dan Fungsinya
1. **Top Bar & Profil Warga:**
   - *Logo Pilah.in & Status "Warga Terverifikasi":* Membangun kredibilitas dan rasa percaya.
   - *Location Breadcrumb ("Kelurahan Cilandak Barat >"):* Menunjukkan basis wilayah layanan operasional bank sampah / mitra yang melayani.
   - *Avatar Profil & Sapaan Ramah:* Personalisasi antarmuka.
2. **Hero Balance Card (Kartu Saldo Daur Ulang):**
   - Menggunakan warna latar gelap kontras (*high-contrast dark card*) sebagai titik fokus visual (*focal point*).
   - *Indikator Status: "✓ Siap Ditarik"* menegaskan bahwa saldo adalah uang tunai likuid, bukan poin tertahan.
   - *Nominal Saldo (Rp 148.500):* Ditampilkan dengan tipografi besar dan tegas.
   - *Sub-info: Total Terkumpul (24.5 kg)* dan tombol pintas `Kelola Saldo >`.
3. **Quick Action Grid (4 Tombol Aksi Cepat):**
   - `[Setor]`: Membuka formulir tiket penjemputan armada atau drop-off mandiri.
   - `[Tarik]`: Membuka formulir pencairan dana ke e-wallet (GoPay/DANA).
   - `[Toko]`: Mengakses katalog produk upcycle (pupuk kompos olahan warga).
   - `[Riwayat]`: Menampilkan mutasi transaksi timbangan dan saldo.
4. **Banner SnapSort AI Detector [BETA]:**
   - Akses satu ketukan (*one-tap access*) menuju fitur unggulan kamera pemindai sampah pintar.
5. **Live Tracking Card (Lacak Jejak & Tiket Sampah):**
   - Menampilkan status tiket berjalan secara *real-time* (`PLH-849281`, Jemput Rumah, 11 kg, Budi Tossa #04).
   - *Stepper Timeline Vertikal (4 Tahapan):*
     1. Permintaan Jemput Diterima (09:30 WIB)
     2. Kurir Meluncur ke Alamat Rumah (10:05 WIB)
     3. Penimbangan Digital di Tempat (Est. 10:25 WIB)
     4. Saldo Mengendap Cair Otomatis (Est. 10:30 WIB)
   - Dilengkapi navigasi kartu geser (*carousel*) jika warga memiliki lebih dari 1 tiket aktif.
6. **Indeks Harga Komoditas Sampah Realtime:**
   - Menampilkan harga acuan pasar per kg secara transparan (Kardus Rp 1.800, PET Rp 3.500, Jelantah Rp 7.000, Organik Rp 800, Kaleng Rp 5.500).
   - Indikator tren fluktuasi harga (▲ +5%, ▲ +8%, Stabil) yang diperbarui harian pukul 07:00 WIB, memotivasi warga untuk menyetor saat harga tinggi.
7. **Kartu Dampak Sirkular (Gamifikasi Ekologi):**
   - Memberikan kepuasan emosional (*intrinsic reward*) melalui metrik nyata: 24.5 kg sampah terselamatkan, 3 pohon diasuh, dan 38.2 kg reduksi emisi karbon.
   - Dilengkapi tombol cetak `[Sertifikat]` kontribusi lingkungan.
8. **Fixed Bottom Navigation Bar:**
   - 4 tab navigasi persisten: `[Beranda]` (aktif), `[Setor]`, `[Toko]`, dan `[Dompet]` yang dirancang berada di zona jangkauan ibu jari (*thumb zone*).
