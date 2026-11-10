# BAB III: ANALISIS DAN PERANCANGAN DESAIN
## 3.1 Analisis Desain Karya

---

### a. Target Pengguna (*Target Audience*)

Dalam merancang platform **Pilah.in**, perumusan target pengguna didasarkan pada pendekatan **ekosistem dua sisi (*two-sided platform*)**. Solusi pengelolaan sampah tidak dapat diselesaikan hanya dari sisi warga (penyetor) tanpa melibatkan kesiapan pihak operasional penjemput dan penampung (bank sampah/TPS3R).

#### 1. Segmen Utama Target Pengguna:
1. **Warga Rumah Tangga Urban & Komunitas Pemukiman (Sisi Penyetor / *Waste Generators*)**
   - **Profil**: Ibu rumah tangga, keluarga muda, dan penghuni komplek perumahan padat usia 22–50 tahun yang bertanggung jawab atas tata kelola sampah harian domestik.
   - **Data Pendukung Riset & Studi Literatur**:
     - Berdasarkan data **Sistem Informasi Pengelolaan Sampah Nasional (SIPSN) KLHK (2024)**, sektor rumah tangga menyumbang kontribusi timbulan sampah terbesar di Indonesia, yaitu mencapai **38,5%** dari total timbulan sampah nasional.
     - Studi perilaku dari *Katadata Insight Center* (2023) menunjukkan bahwa **64,8% masyarakat urban tidak memilah sampah**, dengan alasan utama: (1) repot harus mengantar sampah dalam jumlah besar ke bank sampah yang lokasinya jauh (53,2%), dan (2) tidak adanya insentif finansial langsung yang sepadan dengan usaha pemilahan (41,7%).
   - **Kebutuhan**: Layanan penjemputan sampah terpilah langsung dari teras rumah tanpa batas minimum timbangan yang membebani (*Zero-Scale Barrier*), kepastian jadwal jemput, serta imbalan saldo uang tunai Rupiah asli yang transparan.
   - **Tujuan**: Menjaga kebersihan dan kerapian rumah tanpa tumpukan sampah berbau, sembari memperoleh tambahan pendapatan tunai riil harian/mingguan.

2. **Pengelola Bank Sampah RW & Petugas Lapangan TPS3R (Sisi Mitra / *Waste Collectors & Aggregators*)**
   - **Profil**: Pengurus lingkungan RW, kader PKK, dan operator armada motor roda tiga (Tossa) berusia 30–55 tahun yang bertugas mencatat timbangan dan mengolah sampah daur ulang di tingkat kelurahan.
   - **Data Pendukung**:
     - Laporan Asosiasi Bank Sampah Indonesia (ASOBSI) menyatakan lebih dari **70% Bank Sampah Unit (BSU) tingkat RW berstatus pasif atau mati suri**. Akar permasalahannya adalah pencatatan manual berbasis buku kas kertas (*paper-based logbook*) yang rentan salah hitung, ketidakpastian volume pasokan sampah bersih dari warga, serta kesulitan memasarkan produk hilir olahan (kompos & kerajinan daur ulang).
   - **Kebutuhan**: Sistem pencatatan digital cepat berbasis timbangan lapangan, verifikasi tiket QR instan, dan kanal distribusi penjualan kompos olahan kembali ke warga lokal.
   - **Tujuan**: Meningkatkan efisiensi logistik rute jemputan, menekan kecurangan timbangan, dan mencapai perputaran ekonomi mandiri (*closed-loop revenue*).

---

### b. Batasan Aplikasi (*Scope & Limitations*)

Untuk memastikan realisasi solusi terfokus, terukur, dan dapat diuji secara efektif, ruang lingkup (*scope*) dan batasan sistem Pilah.in dirumuskan ke dalam 5 domain utama:

