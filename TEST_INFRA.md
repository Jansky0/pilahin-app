# TEST_INFRA.md — Pilah.in Opaque-Box Test Infrastructure

## 1. Overview & Testing Philosophy
This document specifies the opaque-box End-to-End (E2E) automated testing infrastructure for the **Pilah.in** application overhaul. 

In accordance with the **Dual Track Project Pattern** and the authoritative requirements in `ORIGINAL_REQUEST.md` and `PROJECT.md`, the test harness operates strictly from an **opaque-box perspective**:
- **Zero internal mocking**: Tests interact exclusively with the live rendered DOM, evaluating real user inputs (clicks, text entries, keyboard events) and verifying visible UI outputs, state transformations, ledger records, and toast notifications.
- **Real runtime execution**: Tests execute against the live Vite application running at `http://localhost:3000` inside headless Chromium via `puppeteer-core`.
- **Authoritative Oracle**: Expected values for deposit pricing, wallet balance arithmetic, store discounts, and cashout thresholds are derived directly from `PROJECT.md` interface contracts and `ORIGINAL_REQUEST.md`.

---

## 2. Directory Layout & Test Suite Structure

```
/home/jansky/pilahin-app/
├── e2e_tests/
│   ├── helpers.js                  # Shared headless browser launcher, DOM utilities, assertions
│   ├── tier1_features.test.js      # Tier 1: Feature coverage (Leaderboard removal, roles, deposit, toko, wallet)
│   ├── tier2_boundary.test.js      # Tier 2: Boundary, corner cases, zero/negative inputs, escrow limits
│   ├── tier3_cross_feature.test.js # Tier 3: Full closed-loop circular economy lifecycle
│   ├── tier4_real_world.test.js    # Tier 4: Real-world mobile ergonomics, partner ops, multi-category deposit
│   └── run_tests.js                # Unified CLI runner with tier filtering, summary reporting, exit codes
├── TEST_INFRA.md                   # Infrastructure & architecture specification (this file)
└── TEST_READY.md                   # Test readiness publication and baseline execution results
```

---

## 3. Test Tiers Specification

### Tier 1: Feature Coverage
Validates the presence, absence, and primary behavior of core features defined in `PROJECT.md`:
1. **Leaderboard Absence (`test_1_1_leaderboard_absent_on_citizen_home`)**:
   - Asserts that the citizen home screen (`activeTab === 'home'`) does NOT render `Peringkat Kebersihan RW Cilandak`, ranking badges (`🥇 RW 05`), or RT/RW leaderboard cards.
2. **Clean Role Separation (`test_1_2_clean_role_navigation`)**:
   - Asserts that the header does NOT display role-switching pills (`Mode Warga` / `Mode Mitra RW`).
   - Asserts that citizen mode is uncluttered and partner mode is accessed cleanly with a dedicated back button (`← Kembali ke Warga`).
3. **Deposit Estimation Calculation (`test_1_3_deposit_calculation`)**:
   - Verifies category selection and weight stepper math (e.g. Kardus @ Rp 1.800/kg, Plastik @ Rp 3.500/kg).
4. **Deposit Weighing & Balance Update (`test_1_4_balance_update_after_weighing`)**:
   - Creates digital ticket `PLH-XXXXXX`, simulates partner weighing, and asserts that `walletBalance` increments by the exact ticket amount with a credit ledger entry.
5. **Toko Sirkular Purchase Deduction (`test_1_5_store_purchase_deduction`)**:
   - Purchases an upcycled product (e.g. Pupuk Kompos @ Rp 18.000), asserting immediate deduction from `walletBalance`, decrement of product stock, and debit ledger entry.
6. **E-Wallet Cashout Validation (`test_1_6_ewallet_cashout_success`)**:
   - Selects cashout channel (GoPay/DANA), enters nominal >= Rp 10.000, and verifies balance deduction and transaction logging.

