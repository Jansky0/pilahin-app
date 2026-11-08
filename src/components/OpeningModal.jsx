import React, { useState } from 'react';
import {
  Recycle,
  Sparkles,
  Truck,
  Wallet,
  ShoppingBag,
  CheckCircle2,
  X,
  ArrowRight,
  ShieldCheck,
  Building2,
  Package,
  Layers,
  ChevronRight
} from 'lucide-react';

export default function OpeningModal({ isOpen, onClose, onOpenAuth }) {
  const [activeTab, setActiveTab] = useState('tentang'); // 'tentang', 'alur', 'katalog'

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 bg-slate-950/75 backdrop-blur-xs flex items-center justify-center p-3 sm:p-4 overflow-y-auto">
      <div className="w-full max-w-md max-h-[92dvh] overflow-y-auto overscroll-contain bg-white rounded-3xl shadow-2xl border border-slate-200 text-slate-900 flex flex-col animate-in fade-in zoom-in-95 duration-200">
        
        {/* Modal Top Bar */}
        <div className="sticky top-0 bg-white/95 backdrop-blur-md px-5 py-3.5 border-b border-slate-100 flex items-center justify-between z-10">
          <div className="flex items-center gap-2">
            <div className="w-7 h-7 rounded-xl bg-gradient-to-tr from-emerald-600 to-teal-500 text-white flex items-center justify-center shadow-xs">
              <Recycle className="w-4 h-4" />
            </div>
            <div>
              <h3 className="text-sm font-extrabold text-slate-900 tracking-tight flex items-center gap-1.5">
                <span>Pilah.in</span>
                <span className="text-[10px] bg-emerald-100 text-emerald-800 font-bold px-1.5 py-0.5 rounded-full">
                  Panduan
                </span>
              </h3>
              <p className="text-[10px] text-slate-500">Platform Ekonomi Sirkular Sampah</p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="w-8 h-8 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-500 hover:text-slate-800 flex items-center justify-center transition cursor-pointer"
            aria-label="Tutup Panduan"
          >
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* Tab Switcher */}
        <div className="px-5 pt-3">
          <div className="grid grid-cols-3 gap-1 bg-slate-100 p-1 rounded-2xl text-xs font-bold">
            <button
              onClick={() => setActiveTab('tentang')}
              className={`py-2 rounded-xl transition cursor-pointer text-center ${
                activeTab === 'tentang'
                  ? 'bg-white text-emerald-800 shadow-xs'
                  : 'text-slate-500 hover:text-slate-900'
              }`}
            >
              Tentang
            </button>
            <button
              onClick={() => setActiveTab('alur')}
              className={`py-2 rounded-xl transition cursor-pointer text-center ${
                activeTab === 'alur'
                  ? 'bg-white text-emerald-800 shadow-xs'
                  : 'text-slate-500 hover:text-slate-900'
              }`}
            >
              4 Langkah Alur
            </button>
            <button
              onClick={() => setActiveTab('katalog')}
              className={`py-2 rounded-xl transition cursor-pointer text-center ${
                activeTab === 'katalog'
                  ? 'bg-white text-emerald-800 shadow-xs'
                  : 'text-slate-500 hover:text-slate-900'
              }`}
            >
              Jenis Sampah
            </button>
          </div>
        </div>

        {/* Content Body */}
        <div className="p-5 space-y-4 flex-1">
          {/* TAB 1: TENTANG PILAH.IN */}
          {activeTab === 'tentang' && (
            <div className="space-y-3.5">
              {/* Hero Banner */}
              <div className="bg-gradient-to-br from-emerald-800 to-teal-900 text-white rounded-2xl p-4.5 space-y-2 shadow-md">
                <div className="inline-flex items-center gap-1.5 bg-emerald-700/80 text-emerald-200 px-2.5 py-0.5 rounded-full text-[10px] font-bold">
                  <Sparkles className="w-3 h-3 text-amber-300" />
                  <span>Sampah Jadi Lebih Bernilai</span>
                </div>
                <h4 className="text-base font-extrabold leading-snug">
                  Ubah Sampah Terpilah Jadi Saldo Tunai &amp; Berdayakan Komunitas Lokal
                </h4>
                <p className="text-xs text-emerald-100/90 leading-relaxed">
                  Pilah.in adalah platform ekonomi sirkular dua arah yang menghubungkan warga penyetor sampah dengan Bank Sampah RW &amp; TPS3R lokal.
                </p>
              </div>

              {/* The Two-Sided Problem & Solution */}
              <div className="space-y-2">
                <div className="bg-rose-50 border border-rose-200/80 rounded-2xl p-3 text-xs text-rose-950 space-y-1">
                  <div className="font-bold flex items-center gap-1.5 text-rose-800">
                    <span>❌ Masalah yang Dipecahkan</span>
                  </div>
                  <p className="text-[11px] text-rose-900/90 leading-relaxed">
                    Warga malas memilah karena dikira tidak ada nilainya dan bingung mau disalurkan ke mana. Di sisi lain, pengurus Bank Sampah RW kekurangan pasokan dan produk kompos olahan menumpuk tidak ada pembelinya.
                  </p>
                </div>

                <div className="bg-emerald-50 border border-emerald-200/80 rounded-2xl p-3 text-xs text-emerald-950 space-y-1">
                  <div className="font-bold flex items-center gap-1.5 text-emerald-800">
                    <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" />
                    <span>✅ Solusi Sirkular Pilah.in</span>
                  </div>
                  <p className="text-[11px] text-emerald-900/90 leading-relaxed">
                    Sampah terpilah ditimbang digital di tempat. Saldo otomatis cair ke dompet dalam bentuk <strong>Rupiah nyata (tanpa poin fiktif)</strong>. Saldo bisa ditarik tunai ke GoPay/DANA atau dibelanjakan kembali untuk membeli pupuk kompos &amp; pot daur ulang karya warga.
                  </p>
                </div>
              </div>

              {/* 3 Core Highlights */}
              <div className="space-y-2 pt-1">
                <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400 block">
                  Keunggulan Utama
                </span>
                <div className="grid grid-cols-3 gap-2 text-center">
                  <div className="bg-slate-50 border border-slate-200 p-2.5 rounded-xl">
                    <div className="text-base mb-1">💸</div>
                    <div className="font-bold text-[11px] text-slate-900">Rupiah Likuid</div>
                    <div className="text-[9px] text-slate-500">Tarik ke GoPay / DANA</div>
                  </div>
                  <div className="bg-slate-50 border border-slate-200 p-2.5 rounded-xl">
                    <div className="text-base mb-1">🛵</div>
                    <div className="font-bold text-[11px] text-slate-900">Motor Tossa</div>
                    <div className="text-[9px] text-slate-500">Jemput ke teras rumah</div>
                  </div>
                  <div className="bg-slate-50 border border-slate-200 p-2.5 rounded-xl">
                    <div className="text-base mb-1">🌱</div>
                    <div className="font-bold text-[11px] text-slate-900">Pasar Upcycle</div>
                    <div className="text-[9px] text-slate-500">Belanja kompos mitra</div>
                  </div>
                </div>
              </div>
            </div>
          )}

          {/* TAB 2: 4 LANGKAH ALUR SIRKULAR */}
          {activeTab === 'alur' && (
            <div className="space-y-3">
              <p className="text-xs text-slate-600">
                Alur sirkular tertutup dari rumahmu hingga kembali menjadi produk bermanfaat:
              </p>

              <div className="space-y-2.5">
                {/* Step 1 */}
                <div className="flex gap-3 bg-slate-50 border border-slate-200/90 rounded-2xl p-3 items-start">
                  <div className="w-7 h-7 rounded-xl bg-emerald-600 text-white font-extrabold text-xs flex items-center justify-center flex-shrink-0 mt-0.5 shadow-xs">
                    1
                  </div>
                  <div className="space-y-0.5">
                    <h5 className="text-xs font-bold text-slate-900">Pilah Sampah di Rumah</h5>
                    <p className="text-[11px] text-slate-500 leading-relaxed">
                      Pisahkan kardus paket, botol plastik PET, minyak jelantah bekas gorengan, atau sisa organik dapur. Pastikan dalam kondisi kering &amp; bersih.
                    </p>
                  </div>
                </div>

                {/* Step 2 */}
                <div className="flex gap-3 bg-slate-50 border border-slate-200/90 rounded-2xl p-3 items-start">
                  <div className="w-7 h-7 rounded-xl bg-emerald-600 text-white font-extrabold text-xs flex items-center justify-center flex-shrink-0 mt-0.5 shadow-xs">
                    2
                  </div>
                  <div className="space-y-0.5">
                    <h5 className="text-xs font-bold text-slate-900">Pilih Jemput atau Antar Mandiri</h5>
                    <p className="text-[11px] text-slate-500 leading-relaxed">
                      <strong>Jemput Mitra:</strong> Armada motor roda tiga Tossa jemput ke alamat rumahmu (ada potongan ongkir logistik 10%).<br />
                      <strong>Antar Sendiri:</strong> Bawa langsung ke Bank Sampah terdekat untuk menikmati <strong>100% saldo utuh tanpa potongan</strong>.
                    </p>
                  </div>
                </div>

                {/* Step 3 */}
                <div className="flex gap-3 bg-slate-50 border border-slate-200/90 rounded-2xl p-3 items-start">
                  <div className="w-7 h-7 rounded-xl bg-emerald-600 text-white font-extrabold text-xs flex items-center justify-center flex-shrink-0 mt-0.5 shadow-xs">
                    3
                  </div>
                  <div className="space-y-0.5">
                    <h5 className="text-xs font-bold text-slate-900">Timbang Digital &amp; Saldo Otomatis Masuk</h5>
                    <p className="text-[11px] text-slate-500 leading-relaxed">
                      Petugas menimbang sampah di tempat secara transparan. Nilai rupiah langsung dikreditkan ke saldo mengendap di dompet aplikasimu.
                    </p>
                  </div>
                </div>

                {/* Step 4 */}
                <div className="flex gap-3 bg-slate-50 border border-slate-200/90 rounded-2xl p-3 items-start">
                  <div className="w-7 h-7 rounded-xl bg-emerald-600 text-white font-extrabold text-xs flex items-center justify-center flex-shrink-0 mt-0.5 shadow-xs">
                    4
                  </div>
                  <div className="space-y-0.5">
                    <h5 className="text-xs font-bold text-slate-900">Tarik ke E-Wallet atau Belanja Produk Daur Ulang</h5>
                    <p className="text-[11px] text-slate-500 leading-relaxed">
                      Cairkan saldo kapan saja ke GoPay / DANA bebas biaya admin, ATAU belanjakan pupuk kompos organik dan pot tanaman daur ulang di Toko Sirkular.
                    </p>
                  </div>
                </div>
              </div>
            </div>
          )}

          {/* TAB 3: KATALOG SAMPAH DITERIMA */}
          {activeTab === 'katalog' && (
            <div className="space-y-3">
              <div className="flex items-center justify-between text-xs">
                <span className="font-bold text-slate-800">Komoditas Bernilai Tinggi</span>
                <span className="text-[10px] text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-full font-bold">
                  Update Real-time
                </span>
              </div>

              <div className="space-y-2">
                <div className="bg-slate-50 border border-slate-200/80 rounded-xl p-2.5 flex items-center justify-between">
                  <div className="flex items-center gap-2.5">
                    <span className="text-xl">📦</span>
                    <div>
                      <div className="text-xs font-bold text-slate-900">Kardus Box &amp; Lembaran</div>
                      <div className="text-[10px] text-slate-500">Kering, lipat pipih, tanpa selotip tebal</div>
                    </div>
                  </div>
                  <div className="text-right">
                    <div className="text-xs font-extrabold text-emerald-700">Rp 1.800/kg</div>
                    <div className="text-[9px] text-emerald-600 font-bold">▲ +5%</div>
                  </div>
                </div>

                <div className="bg-slate-50 border border-slate-200/80 rounded-xl p-2.5 flex items-center justify-between">
                  <div className="flex items-center gap-2.5">
                    <span className="text-xl">🧴</span>
                    <div>
                      <div className="text-xs font-bold text-slate-900">Botol Plastik PET Bening</div>
                      <div className="text-[10px] text-slate-500">Kosongkan air, remas/pipihkan</div>
                    </div>
                  </div>
                  <div className="text-right">
                    <div className="text-xs font-extrabold text-emerald-700">Rp 3.500/kg</div>
                    <div className="text-[9px] text-emerald-600 font-bold">▲ +8%</div>
                  </div>
                </div>

                <div className="bg-slate-50 border border-slate-200/80 rounded-xl p-2.5 flex items-center justify-between">
                  <div className="flex items-center gap-2.5">
                    <span className="text-xl">🛢️</span>
                    <div>
                      <div className="text-xs font-bold text-slate-900">Minyak Jelantah Dapur</div>
                      <div className="text-[10px] text-slate-500">Saring ampas, masukkan jeriken/botol</div>
                    </div>
                  </div>
                  <div className="text-right">
                    <div className="text-xs font-extrabold text-emerald-700">Rp 7.000/liter</div>
                    <div className="text-[9px] text-slate-400 font-bold">Stabil</div>
                  </div>
                </div>

                <div className="bg-slate-50 border border-slate-200/80 rounded-xl p-2.5 flex items-center justify-between">
                  <div className="flex items-center gap-2.5">
                    <span className="text-xl">🥫</span>
                    <div>
                      <div className="text-xs font-bold text-slate-900">Kaleng Aluminium &amp; Besi</div>
                      <div className="text-[10px] text-slate-500">Bebas residu makanan basah</div>
                    </div>
                  </div>
                  <div className="text-right">
                    <div className="text-xs font-extrabold text-emerald-700">Rp 5.500/kg</div>
                    <div className="text-[9px] text-emerald-600 font-bold">▲ +3%</div>
                  </div>
                </div>

                <div className="bg-slate-50 border border-slate-200/80 rounded-xl p-2.5 flex items-center justify-between">
                  <div className="flex items-center gap-2.5">
                    <span className="text-xl">🥬</span>
                    <div>
                      <div className="text-xs font-bold text-slate-900">Sisa Organik &amp; Sayur</div>
                      <div className="text-[10px] text-slate-500">Bahan baku kompos mitra RW</div>
                    </div>
                  </div>
                  <div className="text-right">
                    <div className="text-xs font-extrabold text-emerald-700">Rp 800/kg</div>
                    <div className="text-[9px] text-emerald-600 font-bold">▲ +2%</div>
                  </div>
                </div>
              </div>

              {/* Residue Warning */}
              <div className="bg-amber-50 border border-amber-200/90 rounded-xl p-2.5 text-[10px] text-amber-900 leading-tight">
                ⚠️ <strong>Catatan:</strong> Sampah plastik yang berlemak/berminyak pekat atau popok sekali pakai tergolong <em>residu</em> dan tidak dapat didaur ulang menjadi saldo.
              </div>
            </div>
          )}
        </div>

        {/* Modal Footer Action */}
        <div className="p-4 bg-slate-50 border-t border-slate-100 flex gap-2">
          <button
            onClick={() => {
              onClose();
              if (onOpenAuth) onOpenAuth('login');
            }}
            className="flex-1 py-3 px-3 rounded-xl border border-slate-200 bg-white hover:bg-slate-100 text-slate-700 font-bold text-xs transition cursor-pointer flex items-center justify-center gap-1.5"
          >
            <span>Masuk / Akun</span>
          </button>
          <button
            onClick={onClose}
            className="flex-1 py-3 px-4 rounded-xl bg-emerald-600 hover:bg-emerald-700 active:scale-95 text-white font-bold text-xs transition shadow-md shadow-emerald-700/20 cursor-pointer flex items-center justify-center gap-1.5"
          >
            <span>Mulai Sekarang</span>
            <ArrowRight className="w-3.5 h-3.5" />
          </button>
        </div>
      </div>
    </div>
  );
}