| Domain Batasan | Ruang Lingkup Sistem Pilah.in | Batasan & Keterbatasan Sistem |
| :--- | :--- | :--- |
| **1. Cakupan Wilayah (Geografis)** | Beroperasi secara *hyperlocal* tingkat rukun warga / kelurahan (wilayah pilot studi: **RW 05 Tebet Barat, Jakarta Selatan**). | Penjemputan motor Tossa dibatasi radius maksimal **2,0 km** dari titik pangkalan TPS3R mitra. Pengguna di luar radius layanan akan menerima notifikasi *Out-of-Service Area* dan tiket ditolak secara otomatis (*Sad Path*). |
| **2. Klasifikasi Material Sampah** | Menerima fraksi sampah anorganik bersih bernilai ekonomis (Plastik PET botol bening, HDPE botol tebal, kardus, kertas duplex, kaleng aluminium) dan organik terkompos. | **TIDAK melayani Limbah Medis & B3 (Bahan Berbahaya dan Beracun)** seperti baterai, aki bekas, botol pestisida, atau jarum suntik. Fitur *SnapSort AI* dilengkapi modul deteksi bahaya untuk langsung memblokir pengajuan limbah B3. |
| **3. Arsitektur Perangkat & Aksesibilitas** | Dirancang sebagai *Progressive Web App (PWA)* responsif dengan target utama layar ponsel pintar (*smartphone* rasio 9:19.5, resolusi min. 360x640px hingga 430x932px). | Memerlukan peramban web modern (*Google Chrome 90+*, *Apple Safari 14+*) dengan izin akses kamera aktif (*WebRTC Camera API*) untuk fitur pemindaian foto AI dan QR Code. Belum mendukung pemindaian offline tanpa koneksi internet. |
| **4. Validasi Timbangan (Anti-Fraud)** | Estimasi kuantitas awal dihitung menggunakan modul *Zero-Scale Barrier* berbasis unit volume visual (kantong kresek, kardus mi instan, karung beras). | **SnapSort AI dan estimasi warga hanya berfungsi sebagai panduan acuan (*decision support*)**. Nilai gramasi dan saldo final wajib diverifikasi dan dikunci oleh petugas mitra menggunakan timbangan gantung digital di depan rumah warga saat penjemputan. |
| **5. Transaksi Finansial & Dompet** | Saldo akumulasi merupakan saldo Rupiah asli (bukan token/poin fiktif) yang dapat dicairkan langsung ke dompet digital (GoPay, OVO, Dana) atau dibelanjakan produk pupuk kompos di Toko Sirkular. | Batas penarikan tunai (*cashout*) minimum adalah **Rp 10.000** dan maksimum **Rp 500.000 per transaksi per hari**. Penarikan di bawah nominal minimum akan ditolak oleh sistem validasi dompet. |

---

### c. Platform yang Digunakan (*Development Platform*)

Platform yang dipilih untuk pengembangan karya Pilah.in adalah **Mobile Web Application / Progressive Web App (PWA)** dengan memanfaatkan ekosistem modern:
- **Core Framework**: React.js 18 + Vite (arsitektur berbasis komponen modular).
- **Styling System**: Tailwind CSS v3 (sistem token desain terstandarisasi, responsivitas dinamis).
- **Iconography**: Lucide React Icons (ikon semantik aksesibel).
- **Hosting & Deployment**: Vercel Cloud Platform (SSL otomatis, CDN global, latensi rendah).

#### Alasan Pemilihan Platform & Kelebihannya:
1. **Zero-Installation Barrier (Menghilangkan Hambatan Adopsi Warga)**
   Warga kalangan rumah tangga sering enggan mengunduh aplikasi *native* berukuran besar (50–100 MB) dari Play Store/App Store karena keterbatasan memori internal ponsel *entry-level*. Dengan format PWA, pengguna dapat langsung mengakses seluruh fitur melalui peramban web atau memindai kode QR tanpa proses instalasi yang berbelit.
2. **Cross-Platform Compatibility (Lintas Perangkat Sekali Bangun)**
   Aplikasi dapat berjalan dengan konsistensi antarmuka 100% pada platform Android maupun iOS tanpa perlu memelihara dua basis kode (*codebase*) terpisah, sehingga mempercepat iterasi perancangan dan efisiensi biaya pengembangan.
3. **Pemanfaatan Web Hardware APIs Modern**
   PWA modern telah mendukung API perangkat keras asli seperti kamera web (*MediaDevices API*) untuk pemindaian *SnapSort AI*, *Geolocation API* untuk validasi radius penjemputan, serta fitur *Add to Home Screen* yang memberikan rasa penggunaan (*user experience*) layaknya aplikasi *native*.

---

### d. User Persona (*Fictional User Profiles*)

Berdasarkan sintesis data survei lapangan dan wawancara mendalam, disusun dua profil persona realistis yang merepresentasikan kedua sisi ekosistem Pilah.in:

