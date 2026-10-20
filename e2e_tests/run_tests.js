import * as tier1 from './tier1_features.test.js';
import * as tier2 from './tier2_boundary.test.js';
import * as tier3 from './tier3_cross_feature.test.js';
import * as tier4 from './tier4_real_world.test.js';
import { DEFAULT_APP_URL } from './helpers.js';

// Parse command line arguments
const args = process.argv.slice(2);
const tierArg = args.find(a => a.startsWith('--tier='));
const filterArg = args.find(a => a.startsWith('--filter='));
const allowPending = args.includes('--allow-pending') || args.includes('--report-only');

const selectedTier = tierArg ? parseInt(tierArg.split('=')[1], 10) : null;
const filterPattern = filterArg ? filterArg.split('=')[1].toLowerCase() : null;

const allSuites = [
  { tier: 1, module: tier1 },
  { tier: 2, module: tier2 },
  { tier: 3, module: tier3 },
  { tier: 4, module: tier4 },
];

async function checkServer(url) {
  try {
    const res = await fetch(url, { method: 'HEAD' });
    return res.ok || res.status === 200 || res.status === 304;
  } catch (err) {
    return false;
  }
}

async function main() {
  const targetUrl = process.env.APP_URL || DEFAULT_APP_URL;

  console.log('===============================================================');
  console.log('          PILAH.IN — OPAQUE-BOX E2E TEST SUITE RUNNER           ');
  console.log('===============================================================');
  console.log(`Target URL : ${targetUrl}`);
  console.log(`Timestamp  : ${new Date().toISOString()}`);
  if (selectedTier) console.log(`Filter Tier: Tier ${selectedTier}`);
  if (filterPattern) console.log(`Filter Text: "${filterPattern}"`);
  console.log('---------------------------------------------------------------\n');

  // Verify server reachability
  const isServerUp = await checkServer(targetUrl);
  if (!isServerUp) {
    console.error(`❌ ERROR: Could not connect to target server at ${targetUrl}!`);
    console.error('Please ensure Vite is running (`npm run dev` or `npm run preview`).\n');
    process.exit(1);
  }

  const suitesToRun = allSuites.filter(s => !selectedTier || s.tier === selectedTier);

  let grandTotal = 0;
  let grandPassed = 0;
  let grandFailed = 0;
  const allResults = [];

  for (const suite of suitesToRun) {
    console.log(`\n▶ Running [${suite.module.name}]`);
    console.log('─'.repeat(63));

    const startTime = Date.now();
    let suiteResults = [];

    try {
      suiteResults = await suite.module.run();
    } catch (err) {
      console.error(`💥 Suite execution crashed: ${err.message}`);
      suiteResults.push({
        name: `${suite.module.name} (Suite Lifecycle)`,
        status: 'FAIL',
        error: err.message
      });
    }

    const duration = ((Date.now() - startTime) / 1000).toFixed(2);

    for (const res of suiteResults) {
      if (filterPattern && !res.name.toLowerCase().includes(filterPattern)) {
        continue;
      }

      grandTotal++;
      if (res.status === 'PASS') {
        grandPassed++;
        console.log(`  ✅ [PASS] ${res.name}${res.details ? ` (${res.details})` : ''}`);
      } else {
        grandFailed++;
        console.log(`  ❌ [FAIL] ${res.name}`);
        if (res.error) {
          console.log(`     └─ Reason: ${res.error}`);
        }
      }
      allResults.push({ tier: suite.tier, ...res });
    }

    console.log(`  ↳ Completed in ${duration}s`);
  }

  // Summary Report
  console.log('\n===============================================================');
  console.log('                      TEST EXECUTION SUMMARY                   ');
  console.log('===============================================================');
  console.log(`Total Test Cases Executed : ${grandTotal}`);
  console.log(`Passed                    : ${grandPassed} (${grandTotal > 0 ? ((grandPassed / grandTotal) * 100).toFixed(1) : 0}%)`);
  console.log(`Failed                    : ${grandFailed}`);
  console.log('===============================================================');

  if (grandFailed > 0) {
    console.log('\n⚠️  FAILED TEST CASES (DEFECT / PENDING MILESTONE ESCALATIONS):');
    allResults
      .filter(r => r.status === 'FAIL')
      .forEach(r => {
        console.log(` • [Tier ${r.tier}] ${r.name}`);
        console.log(`   Error: ${r.error}`);
      });
    console.log('\n');

    if (allowPending) {
      console.log('ℹ️  Flag --allow-pending was passed: Exiting with 0 for intermediate milestone gating.');
      process.exit(0);
    } else {
      process.exit(1);
    }
  } else {
    console.log('\n🎉 ALL TESTS PASSED SUCCESSFULLY! Clean exit code 0.\n');
    process.exit(0);
  }
}

main().catch(err => {
  console.error('Fatal Test Runner Exception:', err);
  process.exit(1);
});
