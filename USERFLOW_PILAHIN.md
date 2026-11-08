# Userflow Pilah.in per Fase (Lengkap: Happy Path & Sad Path "Sistem Menolak")

Dokumen ini menyajikan **Userflow Lengkap Pilah.in per Fase** dengan penegasan eksplisit antara **Happy Path (Jalur Sukses)** dan **Sad Path (Sistem Menolak / Penanganan Kegagalan)** sesuai standar arsitektur sistem operasional persampahan sirkular.

---

### Karakteristik & Standar Diagram:
- ⚪ **Clean Monochrome:** Seluruh diagram menggunakan warna dasar putih, garis batas hitam, dan teks hitam bersih (*zero color clutter*).
- 📦 **1 Kotak = 1 Proses Granular:** Setiap kotak hanya merepresentasikan satu tindakan nyata pengguna atau sistem.
- 🚫 **Tanpa "Fast Demo":** Alur login dan registrasi murni melalui proses autentikasi standar (Input WhatsApp/Email $\rightarrow$ Kata Sandi / OTP / Penanganan Lupa Sandi).
- ⚠️ **Eksplisit Sad Path & Sistem Menolak:** Setiap fase memiliki *decision diamond* dan cabang *Sad Path* yang memperlihatkan respons sistem ketika syarat tidak terpenuhi (validasi gagal, limbah B3, di luar radius 3 km, kurasi fisik gagal/basah, saldo kurang, dan PIN salah 3x terkunci).
- 📸 **Sangat Mudah Di-Screenshot:** Setiap fase dipisahkan ke dalam kanvas berukuran proporsional yang pas di layar.

---

