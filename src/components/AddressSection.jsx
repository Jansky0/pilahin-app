import React, { useState } from 'react';
import {
  MapPin,
  Building2,
  Edit3,
  Check,
  Plus,
  Truck,
  CheckCircle2,
  AlertCircle,
  Phone,
  User,
  Home,
  Briefcase,
  Compass,
  X
} from 'lucide-react';

export default function AddressSection({
  depositMethod,
  pickupAddress,
  setPickupAddress,
  activeAddress,
  setActiveAddress,
  savedAddresses,
  setSavedAddresses,
  selectedPartner,
  onOpenPartnerSelect,
  showToast
}) {
  const [isEditingAddress, setIsEditingAddress] = useState(false);
  const [showNewAddressForm, setShowNewAddressForm] = useState(false);

  // Form edit state
  const [editLabel, setEditLabel] = useState(activeAddress?.label || 'Rumah');
  const [editRecipient, setEditRecipient] = useState(activeAddress?.recipient || 'Raka Pradipta');
  const [editPhone, setEditPhone] = useState(activeAddress?.phone || '0812-3456-7890');
  const [editStreet, setEditStreet] = useState(activeAddress?.street || 'Jl. Cemara No. 14, RT 03/RW 05');
  const [editBenchmark, setEditBenchmark] = useState(activeAddress?.benchmark || 'Pagar hitam depan warung Bu Titin, sampah di teras depan');
  const [editSubDistrict, setEditSubDistrict] = useState(activeAddress?.subDistrict || 'Cilandak Barat, Jakarta Selatan');

  // Switch active saved address
  const handleSelectSavedAddress = (addr) => {
    setActiveAddress(addr);
    setEditLabel(addr.label);
    setEditRecipient(addr.recipient);
    setEditPhone(addr.phone);
    setEditStreet(addr.street);
    setEditBenchmark(addr.benchmark);
    setEditSubDistrict(addr.subDistrict);

    const fullStr = `${addr.street}, ${addr.subDistrict} (${addr.recipient} - ${addr.phone})`;
    setPickupAddress(fullStr);
    showToast(`Alamat penjemputan beralih ke: ${addr.label}`);
  };

  // Save changes to current address
  const handleSaveAddress = (e) => {
    e.preventDefault();
    if (!editStreet.trim() || !editRecipient.trim() || !editPhone.trim()) {
      showToast('Mohon lengkapi nama, nomor HP, dan alamat jalan!');
      return;
    }

    const updatedAddr = {
      ...activeAddress,
      label: editLabel.trim() || 'Alamat',
      recipient: editRecipient.trim(),
      phone: editPhone.trim(),
      street: editStreet.trim(),
      benchmark: editBenchmark.trim(),
      subDistrict: editSubDistrict.trim()
    };

    setActiveAddress(updatedAddr);

    // Update in savedAddresses list
    setSavedAddresses(prev =>
      prev.map(a => (a.id === updatedAddr.id ? updatedAddr : a))
    );

    const fullStr = `${updatedAddr.street}, ${updatedAddr.subDistrict} (${updatedAddr.recipient} - ${updatedAddr.phone})`;
    setPickupAddress(fullStr);

    setIsEditingAddress(false);
    showToast('Alamat penjemputan berhasil diperbarui & disimpan!');
  };

  // Create brand new address
  const handleCreateNewAddress = (e) => {
    e.preventDefault();
    if (!editStreet.trim() || !editRecipient.trim() || !editPhone.trim()) {
      showToast('Mohon lengkapi nama, nomor HP, dan alamat jalan!');
      return;
    }

    const newId = 'addr-' + Date.now();
    const newAddr = {
      id: newId,
      label: editLabel.trim() || 'Alamat Baru',
      recipient: editRecipient.trim(),
      phone: editPhone.trim(),
      street: editStreet.trim(),
      benchmark: editBenchmark.trim(),
      subDistrict: editSubDistrict.trim(),
      isDefault: false
    };

    setSavedAddresses(prev => [...prev, newAddr]);
    setActiveAddress(newAddr);

    const fullStr = `${newAddr.street}, ${newAddr.subDistrict} (${newAddr.recipient} - ${newAddr.phone})`;
    setPickupAddress(fullStr);

    setShowNewAddressForm(false);
    setIsEditingAddress(false);
    showToast(`Alamat baru "${newAddr.label}" berhasil ditambahkan!`);
  };

  return (
    <div className="space-y-3">
      {/* MODE 1: PICKUP ARMADA TOSSA (ALAMAT PENJEMPUTAN) */}
      {depositMethod === 'pickup' ? (
        <div className="bg-white rounded-2xl p-4 border border-slate-200/90 shadow-xs space-y-3">
          {/* Header Row */}
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2">
              <div className="w-8 h-8 rounded-xl bg-emerald-100 text-emerald-800 flex items-center justify-center font-bold text-xs flex-shrink-0">
                <MapPin className="w-4 h-4" />
              </div>
              <div>
                <span className="text-[10px] font-bold uppercase tracking-wider text-slate-500 block">
                  Alamat Jemput:
                </span>
                <h4 className="text-xs font-bold text-slate-900 flex items-center gap-1.5">
                  <span>{activeAddress?.label || 'Rumah'}</span>
                  <span className="text-[10px] bg-emerald-100 text-emerald-800 px-1.5 py-0.2 rounded font-semibold">
                    Terverifikasi
                  </span>
                </h4>
              </div>
            </div>

            <button
              type="button"
              onClick={() => setIsEditingAddress(!isEditingAddress)}
              className="text-xs font-bold text-emerald-700 hover:text-emerald-800 bg-emerald-50 hover:bg-emerald-100 px-3 py-1.5 rounded-xl border border-emerald-200 transition cursor-pointer active:scale-95 flex items-center gap-1"
            >
              <Edit3 className="w-3.5 h-3.5" />
              <span>{isEditingAddress ? 'Tutup' : 'Ubah Alamat'}</span>
            </button>
          </div>

          {/* Quick Saved Address Chips */}
          <div className="space-y-1.5 pt-1">
            <div className="flex items-center justify-between text-[11px] text-slate-500 font-semibold">
              <span>Pilih Alamat Tersimpan:</span>
              <button
                type="button"
                onClick={() => {
                  setShowNewAddressForm(true);
                  setIsEditingAddress(true);
                  setEditLabel('');
                  setEditStreet('');
                  setEditBenchmark('');
                }}
                className="text-emerald-700 font-bold hover:underline flex items-center gap-0.5 text-[10px] cursor-pointer"
              >
                <Plus className="w-3 h-3" />
                <span>+ Tambah Baru</span>
              </button>
            </div>

            <div className="flex gap-1.5 overflow-x-auto pb-1 no-scrollbar">
              {savedAddresses.map((addr) => {
                const isSelected = activeAddress?.id === addr.id;
                return (
                  <button
                    key={addr.id}
                    type="button"
                    onClick={() => handleSelectSavedAddress(addr)}
                    className={`px-3 py-1.5 rounded-xl text-xs font-bold flex items-center gap-1.5 transition flex-shrink-0 cursor-pointer ${
                      isSelected
                        ? 'bg-emerald-600 text-white shadow-xs'
                        : 'bg-slate-50 hover:bg-slate-100 text-slate-600 border border-slate-200'
                    }`}
                  >
                    {addr.label.toLowerCase().includes('rumah') ? (
                      <Home className="w-3 h-3" />
                    ) : addr.label.toLowerCase().includes('kantor') ? (
                      <Briefcase className="w-3 h-3" />
                    ) : (
                      <MapPin className="w-3 h-3" />
                    )}
                    <span>{addr.label}</span>
                    {isSelected && <Check className="w-3 h-3" />}
                  </button>
                );
              })}
            </div>
          </div>

          {/* Card Detail Alamat Aktif */}
          {!isEditingAddress ? (
            <div className="bg-slate-50 rounded-xl p-3 border border-slate-200/80 space-y-1.5">
              <div className="flex items-center justify-between text-[11px]">
                <div className="font-bold text-slate-900 flex items-center gap-1.5">
                  <User className="w-3 h-3 text-slate-500" />
                  <span>{activeAddress?.recipient || 'Raka Pradipta'}</span>
                </div>
                <div className="text-slate-600 font-semibold flex items-center gap-1">
                  <Phone className="w-3 h-3 text-slate-400" />
                  <span>{activeAddress?.phone || '0812-3456-7890'}</span>
                </div>
              </div>

              {/* Exact full address line (Test & user compatible) */}
              <p className="text-xs font-bold text-slate-900 leading-snug">
                {pickupAddress}
              </p>

              {activeAddress?.benchmark && (
                <div className="bg-white/80 p-2 rounded-lg border border-slate-200/60 text-[11px] text-slate-700 flex items-start gap-1.5">
                  <Compass className="w-3.5 h-3.5 text-amber-600 flex-shrink-0 mt-0.5" />
                  <div>
                    <span className="font-bold text-slate-800">Patokan Rumah: </span>
                    <span>{activeAddress.benchmark}</span>
                  </div>
                </div>
              )}

              <div className="pt-1 flex items-center gap-1.5 text-[10px] text-emerald-700 font-medium">
                <Truck className="w-3.5 h-3.5 flex-shrink-0" />
                <span>Armada Motor Roda Tiga Tossa jemput &amp; timbang di alamat ini</span>
              </div>
            </div>
          ) : (
            /* FORMULIR EDIT / INPUT ALAMAT LENGKAP */
            <form
              onSubmit={showNewAddressForm ? handleCreateNewAddress : handleSaveAddress}
              className="bg-slate-50 rounded-2xl p-3.5 border border-emerald-200 space-y-3"
            >
              <div className="flex items-center justify-between text-xs font-bold text-slate-900 pb-1 border-b border-slate-200">
                <span>{showNewAddressForm ? '📝 Input Alamat Penjemputan Baru' : '✏️ Edit Detail Alamat Penjemputan'}</span>
                <button
                  type="button"
                  onClick={() => {
                    setIsEditingAddress(false);
                    setShowNewAddressForm(false);
                  }}
                  className="text-slate-400 hover:text-slate-700 cursor-pointer"
                >
                  <X className="w-4 h-4" />
                </button>
              </div>

              <div className="grid grid-cols-2 gap-2">
                <div>
                  <label className="text-[10px] font-bold text-slate-600 block mb-0.5">
                    Label Alamat:
                  </label>
                  <input
                    type="text"
                    value={editLabel}
                    onChange={(e) => setEditLabel(e.target.value)}
                    placeholder="Rumah, Kantor, Kos..."
                    className="w-full text-xs font-semibold p-2 bg-white border border-slate-300 rounded-lg focus:outline-none focus:border-emerald-500"
                    required
                  />
                </div>
                <div>
                  <label className="text-[10px] font-bold text-slate-600 block mb-0.5">
                    Nama Kontak Penjemputan:
                  </label>
                  <input
                    type="text"
                    value={editRecipient}
                    onChange={(e) => setEditRecipient(e.target.value)}
                    placeholder="Nama penerima..."
                    className="w-full text-xs font-semibold p-2 bg-white border border-slate-300 rounded-lg focus:outline-none focus:border-emerald-500"
                    required
                  />
                </div>
              </div>

              <div>
                <label className="text-[10px] font-bold text-slate-600 block mb-0.5">
                  Nomor WhatsApp Aktif (Kurir Konfirmasi ke sini):
                </label>
                <input
                  type="tel"
                  value={editPhone}
                  onChange={(e) => setEditPhone(e.target.value)}
                  placeholder="0812-3456-xxxx"
                  className="w-full text-xs font-semibold p-2 bg-white border border-slate-300 rounded-lg focus:outline-none focus:border-emerald-500"
                  required
                />
              </div>

              <div>
                <label className="text-[10px] font-bold text-slate-600 block mb-0.5">
                  Alamat Lengkap &amp; Nomor Rumah (Akses Motor Tossa):
                </label>
                <textarea
                  rows={2}
                  value={editStreet}
                  onChange={(e) => setEditStreet(e.target.value)}
                  placeholder="Jl. Cemara No. 14, RT 03/RW 05, Kelurahan..."
                  className="w-full text-xs font-semibold p-2 bg-white border border-slate-300 rounded-lg focus:outline-none focus:border-emerald-500 resize-none"
                  required
                />
              </div>

              <div>
                <label className="text-[10px] font-bold text-slate-600 block mb-0.5">
                  Patokan Rumah / Lokasi Sampah Ditaruh:
                </label>
                <input
                  type="text"
                  value={editBenchmark}
                  onChange={(e) => setEditBenchmark(e.target.value)}
                  placeholder="Contoh: Pagar hitam depan warung, sampah sudah di karung depan garasi"
                  className="w-full text-xs font-semibold p-2 bg-white border border-slate-300 rounded-lg focus:outline-none focus:border-emerald-500"
                />
                <p className="text-[9px] text-slate-400 mt-0.5">
                  💡 Membantu driver motor roda tiga Tossa menemukan lokasi dengan cepat tanpa tersesat.
                </p>
              </div>

              <div className="flex gap-2 pt-1">
                <button
                  type="button"
                  onClick={() => {
                    setIsEditingAddress(false);
                    setShowNewAddressForm(false);
                  }}
                  className="flex-1 py-2 rounded-xl border border-slate-200 bg-white hover:bg-slate-100 text-slate-600 font-bold text-xs transition cursor-pointer"
                >
                  Batal
                </button>
                <button
                  type="submit"
                  className="flex-1 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-700 active:scale-95 text-white font-bold text-xs transition shadow-xs cursor-pointer flex items-center justify-center gap-1"
                >
                  <CheckCircle2 className="w-3.5 h-3.5" />
                  <span>{showNewAddressForm ? 'Simpan Alamat Baru' : 'Simpan Perubahan'}</span>
                </button>
              </div>
            </form>
          )}
        </div>
      ) : (
        /* MODE 2: ANTHAR SENDIRI (LOKASI BANK SAMPAH / POS PENGEPUL) */
        <div className="bg-white rounded-2xl p-4 border border-slate-200/90 shadow-xs flex items-center justify-between">
          <div className="flex items-start gap-2.5">
            <div className="w-8 h-8 rounded-xl bg-teal-100 text-teal-800 flex items-center justify-center flex-shrink-0 mt-0.5">
              <Building2 className="w-4 h-4" />
            </div>
            <div>
              <p className="text-[10px] font-bold uppercase tracking-wider text-slate-500">
                Lokasi Pengepul / Drop-off:
              </p>
              <p className="text-xs font-bold text-slate-900 mt-0.5 leading-snug">
                {selectedPartner}
              </p>
              <p className="text-[10px] text-slate-500 mt-0.5">
                Bawa sampahmu ke pos ini • Ditimbang di timbangan pos mitra (100% Saldo Utuh)
              </p>
            </div>
          </div>
          <button
            type="button"
            onClick={onOpenPartnerSelect}
            className="text-xs font-bold text-teal-700 hover:text-teal-800 bg-teal-50 hover:bg-teal-100 px-3 py-1.5 rounded-xl border border-teal-200 transition cursor-pointer active:scale-95 flex-shrink-0"
          >
            Ganti
          </button>
        </div>
      )}
    </div>
  );
}
