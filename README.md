# 🌿 Pilah.in — Platform Sirkular Pengelolaan Sampah Terpilah

> **Kompetisi UI/UX In Action — MIA 2026 UPN Veteran Jakarta**  
> Mengubah beban sampah rumah tangga menjadi berkah bernilai ekonomi melalui siklus ekonomi sirkular yang transparan, modern, dan mudah digunakan.

[![Vercel Deployment](https://img.shields.io/badge/Vercel-pilahin--app--beta.vercel.app-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://pilahin-app-beta.vercel.app)
[![React](https://img.shields.io/badge/React-18.3-61dafb?style=for-the-badge&logo=react&logoColor=black)](https://react.dev)
[![Vite](https://img.shields.io/badge/Vite-6.4-646cff?style=for-the-badge&logo=vite&logoColor=white)](https://vitejs.dev)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.4-38bdf8?style=for-the-badge&logo=tailwindcss&logoColor=white)](https://tailwindcss.com)
[![E2E Tests](https://img.shields.io/badge/E2E%20Tests-16%2F16%20Passing-emerald?style=for-the-badge&logo=puppeteer&logoColor=white)](./e2e_tests)

---

## 🚀 Live Demo
Aplikasi telah dideploy di **Vercel** dan dapat diakses langsung secara publik tanpa instalasi:
👉 **[https://pilahin-app-beta.vercel.app](https://pilahin-app-beta.vercel.app)**  
*(Mirror cadangan Surge: [https://pilahin-app.surge.sh](https://pilahin-app.surge.sh))*

---

## 📌 Latar Belakang & Problem Statement

Kebanyakan masyarakat rumah tangga enggan memilah dan menyetorkan sampah karena beberapa kendala nyata:
1. **Tidak memiliki timbangan:** Calon penyetor tidak tahu pasti berat sampah mereka dan merasa bingung saat aplikasi mewajibkan input kilogram di awal.
2. **Kendala logistik & transparansi biaya:** Sulit mengantar langsung ke TPS3R/pengepul, namun jika dijemput tidak ada kejelasan perihal ongkos kirim.
3. **Ekonomi sirkular terputus:** Saldo sampah seringkali hanya berupa angka statis tanpa perputaran nilai kembali ke produk ramah lingkungan.

### 💡 Solusi Pilah.in
- **Panggil Dulu, Timbang di Tempat:** Warga cukup memilih kategori jenis sampah dan memesan penjemputan mitra (atau menjadwalkan drop-off). Estimasi berat tersedia sebagai kalkulator opsional, sementara timbangan akurat dilakukan oleh kurir/mitra dengan timbangan digital terverifikasi.
- **Top Segmented Method Switcher:** Beralih dengan mudah antara **🚚 Jemput Mitra (Pickup)** dan **📍 Antar Sendiri (Drop-off)** dengan kartu lokasi yang dinamis (*Alamat Jemput* vs *Titik Pengepul Terdekat*).
- **Transparansi Ongkos Jemput 10%:** Untuk layanan jemput, sistem secara jujur memotong 10% dari total estimasi sebagai ongkos operasional kurir mitra lokal, lengkap dengan banner peringatan dan rincian transparan.
- **Dompet Saldo Mengendap & Pasar Sirkular:** Saldo hasil setor sampah langsung masuk dompet digital, dapat ditarik ke e-wallet (GoPay, DANA) atau langsung dibelanjakan untuk produk olahan daur ulang (kompos organik, eco-enzym, tas daur ulang) buatan pengelola sampah lokal.

---

## ✨ Fitur Utama

### 1. 🚚 Alur Setor Sampah Adaptif
- **Metode Fleksibel:** Switcher di bagian atas memungkinkan pemilihan metode *Jemput Mitra* atau *Antar Sendiri* secara instan.
- **Dynamic Location Card:**
  - *Jemput Mitra:* Menampilkan alamat rumah pengguna lengkap dengan modal edit alamat & catatan patokan.
  - *Antar Sendiri:* Menampilkan titik pengepul mitra terdekat (jarak, jam operasional, rating) dengan pemilih lokasi interaktif.
- **Kalkulator Estimasi Berat:** Slider interaktif untuk menghitung perkiraan berat dan nominal rupiah (Rp/kg) berdasarkan jenis sampah (Plastik PET, Kertas & Kardus, Logam & Kaleng, Minyak Jelantah, Elektronik).
- **Konfirmasi Transparan:** Dialog rincian pesanan dengan potongan 10% ongkir untuk jemput atau 0% untuk antar sendiri.

### 2. 💳 Dompet Saldo Mengendap
- Pantau saldo rupiah terkumpul (`Rp`) dan Poin Hijau keberlanjutan.
- Simulasi penarikan dana instan ke GoPay atau DANA dengan validasi nomor rekening/HP.
- Riwayat mutasi transaksi real-time.

### 3. 🛍️ Pasar Sirkular (Eco-Shop)
- Belanja produk ramah lingkungan karya bank sampah / mitra pengelola lokal.
- Pembayaran instan memotong langsung saldo mengendap hasil penjualan sampah.

### 4. 📚 Edukasi & Panduan Pilah AI
- Ensiklopedia jenis sampah (Plastik, Kertas, Logam, Organik, Elektronik).
- Tips mencegah kontaminasi sampah agar bernilai jual optimal.

### 5. 🎬 Netflix-Style Frosted Navbar
- Navigasi bawah bertema gelap modern (`bg-slate-950/92 backdrop-blur-xl`) dengan aksen glow emerald.
- Responsif di layar smartphone maupun tablet/desktop.

---

## 🛠️ Tech Stack & Arsitektur

- **Frontend Framework:** React 18
- **Bundler & Build Tool:** Vite
- **Styling:** Tailwind CSS (Responsive, Clean Neumorphic & Frosted Glass effects)
- **Icons:** Lucide React
- **Micro-interactions:** Canvas Confetti
- **Testing:** Puppeteer Automated End-to-End Test Suite

---

## 💻 Panduan Menjalankan Secara Lokal

### Prasyarat
- Node.js versi 18 atau lebih baru
- npm versi 9 atau lebih baru

### Langkah Instalasi
```bash
# 1. Clone repositori
git clone https://github.com/Jansky0/pilahin-app.git
cd pilahin-app

# 2. Pasang dependensi
npm install

# 3. Jalankan server pengembangan
npm run dev
```

Buka peramban di `http://localhost:3000` (atau port yang ditampilkan di terminal).

### Menjalankan Build Produksi
```bash
npm run build
npm run preview
```

### Menjalankan Uji Coba E2E
```bash
node e2e_tests/comprehensive_test.cjs
```

---

## 📁 Struktur Direktori

```
pilahin-app/
├── public/              # Aset statis publik
├── src/
│   ├── App.jsx          # Komponen utama antarmuka & state management
│   ├── index.css        # Tailwind CSS & custom animations
│   └── main.jsx         # Entry point React
├── e2e_tests/           # Skrip pengujian otomatis Puppeteer
├── dist/                # Output build produksi (Surge deployment)
├── index.html           # Template HTML utama
├── package.json         # Konfigurasi dependensi & skrip npm
├── vite.config.js       # Konfigurasi Vite bundler
└── README.md            # Dokumentasi proyek
```

---

## 👥 Pengembang & Tim

- **Pengembang:** Jansky0 (`andikagt99@gmail.com`)
- **Tujuan:** Kompetisi UI/UX In Action — MIA 2026 UPN Veteran Jakarta

---

*🌿 Bersama Pilah.in, wujudkan Indonesia bersih tanpa beban dan ciptakan nilai ekonomi nyata dari setiap kilogram sampah terpilah.*
