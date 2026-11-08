import React, { useState } from 'react';
import {
  Recycle,
  User,
  Mail,
  Lock,
  Smartphone,
  MapPin,
  Building2,
  CheckCircle2,
  X,
  ArrowRight,
  ShieldCheck,
  Sparkles,
  LogIn,
  UserPlus
} from 'lucide-react';

export default function AuthModal({
  isOpen,
  initialMode = 'login',
  onClose,
  onLoginSuccess,
  showToast
}) {
  const [mode, setMode] = useState(initialMode); // 'login' or 'register'

  // Login Form State
  const [loginIdentifier, setLoginIdentifier] = useState('raka@pilahin.id');
  const [loginPassword, setLoginPassword] = useState('password123');

  // Register Form State
  const [regName, setRegName] = useState('');
  const [regPhone, setRegPhone] = useState('');
  const [regEmail, setRegEmail] = useState('');
  const [regPassword, setRegPassword] = useState('');
  const [regRole, setRegRole] = useState('warga'); // 'warga' or 'mitra'
  const [regAddress, setRegAddress] = useState('');
  const [regBenchmark, setRegBenchmark] = useState('');

  if (!isOpen) return null;

  // Handle standard submit
  const handleLoginSubmit = (e) => {
    e.preventDefault();
    if (!loginIdentifier.trim() || !loginPassword.trim()) {
      showToast('Mohon isi email/nomor HP dan password!');
      return;
    }

    // Authenticate user
    const user = {
      id: 'usr-' + Date.now(),
      name: loginIdentifier.includes('sri') || loginIdentifier.includes('mitra') ? 'Ibu Sri Mulyani' : 'Raka Pradipta',
      email: loginIdentifier,
      phone: '0812-3456-7890',
      role: loginIdentifier.includes('sri') || loginIdentifier.includes('mitra') ? 'mitra' : 'warga',
      avatar: loginIdentifier.includes('sri') || loginIdentifier.includes('mitra') ? 'SM' : 'RP',
      primaryAddress: 'Jl. Cemara No. 14, RT 03/RW 05, Cilandak Barat',
      addressBenchmark: 'Pagar hitam depan warung Bu Titin, sampah di teras depan',
      userRank: 'Pahlawan Hijau Level 3'
    };

    onLoginSuccess(user);
    showToast(`Selamat datang kembali, ${user.name}!`);
    onClose();
  };

  const handleRegisterSubmit = (e) => {
    e.preventDefault();
    if (!regName.trim() || !regPhone.trim() || !regPassword.trim()) {
      showToast('Mohon lengkapi nama, nomor WhatsApp, dan password!');
      return;
    }

    const newUser = {
      id: 'usr-' + Date.now(),
      name: regName.trim(),
      email: regEmail.trim() || `${regPhone.replace(/\D/g, '')}@pilahin.id`,
      phone: regPhone.trim(),
      role: regRole,
      avatar: regName.trim().slice(0, 2).toUpperCase(),
      primaryAddress: regAddress.trim() || 'Jl. Danau Tamblingan No. 42, Sanur',
      addressBenchmark: regBenchmark.trim() || 'Sampah di teras depan',
      userRank: 'Warga Pemilah Pemula (Level 1)'
    };

    onLoginSuccess(newUser);
    showToast(`Akun berhasil dibuat! Selamat datang di Pilah.in, ${newUser.name}!`);
    onClose();
  };

  // Quick 1-Click Demo Profiles
  const handleDemoLogin = (profileType) => {
    if (profileType === 'warga') {
      const user = {
        id: 'usr-raka',
        name: 'Raka Pradipta',
        email: 'raka@pilahin.id',
        phone: '0812-3456-7890',
        role: 'warga',
        avatar: 'RP',
        primaryAddress: 'Jl. Cemara No. 14, RT 03/RW 05, Cilandak Barat',
        addressBenchmark: 'Pagar hitam depan warung Bu Titin, sampah di teras depan',
        userRank: 'Pahlawan Hijau Level 3'
      };
      onLoginSuccess(user);
      showToast('Masuk sebagai Warga: Raka Pradipta');
    } else {
      const user = {
        id: 'usr-sri',
        name: 'Ibu Sri Mulyani',
        email: 'sri@banksampah05.id',
        phone: '0813-8899-7711',
        role: 'mitra',
        avatar: 'SM',
        primaryAddress: 'Pos Bank Sampah Berkah Lestari, Balai Warga RW 05',
        addressBenchmark: 'Samping pos satpam utama',
        userRank: 'Pengurus Utama Bank Sampah'
      };
      onLoginSuccess(user);
      showToast('Masuk sebagai Mitra: Ibu Sri (Bank Sampah RW 05)');
    }
    onClose();
  };

  return (
    <div className="fixed inset-0 z-50 bg-slate-950/75 backdrop-blur-xs flex items-center justify-center p-3 sm:p-4 overflow-y-auto">
      <div className="w-full max-w-sm max-h-[92dvh] overflow-y-auto overscroll-contain bg-white rounded-3xl p-5 shadow-2xl border border-slate-200 text-slate-900 space-y-4 animate-in fade-in zoom-in-95 duration-200">
        
        {/* Modal Header */}
        <div className="flex items-center justify-between pb-2 border-b border-slate-100">
          <div className="flex items-center gap-2">
            <div className="w-7 h-7 rounded-xl bg-gradient-to-tr from-emerald-600 to-teal-500 text-white flex items-center justify-center shadow-xs">
              <Recycle className="w-4 h-4" />
            </div>
            <div>
              <h3 className="text-sm font-extrabold text-slate-900 tracking-tight">
                {mode === 'login' ? 'Masuk ke Pilah.in' : 'Daftar Akun Baru'}
              </h3>
              <p className="text-[10px] text-slate-500">
                {mode === 'login' ? 'Kelola saldo & transaksi sirkularmu' : 'Mulai pilah & ubah sampah jadi rupiah'}
              </p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="w-8 h-8 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-500 hover:text-slate-800 flex items-center justify-center transition cursor-pointer"
            aria-label="Tutup"
          >
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* Mode Toggle Pills */}
        <div className="grid grid-cols-2 gap-1 bg-slate-100 p-1 rounded-2xl text-xs font-bold">
          <button
            type="button"
            onClick={() => setMode('login')}
            className={`py-2 rounded-xl transition cursor-pointer text-center flex items-center justify-center gap-1.5 ${
              mode === 'login'
                ? 'bg-white text-emerald-800 shadow-xs'
                : 'text-slate-500 hover:text-slate-900'
            }`}
          >
            <LogIn className="w-3.5 h-3.5" />
            <span>Masuk</span>
          </button>
          <button
            type="button"
            onClick={() => setMode('register')}
            className={`py-2 rounded-xl transition cursor-pointer text-center flex items-center justify-center gap-1.5 ${
              mode === 'register'
                ? 'bg-white text-emerald-800 shadow-xs'
                : 'text-slate-500 hover:text-slate-900'
            }`}
          >
            <UserPlus className="w-3.5 h-3.5" />
            <span>Daftar Akun</span>
          </button>
        </div>

        {/* 1-Click Fast Demo Logins */}
        <div className="bg-emerald-50/60 border border-emerald-200/80 rounded-2xl p-3 space-y-1.5">
          <span className="text-[10px] font-bold uppercase tracking-wider text-emerald-800 block">
            ⚡ Masuk Cepat (Akun Demo Langsung)
          </span>
          <div className="grid grid-cols-2 gap-2">
            <button
              type="button"
              onClick={() => handleDemoLogin('warga')}
              className="bg-white hover:bg-emerald-100/60 border border-emerald-300 text-emerald-900 text-[11px] font-bold py-2 px-2.5 rounded-xl transition cursor-pointer text-left active:scale-95 shadow-2xs"
            >
              <div className="flex items-center gap-1">
                <span className="w-2 h-2 rounded-full bg-emerald-500"></span>
                <span>Warga Penyetor</span>
              </div>
              <p className="text-[9px] text-slate-500 mt-0.5 truncate">Raka Pradipta</p>
            </button>
            <button
              type="button"
              onClick={() => handleDemoLogin('mitra')}
              className="bg-white hover:bg-amber-100/60 border border-amber-300 text-amber-900 text-[11px] font-bold py-2 px-2.5 rounded-xl transition cursor-pointer text-left active:scale-95 shadow-2xs"
            >
              <div className="flex items-center gap-1">
                <span className="w-2 h-2 rounded-full bg-amber-500"></span>
                <span>Mitra Bank Sampah</span>
              </div>
              <p className="text-[9px] text-slate-500 mt-0.5 truncate">Ibu Sri (RW 05)</p>
            </button>
          </div>
        </div>

        {/* MODE: LOGIN FORM */}
        {mode === 'login' ? (
          <form onSubmit={handleLoginSubmit} className="space-y-3">
            <div>
              <label className="text-[11px] font-bold text-slate-700 block mb-1">
                Email atau No. WhatsApp:
              </label>
              <div className="relative">
                <Mail className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
                <input
                  type="text"
                  value={loginIdentifier}
                  onChange={(e) => setLoginIdentifier(e.target.value)}
                  placeholder="contoh: raka@pilahin.id atau 081234..."
                  className="w-full text-xs font-semibold pl-9 pr-3 py-2.5 bg-slate-50 border border-slate-300 rounded-xl focus:outline-none focus:border-emerald-500 text-slate-900"
                  required
                />
              </div>
            </div>

            <div>
              <label className="text-[11px] font-bold text-slate-700 block mb-1">
                Password:
              </label>
              <div className="relative">
                <Lock className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
                <input
                  type="password"
                  value={loginPassword}
                  onChange={(e) => setLoginPassword(e.target.value)}
                  placeholder="••••••••"
                  className="w-full text-xs font-semibold pl-9 pr-3 py-2.5 bg-slate-50 border border-slate-300 rounded-xl focus:outline-none focus:border-emerald-500 text-slate-900"
                  required
                />
              </div>
            </div>

            <button
              type="submit"
              className="w-full bg-emerald-600 hover:bg-emerald-700 active:scale-95 text-white font-bold text-xs py-3 rounded-xl transition shadow-md shadow-emerald-700/20 cursor-pointer flex items-center justify-center gap-1.5 mt-2"
            >
              <LogIn className="w-4 h-4" />
              <span>Masuk ke Akun</span>
            </button>

            <p className="text-center text-[11px] text-slate-500 pt-1">
              Belum punya akun?{' '}
              <button
                type="button"
                onClick={() => setMode('register')}
                className="text-emerald-700 font-bold hover:underline cursor-pointer"
              >
                Daftar Sekarang
              </button>
            </p>
          </form>
        ) : (
          /* MODE: REGISTER FORM */
          <form onSubmit={handleRegisterSubmit} className="space-y-3">
            <div>
              <label className="text-[11px] font-bold text-slate-700 block mb-1">
                Nama Lengkap:
              </label>
              <div className="relative">
                <User className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
                <input
                  type="text"
                  value={regName}
                  onChange={(e) => setRegName(e.target.value)}
                  placeholder="contoh: Raka Pradipta"
                  className="w-full text-xs font-semibold pl-9 pr-3 py-2.5 bg-slate-50 border border-slate-300 rounded-xl focus:outline-none focus:border-emerald-500 text-slate-900"
                  required
                />
              </div>
            </div>

            <div className="grid grid-cols-2 gap-2">
              <div>
                <label className="text-[11px] font-bold text-slate-700 block mb-1">
                  No. WhatsApp Aktif:
                </label>
                <div className="relative">
                  <Smartphone className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
                  <input
                    type="tel"
                    value={regPhone}
                    onChange={(e) => setRegPhone(e.target.value)}
                    placeholder="0812-xxxx"
                    className="w-full text-xs font-semibold pl-9 pr-2.5 py-2.5 bg-slate-50 border border-slate-300 rounded-xl focus:outline-none focus:border-emerald-500 text-slate-900"
                    required
                  />
                </div>
              </div>
              <div>
                <label className="text-[11px] font-bold text-slate-700 block mb-1">
                  Email (Opsional):
                </label>
                <div className="relative">
                  <Mail className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
                  <input
                    type="email"
                    value={regEmail}
                    onChange={(e) => setRegEmail(e.target.value)}
                    placeholder="email@..."
                    className="w-full text-xs font-semibold pl-9 pr-2.5 py-2.5 bg-slate-50 border border-slate-300 rounded-xl focus:outline-none focus:border-emerald-500 text-slate-900"
                  />
                </div>
              </div>
            </div>

            <div>
              <label className="text-[11px] font-bold text-slate-700 block mb-1">
                Password:
              </label>
              <div className="relative">
                <Lock className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
                <input
                  type="password"
                  value={regPassword}
                  onChange={(e) => setRegPassword(e.target.value)}
                  placeholder="Minimal 6 karakter"
                  className="w-full text-xs font-semibold pl-9 pr-3 py-2.5 bg-slate-50 border border-slate-300 rounded-xl focus:outline-none focus:border-emerald-500 text-slate-900"
                  required
                />
              </div>
            </div>

            {/* Role Selection */}
            <div>
              <label className="text-[11px] font-bold text-slate-700 block mb-1">
                Daftar Sebagai Peran:
              </label>
              <div className="grid grid-cols-2 gap-2">
                <button
                  type="button"
                  onClick={() => setRegRole('warga')}
                  className={`py-2 px-3 rounded-xl border text-xs font-bold text-left transition cursor-pointer ${
                    regRole === 'warga'
                      ? 'border-emerald-500 bg-emerald-50 text-emerald-800'
                      : 'border-slate-200 text-slate-600 hover:bg-slate-50'
                  }`}
                >
                  <div className="flex items-center gap-1.5">
                    <User className="w-3.5 h-3.5 text-emerald-600" />
                    <span>Warga Penyetor</span>
                  </div>
                </button>
                <button
                  type="button"
                  onClick={() => setRegRole('mitra')}
                  className={`py-2 px-3 rounded-xl border text-xs font-bold text-left transition cursor-pointer ${
                    regRole === 'mitra'
                      ? 'border-amber-500 bg-amber-50 text-amber-900'
                      : 'border-slate-200 text-slate-600 hover:bg-slate-50'
                  }`}
                >
                  <div className="flex items-center gap-1.5">
                    <Building2 className="w-3.5 h-3.5 text-amber-600" />
                    <span>Pengelola Bank Sampah</span>
                  </div>
                </button>
              </div>
            </div>

            {/* Address fields right in register! */}
            <div>
              <label className="text-[11px] font-bold text-slate-700 block mb-1">
                Alamat Utama Penjemputan Sampah:
              </label>
              <div className="relative">
                <MapPin className="w-4 h-4 text-slate-400 absolute left-3 top-3" />
                <textarea
                  rows={2}
                  value={regAddress}
                  onChange={(e) => setRegAddress(e.target.value)}
                  placeholder="Nama jalan, nomor rumah, RT/RW, kelurahan..."
                  className="w-full text-xs font-semibold pl-9 pr-3 py-2 bg-slate-50 border border-slate-300 rounded-xl focus:outline-none focus:border-emerald-500 text-slate-900 resize-none"
                />
              </div>
            </div>

            <div>
              <label className="text-[11px] font-bold text-slate-700 block mb-1">
                Patokan Rumah (untuk Kurir Armada):
              </label>
              <input
                type="text"
                value={regBenchmark}
                onChange={(e) => setRegBenchmark(e.target.value)}
                placeholder="contoh: Pagar hitam samping warung, seberang masjid"
                className="w-full text-xs font-semibold px-3 py-2 bg-slate-50 border border-slate-300 rounded-xl focus:outline-none focus:border-emerald-500 text-slate-900"
              />
            </div>

            <button
              type="submit"
              className="w-full bg-emerald-600 hover:bg-emerald-700 active:scale-95 text-white font-bold text-xs py-3 rounded-xl transition shadow-md shadow-emerald-700/20 cursor-pointer flex items-center justify-center gap-1.5 mt-2"
            >
              <UserPlus className="w-4 h-4" />
              <span>Daftar Sekarang</span>
            </button>

            <p className="text-center text-[11px] text-slate-500 pt-1">
              Sudah punya akun?{' '}
              <button
                type="button"
                onClick={() => setMode('login')}
                className="text-emerald-700 font-bold hover:underline cursor-pointer"
              >
                Masuk di Sini
              </button>
            </p>
          </form>
        )}
      </div>
    </div>
  );
}