#### Persona 1: Warga Rumah Tangga (Sisi Penyetor)
* **Nama**: Ibu Siti Rahmawati (38 Tahun)
* **Pekerjaan**: Ibu Rumah Tangga & Pembuat Kue Rumahan
* **Lokasi**: Tebet Barat RW 05, Jakarta Selatan
* **Pendidikan**: D3 Manajemen
* **Tingkat Kemahiran Teknologi**: Menengah (Aktif menggunakan WhatsApp, Shopee, dan GoPay/e-wallet untuk belanja dapur).
* **Kutipan (*Quote*)**:
  > *"Saya mau aja pilah sampah botol dan kardus paket, tapi kalau harus nyimpen berkilo-kilo sampai rumah berantakan terus gotong sendiri ke bank sampah yang jauh, ya mending dibuang ke tempat sampah depan rumah."*
* **Perilaku (*Behaviors*)**:
  - Menghasilkan sampah anorganik harian berupa botol minyak goreng, kardus paket kiriman belanja daring, dan botol minuman plastik keluarga.
  - Sangat menghargai kebersihan dapur dan efisiensi anggaran belanja harian keluarga.
* **Tujuan (*Goals*)**:
  - Ingin sampah anorganik rumah tangga dijemput secara rutin tanpa membuat rumah terlihat kotor dan menumpuk.
  - Ingin usaha pemilahan sampahnya menghasilkan uang tambahan riil untuk menambah saldo belanja sayur atau pulsa.
* **Hambatan & Keluhan (*Pain Points*)**:
  - Tidak memiliki timbangan gantung di rumah untuk menimbang sampah sebelum disetor.
  - Bank sampah RW hanya buka 1 kali sebulan dan lokasinya berjarak lebih dari 1 km.
  - Sering kecewa dengan aplikasi bank sampah lain yang hanya memberikan "koin poin virtual" yang sulit ditukar uang tunai.
* **Bagaimana Pilah.in Membantu**:
  - Fitur *SnapSort AI* & *Zero-Scale Estimator* memungkinkannya menyetor sampah walau hanya sekantong kresek tanpa perlu menimbang sendiri.
  - Armada motor Tossa menjemput langsung ke teras rumah, dan saldo langsung masuk ke dompet aplikasi dalam bentuk Rupiah yang bisa dicairkan ke GoPay seketika.

---

#### Persona 2: Koordinator Bank Sampah RW (Sisi Mitra Pengelola)
* **Nama**: Pak Bambang Hartono (46 Tahun)
* **Pekerjaan**: Koordinator Bank Sampah RW 05 & Petugas Logistik Lapangan
* **Lokasi**: Pangkalan TPS3R Kelurahan Tebet Barat
* **Pendidikan**: SMA
* **Tingkat Kemahiran Teknologi**: Pemula-Menengah (Fasih menggunakan ponsel pintar Android untuk WhatsApp dan navigasi Google Maps).
* **Kutipan (*Quote*)**:
  > *"Tiap akhir bulan saya pusing rekap buku timbangan kertas yang kena air atau catatannya hilang. Warga juga jarang pilah dari rumah, jadi sampah campur aduk dan kompos yang kami buat di TPS3R malah numpuk nggak laku."*
* **Perilaku (*Behaviors*)**:
  - Mengoperasikan motor roda tiga Tossa untuk mengangkut sampah terpilah keliling lingkungan warga 2 kali seminggu.
  - Membawa timbangan gantung digital portabel saat berkeliling menjemput sampah ke rumah-rumah.
* **Tujuan (*Goals*)**:
  - Mencatat setoran sampah warga secara cepat di tempat tanpa ribet menulis manual di buku tulis.
  - Memastikan hanya sampah bersih bernilai daur ulang yang masuk ke bank sampah untuk menjaga higienitas dan nilai jual ke pengepul besar.
  - Memiliki saluran penjualan untuk produk pupuk kompos hasil olahan TPS3R kembali ke warga lingkungan sekitar.
* **Hambatan & Keluhan (*Pain Points*)**:
  - Sering terjadi selisih pencatatan uang setoran antara catatan warga dan catatan kas pengurus RW.
  - Warga sering menyelipkan sampah kotor atau limbah berbahaya (baterai/obat) yang merusak mesin cacah plastik.
  - Gudang TPS3R penuh oleh tumpukan karung pupuk kompos organik yang belum terserap pasar.
