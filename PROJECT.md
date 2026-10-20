# Project: Pilah.in Overhaul

## Architecture
Pilah.in is a modern waste management and circular economy progressive web application built with React 18, Vite, and Tailwind CSS v4.
The overhaul transforms the app into a "Fresh Eco-Tech" digital product inspired by contemporary fintech (GoPay, Revolut) and modern circular apps (Rekosistem, Octopus, Dribbble/Lovable aesthetic).

### Core Circular Loop Data Flow:
```
[Warga: Pilah Sampah] 
       │
       ▼
[Setor Sampah (Drop-Off / Pickup)] ───► [Tiket Digital PLH-XXXXXX]
                                                  │
                                                  ▼
                                       [Mitra: Timbang & Verifikasi]
                                                  │
                                                  ▼
[Belanja Toko Sirkular] ◄── [Dompet Saldo Mengendap] ──► [Tarik Saldo e-Wallet]
(Potong saldo instan)       (Mutasi Real-time)           (GoPay / DANA)
```

### Module Boundaries:
- `src/App.jsx`: Main application container, role router (Warga vs Mitra), global reactive state.
- `src/index.css`: Tailwind CSS v4 import, `@theme` design tokens (Plus Jakarta Sans, Inter, Fresh Eco-Tech palette).
- `src/lib/utils.js`: Class merging utilities (`clsx`, `twMerge` or equivalent).
- `e2e_tests/`: End-to-end test runner and specification test cases (Tiers 1-4).

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | Leaderboard Elimination | Hapus total Papan Peringkat RW dari beranda warga | M1 | ORIGINAL_REQUEST R2, Explorer 2 (DONE) |
| 2 | Header Switcher Elimination | Hapus role-switcher pill dan frame mode dari header | M1 | ORIGINAL_REQUEST R2, Explorer 1, 2, 3 (DONE) |
| 3 | Clean Role Separation | Portal Mitra diakses bersih via Profil Warga; tombol tegas "Kembali ke Warga" | M1 | ORIGINAL_REQUEST R2, Explorer 2 (DONE) |
| 4 | Penyetoran Terpilah | Pilihan Drop-off & Pickup, kalkulator live harga komoditas, tiket digital PLH-XXXXXX | M2 | ORIGINAL_REQUEST R2, Explorer 2 (DONE) |
| 5 | Timbangan Mitra Simulator | Verifikasi dan timbang tiket oleh Mitra untuk kredit saldo otomatis | M2 | ORIGINAL_REQUEST R2, Explorer 2 (DONE) |
| 6 | Dompet Saldo Mengendap | Saldo rupiah transparan, indikator pending/settled, mutasi riwayat kredit/debit | M2 | ORIGINAL_REQUEST R2, Explorer 2 (DONE) |
| 7 | Penarikan e-Wallet | Form pencairan saldo instan ke GoPay & DANA dengan validasi saldo minimum | M2 | ORIGINAL_REQUEST R2, Explorer 2 (DONE) |
| 8 | Toko Sirkular Mitra | Katalog produk daur ulang, harga spesial saldo sampah, checkout potong saldo | M2 | ORIGINAL_REQUEST R2, Explorer 2 (DONE) |
| 9 | Design Tokens & Theme | Setup token Tailwind v4 di index.css: font Plus Jakarta Sans, Inter, warna eco-tech | M3 | ORIGINAL_REQUEST R3, Explorer 1, 3 (DONE) |
| 10 | Modern Bento Cards & UI | Redesain Beranda: Hero Wallet Card, 4-button Action Hub, Personal Eco-Impact | M3 | ORIGINAL_REQUEST R3, Explorer 1 (DONE) |
| 11 | Mobile Ergonomics (360-430px)| Container max-w-md responsif, touch target >=44px, no double scroll, no header wrap | M3 | ORIGINAL_REQUEST R3, Explorer 3 (DONE) |
| 12 | Zero-CLS Bottom Navbar | Fixed 4-column navigation (Beranda, Setor, Toko, Dompet) tanpa horizontal jitter | M3 | ORIGINAL_REQUEST R3, Explorer 3 (DONE) |
| 13 | Responsive Scrollable Modals | Max-height 90dvh dengan overflow-y-auto untuk modal setor, tiket, belanja, tarik saldo | M3 | ORIGINAL_REQUEST R3, Explorer 3 (DONE) |
| 14 | E2E Test Suite Creation | Opaque-box automated test harness covering Tiers 1-4 requirements | E2E-Track | ORIGINAL_REQUEST R4 (DONE) |
| 15 | End-to-End Verification | Build pass (npm run build) & verifikasi transaksi 100% lancar di localhost:3000 | M4 | ORIGINAL_REQUEST R4 (DONE) |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | Fitur Refactor: Clean Roles & Leaderboard Removal | Features 1, 2, 3 | none | DONE |
| E2E | E2E Test Suite Track | Feature 14 (Tiers 1-4) | none | DONE |
| M2 | Core Circular Loop Architecture & State | Features 4, 5, 6, 7, 8 | M1 | DONE |
| M3 | UI & Visual Design System Overhaul | Features 9, 10, 11, 12, 13 | M2 | DONE |
| M4 | Final Milestone: 100% E2E Pass & Verification | Feature 15 | M3, E2E | DONE |