> [!TIP]
> ### 3 Cara Melihat & Mengambil Screenshot per Fase:
> 1. **Web Viewer Interaktif (Rekomendasi untuk Screenshot):**  
>    Buka **[http://localhost:3000/userflow_view.html](http://localhost:3000/userflow_view.html)** di browser. Anda dapat berpindah tab per fase dan langsung screenshot atau klik tombol **"Unduh Gambar PNG"**.
> 2. **File Draw.io Multi-Tab:**  
>    Buka **[userflow_pilahin.drawio](file:///home/jansky/pilahin-app/userflow_pilahin.drawio)** di [app.diagrams.net](https://app.diagrams.net/). Di bagian bawah terdapat 5 tab/sheet yang masing-masing berisi 1 fase.
> 3. **File Draw.io Individual per Fase:**  
>    Tersedia di folder **[drawio_phases/](file:///home/jansky/pilahin-app/drawio_phases/)**:
>    - [fase_1_registrasi_dan_login.drawio](file:///home/jansky/pilahin-app/drawio_phases/fase_1_registrasi_dan_login.drawio)
>    - [fase_2_beranda_dan_snapsort_ai.drawio](file:///home/jansky/pilahin-app/drawio_phases/fase_2_beranda_dan_snapsort_ai.drawio)
>    - [fase_3_pengajuan_setor_sampah.drawio](file:///home/jansky/pilahin-app/drawio_phases/fase_3_pengajuan_setor_sampah.drawio)
>    - [fase_4_timbang_lapangan_dan_mitra.drawio](file:///home/jansky/pilahin-app/drawio_phases/fase_4_timbang_lapangan_dan_mitra.drawio)
>    - [fase_5_belanja_toko_dan_tarik_tunai.drawio](file:///home/jansky/pilahin-app/drawio_phases/fase_5_belanja_toko_dan_tarik_tunai.drawio)

---

## Rincian & Diagram Mermaid per Fase

### Fase 1: Registrasi, Verifikasi OTP & Login (dengan Sad Path Validasi & OTP)
- **Happy Path:** Pendaftaran akun baru bertahap (Data $\rightarrow$ OTP $\rightarrow$ Alamat $\rightarrow$ PIN) dan login normal berhasil menuju Beranda Warga.
- **Sad Path (Sistem Menolak):**
  1. *Format Data Tidak Valid:* Nomor WhatsApp kurang dari 10 digit atau sandi kurang dari 6 karakter $\rightarrow$ **Sistem Menolak** & minta perbaikan.
  2. *OTP Salah / Kedaluwarsa:* Kode verifikasi 6-digit tidak cocok $\rightarrow$ **Sistem Menolak** & wajib kirim ulang OTP.
  3. *Kredensial Login Salah:* Nomor HP atau kata sandi tidak cocok dengan database $\rightarrow$ **Sistem Menolak** & beri notifikasi peringatan.

```mermaid
flowchart TD
    classDef default fill:#ffffff,stroke:#000000,stroke-width:1.2px,color:#000000
    classDef startEnd fill:#ffffff,stroke:#000000,stroke-width:2px,color:#000000
    classDef decision fill:#ffffff,stroke:#000000,stroke-width:1.2px,color:#000000
    classDef sad fill:#ffffff,stroke:#000000,stroke-width:1.8px,stroke-dasharray: 4 4,color:#000000

    Start([Mulai: Buka Pilah.in]):::startEnd --> Landing[Buka Halaman Utama / Landing Page]
    Landing --> DecAcc{Sudah Punya<br/>Akun?}:::decision

    %% Registrasi
    DecAcc -- "Belum (Daftar)" --> RegRole[Pilih Peran: Warga / Mitra]
    RegRole --> RegData[Input Data Diri: Nama, WA, Sandi]
    RegData --> DecValid{Format Data<br/>Valid?}:::decision
    
    %% Sad Path 1
    DecValid -- "Tidak" --> ErrData[SISTEM MENOLAK (SAD PATH):<br/>Format Salah, Wajib Min 10 Digit]:::sad
    ErrData -.->|Perbaiki Data| RegData
    
    DecValid -- "Ya (Valid)" --> SendOTP[Kirim Kode OTP ke WhatsApp]
    SendOTP --> InpOTP[Input Kode OTP 6 Digit]
    InpOTP --> DecOTP{Kode OTP<br/>Cocok?}:::decision
    
    %% Sad Path 2
    DecOTP -- "Salah" --> ErrOTP[SISTEM MENOLAK (SAD PATH):<br/>OTP Salah / Kedaluwarsa]:::sad
    ErrOTP -.->|Kirim Ulang Kode| SendOTP
    
    DecOTP -- "Cocok" --> RegAddr[Input Alamat & Titik Jemput Teras]
    RegAddr --> RegPIN[Buat 6 Digit PIN Transaksi]
    RegPIN --> RegDone[Registrasi Berhasil]

    %% Login
    DecAcc -- "Sudah (Masuk)" --> InpID[Input No. WhatsApp / Email]
    InpID --> DecForgot{Lupa Kata<br/>Sandi?}:::decision

    %% Lupa Password
    DecForgot -- "Ya (Lupa)" --> ReqReset[Klik Lupa Password & Minta Token WA]
    ReqReset --> InpResetOTP[Input OTP Reset dari WhatsApp]
    InpResetOTP --> InpNewPass[Input Kata Sandi Baru]
    InpNewPass -.->|Login Sandi Baru| InpID

    %% Normal Login
    DecForgot -- "Ingat" --> InpPass[Input Kata Sandi Akun]
    InpPass --> DecAuth{Kredensial<br/>Cocok?}:::decision
    
    %% Sad Path 3
    DecAuth -- "Salah" --> ErrAuth[SISTEM MENOLAK (SAD PATH):<br/>Kredensial Salah / Tidak Terdaftar]:::sad
    ErrAuth -.->|Ulangi Masuk| InpPass
    
    DecAuth -- "Cocok" --> LoginDone[Login Berhasil & Sesi Terbit]

    %% End
    RegDone --> Home([Masuk ke Beranda Warga]):::startEnd
    LoginDone --> Home
```

---

### Fase 2: Beranda Warga & Deteksi Sampah (SnapSort AI)
- **Happy Path:** Pantau saldo mengendap, ambil foto sampah botol PET, lolos klasifikasi AI, dan otomatis diarahkan ke formulir setor (*prefill*).
- **Sad Path (Sistem Menolak):**
  1. *Limbah B3 / Tercemar:* Terdeteksi baterai, aki, limbah medis, atau zat berbahaya $\rightarrow$ **SISTEM MENOLAK KERAS (Sad Path)**, material dilarang masuk sirkular RW & diarahkan ke TPS B3 DLH.
  2. *Objek Buram / Gelap:* Kamera AI tidak mampu mengenali material $\rightarrow$ **SISTEM MENOLAK ANALISIS (Sad Path)**, instruksikan warga untuk mengambil foto ulang dengan pencahayaan memadai.

```mermaid
flowchart TD
    classDef default fill:#ffffff,stroke:#000000,stroke-width:1.2px,color:#000000
    classDef startEnd fill:#ffffff,stroke:#000000,stroke-width:2px,color:#000000
    classDef decision fill:#ffffff,stroke:#000000,stroke-width:1.2px,color:#000000
    classDef sad fill:#ffffff,stroke:#000000,stroke-width:1.8px,stroke-dasharray: 4 4,color:#000000

    Start([Mulai: Beranda Warga]):::startEnd --> ViewHome[Pantau Saldo Mengendap & Riwayat]
    ViewHome --> DecAI{Gunakan Pindai<br/>SnapSort AI?}:::decision

    DecAI -- "Tidak (Manual)" --> GoManual[Buka Tab Setor Sampah Manual]

    DecAI -- "Ya (Buka AI)" --> OpenAI[Buka Tab SnapSort AI]
    OpenAI --> SnapCam[Arahkan Kamera & Ambil Foto Sampah]
    SnapCam --> DecMat{Hasil Analisis<br/>Material AI?}:::decision

    %% Sad Paths
    DecMat -- "Tercemar / B3" --> WarnB3[SISTEM MENOLAK (SAD PATH):<br/>Limbah B3 Dilarang Masuk Sirkular!]:::sad
    DecMat -- "Buram / Gelap" --> WarnBlur[SISTEM MENOLAK (SAD PATH):<br/>Objek Tidak Terbaca, Foto Ulang]:::sad
    WarnBlur -.->|Ambil Foto Ulang| SnapCam

    %% Happy Path
    DecMat -- "Bersih & Layak" --> AIValid[Deteksi Material Valid: PET 96%, Rp 3.500/kg]
    AIValid --> PrefillSetor[Klik Langsung Setor / Auto-Prefill Tab Setor]

    GoManual --> EndSetor([Menuju Halaman Setor Sampah]):::startEnd
    PrefillSetor --> EndSetor
```

---

### Fase 3: Pengajuan Penyetoran Sampah (Jemput vs Drop-off & Sad Path Di Luar Radius)
- **Happy Path:** Warga memilih kategori & berat sampah, memilih metode jemputan Tossa (ongkir 10%) atau drop-off pos mitra (ongkir 0%), dan menerbitkan tiket digital QR resmi.
- **Sad Path (Sistem Menolak):**
  1. *Sampah Kosong (0 kg):* Warga menekan submit tanpa memilih kategori $\rightarrow$ **Sistem Menolak** & wajib pilih minimal 1 sampah.
  2. *Di Luar Radius Layanan Tossa (> 3 km):* Alamat penjemputan berada di luar jangkauan motor Tossa RW $\rightarrow$ **SISTEM MENOLAK PENJEMPUTAN (Sad Path)**, opsi jemputan dikunci dan sistem secara otomatis merekomendasikan opsi Drop-off Mandiri ke Pos Mitra terdekat.

```mermaid
flowchart TD
    classDef default fill:#ffffff,stroke:#000000,stroke-width:1.2px,color:#000000
    classDef startEnd fill:#ffffff,stroke:#000000,stroke-width:2px,color:#000000
    classDef decision fill:#ffffff,stroke:#000000,stroke-width:1.2px,color:#000000
    classDef sad fill:#ffffff,stroke:#000000,stroke-width:1.8px,stroke-dasharray: 4 4,color:#000000

    Start([Mulai: Tab Setor Sampah]):::startEnd --> PickWaste[Pilih Kategori & Atur Berat kg]
    PickWaste --> DecWasteValid{Kategori Terpilih &<br/>Berat > 0 kg?}:::decision

    %% Sad Path Kosong
    DecWasteValid -- "Tidak" --> ErrEmpty[SISTEM MENOLAK (SAD PATH):<br/>Pilih Minimal 1 Jenis Sampah]:::sad
    ErrEmpty -.->|Pilih Sampah| PickWaste

    DecWasteValid -- "Ya" --> DecMethod{Pilih Metode<br/>Penyetoran?}:::decision

    %% Jemput Tossa
    DecMethod -- "Jemput Armada Tossa" --> CalcTossa[Kalkulasi Ongkir Jemput 10%]
    CalcTossa --> PickAddr[Pilih Alamat Jemput & Patokan]
    PickAddr --> DecRadius{Alamat Dalam<br/>Radius <= 3 km?}:::decision

    %% Sad Path Radius
    DecRadius -- "> 3 km" --> ErrRadius[SISTEM MENOLAK (SAD PATH):<br/>Di Luar Radius Operasional Tossa]:::sad
    ErrRadius --> RecDropoff[Tampilkan Rekomendasi Drop-off Mandiri]
    RecDropoff -.->|Beralih Opsi| CalcDropoff

    DecRadius -- "<= 3 km" --> SubmitTossa[Klik Ajukan Penjemputan Tossa]

    %% Drop-off
    DecMethod -- "Antar Sendiri (Drop-off)" --> CalcDropoff[Kalkulasi Drop-off 0% Ongkir (Saldo Utuh)]
    CalcDropoff --> PickPos[Pilih Drop Point / Pos Mitra RW]
    PickPos --> SubmitDropoff[Klik Buat Tiket Mandiri]

    SubmitTossa --> TicketQR[Tiket Digital QR Terbit: PLH-XXXXXX]
    SubmitDropoff --> TicketQR

    TicketQR --> EndSetor([Selesai: Menunggu Penimbangan Lapangan]):::startEnd
```

---

### Fase 4: Operasional Timbang Lapangan & Sad Path Penolakan Kurasi Fisik
- **Happy Path:** Petugas menimbang sampah di teras/pos mitra, menginput ke Portal Mitra Pengelola, kurasi fisik lolos bersih $\rightarrow$ Saldo Rupiah cair detik itu juga ke Dompet Warga.
- **Sad Path (Sistem Menolak):**
  1. *Warga Tidak Ada di Lokasi:* Kurir Tossa tiba namun warga tidak ada $\rightarrow$ Jadwalkan ulang jemputan (tiket tetap aktif).
  2. *Pos Mitra Tutup:* Warga datang di luar jam operasional (13.00 - 16.00 WIB) $\rightarrow$ Pos tutup, tiket tetap berlaku untuk esok hari.
  3. *KURASI FISIK GAGAL (SISTEM MENOLAK):* Sampah kardus basah kuyup terkena hujan atau botol plastik bercampur minyak santan/B3 $\rightarrow$ Petugas mengklik tombol **"Tolak Sampah (Kurasi Gagal)"** di portal mitra $\rightarrow$ **SISTEM MENOLAK TIKET (Sad Path)**, saldo ditahan Rp 0, dan sistem mengirimkan kartu edukasi penolakan beserta tombol *"Ajukan Setor Ulang"* ke aplikasi warga.

```mermaid
flowchart TD
    classDef default fill:#ffffff,stroke:#000000,stroke-width:1.2px,color:#000000
    classDef startEnd fill:#ffffff,stroke:#000000,stroke-width:2px,color:#000000
    classDef decision fill:#ffffff,stroke:#000000,stroke-width:1.2px,color:#000000
    classDef sad fill:#ffffff,stroke:#000000,stroke-width:1.8px,stroke-dasharray: 4 4,color:#000000

    Start([Mulai: Tiket Digital Aktif]):::startEnd --> DecFieldType{Metode Penyetoran<br/>Lapangan?}:::decision

    %% Jemput
    DecFieldType -- "Jemput Tossa" --> TossaArrive[Armada Tossa Tiba di Alamat Warga]
    TossaArrive --> DecCitizen{Warga Ada di<br/>Rumah?}:::decision
    
    DecCitizen -- "Tidak" --> Reschedule[SAD PATH: Warga Tidak di Lokasi<br/>Jadwalkan Ulang Jemputan]:::sad
    DecCitizen -- "Ada" --> WeighTossa[Timbang Digital Bersama di Teras]

    %% Drop-off
    DecFieldType -- "Antar Sendiri" --> DropoffArrive[Warga Bawa Sampah ke Pos Mitra]
    DropoffArrive --> DecPosOpen{Pos Sedang Buka?<br/>13.00 - 16.00 WIB}:::decision
    
    DecPosOpen -- "Tutup" --> PosClosed[SAD PATH: Pos Tutup<br/>Warga Datang Kembali Besok]:::sad
    DecPosOpen -- "Buka" --> WeighPos[Petugas Timbang Digital di Pos Mitra]

    %% Portal Mitra
    WeighTossa --> OpenMitra[Buka Portal Mitra Pengelola Sampah]
    WeighPos --> OpenMitra

    OpenMitra --> InpWeight[Input Nomor Tiket & Bobot Riil Timbangan]
    InpWeight --> DecKurasi{Kurasi Fisik Lolos<br/>Standar Pilah Bersih?}:::decision

    %% SAD PATH UTAMA: KURASI FISIK GAGAL (SISTEM MENOLAK)
    DecKurasi -- "Tolak (Gagal)" --> ErrKurasi[SISTEM MENOLAK (SAD PATH):<br/>Sampah Basah / Tercemar Minyak / B3]:::sad
    ErrKurasi --> RejTicket[Tiket Berstatus Ditolak & Saldo Rp 0]
    RejTicket --> EduWarga[Kirim Kartu Edukasi Penolakan & Opsi Setor Ulang ke Warga]

    %% HAPPY PATH
    DecKurasi -- "Lolos (Bersih)" --> VerifyData[Verifikasi Data Penimbangan & Kalkulasi Saldo]
    VerifyData --> CreditBalance[Saldo Tunai Masuk Instan ke Dompet Warga]

    CreditBalance --> EndField([Selesai: Saldo Siap Digunakan]):::startEnd
```

---

### Fase 5: Pemanfaatan Saldo Likuid Warga & Sad Paths (PIN Salah & Saldo Kurang)
- **Happy Path:** Warga membelanjakan saldo untuk pupuk kompos olahan mitra (Rp 18.000) atau mencairkan uang tunai ke GoPay/DANA (Rp 50.000) dengan PIN valid.
- **Sad Path (Sistem Menolak):**
  1. *Saldo Tidak Mencukupi:* Nominal belanja atau pencairan melebihi saldo aktif $\rightarrow$ **SISTEM MENOLAK TRANSAKSI (Sad Path)**, transaksi dibatalkan dan sistem meminta warga menyetorkan sampah lebih banyak.
  2. *PIN Transaksi Salah 3 Kali:* Pengguna salah memasukkan PIN transaksi sebanyak 3 kali berturut-turut $\rightarrow$ **SISTEM MENOLAK & KUNCI AKUN SEMENTARA (Sad Path)**, akun dibekukan selama 15 menit demi keamanan saldo, dan sistem mengirimkan tautan reset PIN melalui WhatsApp OTP.

```mermaid
flowchart TD
    classDef default fill:#ffffff,stroke:#000000,stroke-width:1.2px,color:#000000
    classDef startEnd fill:#ffffff,stroke:#000000,stroke-width:2px,color:#000000
    classDef decision fill:#ffffff,stroke:#000000,stroke-width:1.2px,color:#000000
    classDef sad fill:#ffffff,stroke:#000000,stroke-width:1.8px,stroke-dasharray: 4 4,color:#000000

    Start([Mulai: Saldo Mengendap di Dompet]):::startEnd --> DecUse{Pilihan Pemanfaatan<br/>Saldo?}:::decision

    %% Belanja
    DecUse -- "Belanja Produk Upcycle" --> OpenStore[Buka Tab Toko Sirkular]
    OpenStore --> PickProduct[Pilih Pupuk Kompos Super 5kg: Rp 18.000]
    PickProduct --> DecBalStore{Saldo Cukup<br/>>= Rp 18.000?}:::decision
    
    %% Sad Path Saldo Belanja
    DecBalStore -- "Tidak" --> ErrBalStore[SISTEM MENOLAK (SAD PATH):<br/>Saldo Kurang, Transaksi Batal]:::sad

    DecBalStore -- "Cukup" --> PINStore[Input PIN Transaksi 6 Digit]
    PINStore --> DecPINStore{PIN Transaksi<br/>Valid?}:::decision

    %% Sad Path PIN Belanja
    DecPINStore -- "Salah 3x" --> ErrPINStore[SISTEM MENOLAK (SAD PATH):<br/>Akun Dikunci Sementara 15 Menit]:::sad

    DecPINStore -- "Benar" --> StoreDone[Pembelian Kompos Selesai / Loop Tertutup]

    %% Tarik Tunai
    DecUse -- "Tarik Tunai E-Wallet" --> OpenWallet[Buka Tab Dompet Rupiah]
    OpenWallet --> InpCashout[Pilih GoPay/DANA, Nominal Rp 50.000, & No HP]
    InpCashout --> DecMin{Nominal >= 10k &<br/>No HP Valid?}:::decision
    
    DecMin -- "Tidak" --> ErrMin[SISTEM MENOLAK:<br/>Minimal Tarik Rp 10.000]:::sad
    ErrMin -.->|Perbaiki| InpCashout
    
    DecMin -- "Valid" --> DecBalCash{Saldo Cukup<br/>>= Rp 50.000?}:::decision
    
    %% Sad Path Saldo Tarik
    DecBalCash -- "Kurang" --> ErrBalCash[SISTEM MENOLAK (SAD PATH):<br/>Saldo Mengendap Tidak Cukup]:::sad

    DecBalCash -- "Cukup" --> PINCash[Input PIN Transaksi 6 Digit]
    PINCash --> DecPINCash{PIN Transaksi<br/>Valid?}:::decision

    %% Sad Path PIN Tarik
    DecPINCash -- "Salah 3x" --> ErrPINCash[SISTEM MENOLAK (SAD PATH):<br/>Akun Dikunci Sementara 15 Menit]:::sad

    DecPINCash -- "Benar" --> CashDone[Uang Tunai Cair ke E-Wallet (0% Admin Fee)]

    StoreDone --> EndUse([Selesai: Nilai Ekonomi & Lingkungan Nyata]):::startEnd
    CashDone --> EndUse
```

---

## Ringkasan File Siap Pakai

| Item | Tipe | Lokasi File |
|---|---|---|
| **Web Viewer Interaktif** | Live Browser | [http://localhost:3000/userflow_view.html](http://localhost:3000/userflow_view.html) |
| **Draw.io Master (5 Tabs)** | Diagram | [userflow_pilahin.drawio](file:///home/jansky/pilahin-app/userflow_pilahin.drawio) |
| **Draw.io Information Architecture** | Diagram | [information_architecture_pilahin.drawio](file:///home/jansky/pilahin-app/information_architecture_pilahin.drawio) |
| **PNG Screenshot IA (Proposal)** | Gambar | [information_architecture_pilahin.png](file:///home/jansky/Screenshots_Userflow/information_architecture_pilahin.png) |
| **Draw.io Fase 1** | Diagram | [fase_1_registrasi_dan_login.drawio](file:///home/jansky/pilahin-app/drawio_phases/fase_1_registrasi_dan_login.drawio) |
| **Draw.io Fase 2** | Diagram | [fase_2_beranda_dan_snapsort_ai.drawio](file:///home/jansky/pilahin-app/drawio_phases/fase_2_beranda_dan_snapsort_ai.drawio) |
| **Draw.io Fase 3** | Diagram | [fase_3_pengajuan_setor_sampah.drawio](file:///home/jansky/pilahin-app/drawio_phases/fase_3_pengajuan_setor_sampah.drawio) |
| **Draw.io Fase 4** | Diagram | [fase_4_timbang_lapangan_dan_mitra.drawio](file:///home/jansky/pilahin-app/drawio_phases/fase_4_timbang_lapangan_dan_mitra.drawio) |
| **Draw.io Fase 5** | Diagram | [fase_5_belanja_toko_dan_tarik_tunai.drawio](file:///home/jansky/pilahin-app/drawio_phases/fase_5_belanja_toko_dan_tarik_tunai.drawio) |
| **PNG Screenshot Fase 1** | Gambar | [fase_1_registrasi_dan_login.png](file:///home/jansky/pilahin-app/flow_screenshots/fase_1_registrasi_dan_login.png) |
| **PNG Screenshot Fase 2** | Gambar | [fase_2_beranda_dan_snapsort_ai.png](file:///home/jansky/pilahin-app/flow_screenshots/fase_2_beranda_dan_snapsort_ai.png) |
| **PNG Screenshot Fase 3** | Gambar | [fase_3_pengajuan_setor_sampah.png](file:///home/jansky/pilahin-app/flow_screenshots/fase_3_pengajuan_setor_sampah.png) |
| **PNG Screenshot Fase 4** | Gambar | [fase_4_timbang_lapangan_dan_mitra.png](file:///home/jansky/pilahin-app/flow_screenshots/fase_4_timbang_lapangan_dan_mitra.png) |
| **PNG Screenshot Fase 5** | Gambar | [fase_5_belanja_toko_dan_tarik_tunai.png](file:///home/jansky/pilahin-app/flow_screenshots/fase_5_belanja_toko_dan_tarik_tunai.png) |