### Tier 2: Boundary & Corner Cases
Tests system resilience against invalid inputs, extreme boundaries, and escrow limits:
1. **Zero Amount Deposit Rejection (`test_2_1_zero_deposit_prevention`)**:
   - Attempting to generate a deposit ticket with 0 kg or no categories selected is blocked with an alert/toast.
2. **Below Minimum Cashout (`test_2_2_below_minimum_cashout`)**:
   - Entering an amount < Rp 10.000 (e.g. Rp 5.000 or Rp 0) triggers validation rejection without balance deduction.
3. **Store Purchase Overdraft (`test_2_3_store_purchase_insufficient_balance`)**:
   - Attempting to purchase a product whose price exceeds current `walletBalance` triggers an insufficient balance warning.
4. **Cashout Overdraft (`test_2_4_cashout_exceeding_balance`)**:
   - Attempting to withdraw more than the active escrow balance is rejected.
5. **Phone Format Validation (`test_2_5_invalid_phone_cashout`)**:
   - Submitting malformed or non-numeric phone numbers is rejected.
6. **Negative Weight Stepper Prevention (`test_2_6_negative_stepper_weight`)**:
   - Steppers cannot decrement weights below 1 kg or negative numbers.

### Tier 3: Cross-Feature Combinations (Full Circular Loop)
Validates the complete closed-loop circular economy workflow end-to-end:
```
[Initial Balance B0] 
       │
       ▼
[1. Setor Sampah: Kardus 5kg (+Rp 9.000)]
       │
       ▼
[2. Verifikasi Timbang Mitra ──► Saldo Naik: B1 = B0 + 9.000]
       │
       ▼
[3. Toko Sirkular: Beli Pupuk (-Rp 18.000) ──► Saldo Turun: B2 = B1 - 18.000]
       │
       ▼
[4. Tarik Saldo ke GoPay (-Rp 50.000) ──► Saldo Turun: B3 = B2 - 50.000]
       │
       ▼
[5. Mutasi Kas Terverifikasi: 3 Entri (1 Kredit, 2 Debit)]
```

### Tier 4: Real-World Scenarios
1. **Citizen Daily Mobile Flow (`test_4_1_citizen_daily_flow`)**:
   - Standard 390x844 viewport navigation, verifying persistent bottom navigation bar, zero horizontal overflow, and responsive dialogs.
2. **Partner Portal Operations (`test_4_2_partner_weighing_portal`)**:
   - Partner operator enters ticket code, inputs scale weight, and confirms credit dispatch.
3. **Multi-Category Deposit Flow (`test_4_3_multi_category_deposit`)**:
   - Complex deposit ticket combining multiple waste streams (Kardus + Botol PET + Minyak Jelantah) with accurate subtotal aggregation.

---

## 4. Execution & CLI Options

The test suite can be run via the standard Node.js test runner:

```bash
# Run all tiers (Tiers 1-4)
node e2e_tests/run_tests.js

# Run a specific tier
node e2e_tests/run_tests.js --tier=1
node e2e_tests/run_tests.js --tier=2
node e2e_tests/run_tests.js --tier=3
node e2e_tests/run_tests.js --tier=4

# Run with custom application URL (defaults to http://localhost:3000)
APP_URL=http://localhost:3000 node e2e_tests/run_tests.js

# Run in headed mode (for visual debugging)
HEADLESS=false node e2e_tests/run_tests.js
```

### Exit Code Convention:
- `0`: All executed test cases passed successfully.
- `1`: One or more test cases failed (with detailed failure reason, expected vs actual values, and step context).

---

## 5. Technical Requirements & Dependencies
- **Node.js**: v20+ (tested on Node v26.1.0)
- **Browser**: Chromium (located at `/home/jansky/.local/bin/google-chrome`)
- **Driver**: `puppeteer-core` (zero-bundle browser automation)
- **Target Server**: Vite dev server (`http://localhost:3000`)