## Interface Contracts
### Warga ↔ Mitra Navigation Contract
- State `currentRole`: `'citizen'` | `'partner'`. Default: `'citizen'`.
- Citizen enters Partner mode strictly via User Profile Modal: `onSwitchToPartner()`.
- Partner mode displays clear dedicated header with `[← Kembali ke Akun Warga]`.
- Header never renders role-switch pills on top of the screen.

### Core Circular State Contract
- `walletBalance`: `number` (Rupiah).
- `transactions`: Array of `{ id, type: 'credit' | 'debit', title, subtitle, amount, date, status, category, referenceId }`.
- `depositCategories`: Array of `{ id, name, pricePerKg, unit, icon, color, description }`.
- `depositTicket`: `{ id, code: 'PLH-XXXXXX', type: 'dropoff' | 'pickup', items: [{ categoryId, weight, subtotal }], totalEstimated, status: 'submitted' | 'verified', createdAt }`.
- `products`: Array of `{ id, name, category, price, wastePrice, stock, partnerName, image, rating }`.
- `handleCreateDepositTicket(ticketData)`: Creates active ticket, status `'submitted'`.
- `handleSimulatePartnerWeighing(ticketId, finalWeights)`: Credits `walletBalance`, marks ticket `'verified'`, appends credit transaction to ledger.
- `handleBuyProduct(productId, qty)`: Deducts `wastePrice * qty` from `walletBalance`, decrements stock, appends debit transaction.
- `handleCashout(ewalletType, phone, amount)`: Validates `amount <= walletBalance && amount >= 10000`, deducts `amount`, appends debit transaction.

### Mobile Layout & Viewport Contract
- Outer wrapper: `bg-slate-100 min-h-dvh flex justify-center selection:bg-emerald-500 selection:text-white`.
- Screen container: `w-full max-w-md mx-auto min-h-dvh bg-slate-50 relative flex flex-col shadow-xl overflow-x-hidden`.
- Bottom navigation: `fixed bottom-0 inset-x-0 z-40 max-w-md mx-auto bg-white/95 backdrop-blur-md border-t border-slate-200/80 px-4 py-2 grid grid-cols-4 gap-1`.
- Navigation items: 4 tabs (`Beranda`, `Setor`, `Toko`, `Dompet`), each with minimum 44px touch target, static label (0 CLS).
- Content padding bottom: `pb-24` to prevent content occlusion by the fixed bottom navbar.

## Code Layout
- `src/App.jsx`: Main React component.
- `src/index.css`: Global styles & Tailwind v4 `@theme`.
- `src/lib/utils.js`: Utility helpers.
- `e2e_tests/`: Test suite runner and automated tests.