* **Bagaimana Pilah.in Membantu**:
  - Portal Mitra di Pilah.in menyediakan dasbor verifikasi tiket QR sekali pindai dan penguncian gramasi timbangan digital yang otomatis mengkreditkan saldo ke rekening warga secara transparan.
  - Fitur *Modal Kurasi Sampah* memungkinkan penolakan sampah kotor/B3 disertai alasan edukatif transparan (*Sad Path*).
  - *Toko Sirkular Lokal* memajang produk pupuk kompos olahan TPS3R agar dapat dibeli langsung oleh warga menggunakan saldo sampah mereka.

---

### e. Analisis SWOT (*Strengths, Weaknesses, Opportunities, Threats*)

| Aspek | Analisis Deskriptif | Implikasi Strategis Desain Sistem |
| :--- | :--- | :--- |
| **Strengths (Kekuatan)** | 1. **Zero-Scale Barrier**: Warga dapat menyetor sampah berbasis perkiraan visual (kantong/kardus) tanpa harus memiliki timbangan fisik sendiri.<br>2. **Closed-Loop Circular Economy**: Saldo hasil jual sampah dapat langsung dibelanjakan pupuk kompos lokal hasil olahan TPS3R mitra (*circular balance*).<br>3. **Real-Money Incentive**: Menggunakan mata uang Rupiah asli dengan pencairan fleksibel ke e-wallet, bukan sistem poin koin fiktif.<br>4. **Two-Sided Synergy**: Antarmuka terpadu untuk warga penyetor dan portal verifikasi timbangan untuk mitra pengelola RW. | Menghilangkan friksi adopsi di level akar rumput, menciptakan retensi pengguna yang tinggi karena keuntungan finansial langsung dirasakan, serta memberdayakan ekonomi lokal bank sampah RW. |
| **Weaknesses (Kelemahan)** | 1. **Ketergantungan pada Armada Fisik**: Efektivitas layanan sangat bertumpu pada kesiapan fisik armada motor Tossa dan keaktifan pengurus bank sampah setempat.<br>2. **Keterbatasan Akurasi Computer Vision Web**: Pemindaian AI pada kamera ponsel berpotensi bias jika pencahayaan ruangan warga redup atau objek sampah tertumpuk. | Diantisipasi dengan mekanisme *dual-check*: perkiraan AI hanya menjadi estimasi sementara, sedangkan penentuan berat dan pencairan saldo akhir tetap diverifikasi oleh timbangan fisik mitra di lapangan. |
| **Opportunities (Peluang)** | 1. **Regulasi Pemerintah yang Mendukung**: Kebijakan Permen LHK No. 14 Tahun 2021 tentang Pengelolaan Sampah pada Bank Sampah dan target *Indonesia Bebas Sampah 2025*.<br>2. **Tingginya Penetrasi Dompet Digital**: Lebih dari 80% masyarakat urban telah terbiasa bertransaksi menggunakan GoPay/OVO/Dana/QRIS.<br>3. **Tren Gaya Hidup Berkelanjutan (*Green Lifestyle*)**: Generasi muda dan ibu rumah tangga semakin peduli terhadap jejak karbon (*carbon footprint metric*). | Peluang kemitraan strategis dengan dinas lingkungan hidup pemda, integrasi *corporate CSR sponsorship*, dan ekspansi jaringan bank sampah lintas rukun warga di kota-kota besar Indonesia. |
| **Threats (Ancaman)** | 1. **Fluktuasi Harga Pasar Daur Ulang**: Perubahan harga beli sampah anorganik dari pengepul pabrik besar dapat memengaruhi margin harga beli ke warga.<br>2. **Inersia Kebiasaan Warga**: Resistensi budaya membuang sampah sembarangan atau menggabungkan seluruh jenis sampah ke satu kantong plastik.<br>3. **Kecurangan Kualitas Sampah (*Fraud*)**: Potensi warga membasahi kardus atau mengisi botol plastik dengan pasir agar timbangan lebih berat. | Sistem dilengkapi fitur *SOP Verifikasi Mitra*, batas toleransi timbangan, dan opsi pembatalan/penolakan tiket setoran (*Sad Path*) jika material sampah terbukti basah atau sengaja dimanipulasi. |
