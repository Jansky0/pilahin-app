import puppeteer from 'puppeteer-core';

export const DEFAULT_APP_URL = process.env.APP_URL || 'http://localhost:3000';
export const CHROME_PATH = process.env.CHROME_BIN || '/home/jansky/.local/bin/google-chrome';

/**
 * Launch Chromium browser instance via puppeteer-core
 */
export async function launchBrowser(options = {}) {
  const headless = process.env.HEADLESS !== 'false';
  return await puppeteer.launch({
    executablePath: CHROME_PATH,
    headless: headless ? 'new' : false,
    args: [
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--disable-dev-shm-usage',
      '--disable-gpu',
      '--window-size=400,900'
    ],
    ...options
  });
}

/**
 * Create a new page with mobile viewport
 */
export async function createPage(browser, viewport = { width: 390, height: 844 }) {
  const page = await browser.newPage();
  await page.setViewport(viewport);
  return page;
}

/**
 * Open application and wait for network idle
 */
export async function openApp(page, url = DEFAULT_APP_URL) {
  await page.goto(url, { waitUntil: 'networkidle0', timeout: 15000 });
  await delay(300);
}

/**
 * Delay helper
 */
export const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

/**
 * Parse Indonesian Rupiah string (e.g. "Rp 148.500" or "Rp148.500" or "+Rp 24.900") to integer
 */
export function parseRupiah(str) {
  if (!str) return 0;
  const cleaned = str.replace(/[^\d]/g, '');
  return parseInt(cleaned, 10) || 0;
}

/**
 * Extract active wallet balance from DOM
 */
export async function getWalletBalance(page) {
  return await page.evaluate(() => {
    // Check big balance card in Dompet
    const bigBalance = document.querySelector('.text-3xl.font-extrabold');
    if (bigBalance && bigBalance.innerText.includes('Rp')) {
      const match = bigBalance.innerText.replace(/[^\d]/g, '');
      return parseInt(match, 10) || 0;
    }

    // Check Hero Card on Home
    const heroBalance = Array.from(document.querySelectorAll('div, span, h2, h3, p'))
      .find(el => el.innerText && el.innerText.match(/Rp\s*[\d.]+/));
    if (heroBalance) {
      const match = heroBalance.innerText.match(/Rp\s*([\d.]+)/);
      if (match) {
        return parseInt(match[1].replace(/\./g, ''), 10) || 0;
      }
    }
    return 0;
  });
}

/**
 * Switch active navigation tab
 * Supports: 'home' | 'setor' | 'toko' | 'snapsort' | 'dompet'
 * or friendly labels: 'Beranda' | 'Setor' | 'Toko' | 'Dompet'
 */
export async function switchTab(page, tabIdOrName) {
  const normalized = tabIdOrName.toLowerCase();

  await page.evaluate((target) => {
    // 1. Try clicking action tiles on Home if visible
    if (target.includes('setor')) {
      const tile = Array.from(document.querySelectorAll('div, span, button'))
        .find(el => el.textContent.trim() === 'Setor Sampah');
      if (tile) { tile.click(); return; }
    }
    if (target.includes('toko')) {
      const tile = Array.from(document.querySelectorAll('div, span, button'))
        .find(el => el.textContent.trim() === 'Toko Sirkular');
      if (tile) { tile.click(); return; }
    }
    if (target.includes('dompet')) {
      const tile = Array.from(document.querySelectorAll('div, span, button'))
        .find(el => el.textContent.trim() === 'Dompet');
      if (tile) { tile.click(); return; }
    }

    // 2. Try bottom navbar buttons
    const navButtons = Array.from(document.querySelectorAll('nav button, header button, footer button, [role="tab"]'));
    for (const btn of navButtons) {
      const text = btn.innerText.toLowerCase();
      if (
        (target.includes('home') || target.includes('beranda')) && text.includes('beranda') ||
        target.includes('setor') && text.includes('setor') ||
        target.includes('toko') && text.includes('toko') ||
        target.includes('dompet') && text.includes('dompet') ||
        target.includes('snapsort') && text.includes('snap')
      ) {
        btn.click();
        return;
      }
    }

    // 3. Fallback: bottom nav icons click by position if unlabelled
    const allNavBtns = Array.from(document.querySelectorAll('nav button'));
    if (allNavBtns.length >= 4) {
      if (target.includes('home') || target.includes('beranda')) allNavBtns[0].click();
      else if (target.includes('setor')) allNavBtns[1].click();
      else if (target.includes('toko')) allNavBtns[2].click();
      else if (target.includes('dompet')) allNavBtns[allNavBtns.length - 1].click();
    }
  }, normalized);

  await delay(400);
}

/**
 * Click element matching text
 */
export async function clickByText(page, textOrRegex, selector = 'button, div, span, a') {
  return await page.evaluate((pattern, sel) => {
    const isRegex = pattern.startsWith('/') && pattern.endsWith('/');
    const reg = isRegex ? new RegExp(pattern.slice(1, -1), 'i') : null;

    const elements = Array.from(document.querySelectorAll(sel));
    const target = elements.find(el => {
      const t = el.innerText ? el.innerText.trim() : '';
      if (reg) return reg.test(t);
      return t.toLowerCase().includes(pattern.toLowerCase());
    });

    if (target) {
      target.click();
      return true;
    }
    return false;
  }, typeof textOrRegex === 'string' ? textOrRegex : textOrRegex.toString(), selector);
}

/**
 * Extract currently visible toast notification text
 */
export async function getToastText(page) {
  return await page.evaluate(() => {
    const toasts = Array.from(document.querySelectorAll('.animate-bounce, [role="alert"], .fixed.top-4'));
    if (toasts.length > 0) {
      return toasts[0].innerText.trim();
    }
    return null;
  });
}

/**
 * Get transactions list from Dompet tab
 */
export async function getTransactions(page) {
  return await page.evaluate(() => {
    const rows = Array.from(document.querySelectorAll('.space-y-2\\.5 > div, [data-testid="transaction-item"]'));
    return rows.map(r => {
      const text = r.innerText.trim();
      const isCredit = text.includes('+');
      return {
        text,
        isCredit
      };
    });
  });
}

/**
 * Set input value cleanly triggering React synthetic onChange
 */
export async function setInputValue(page, selector, value) {
  return await page.evaluate((sel, val) => {
    let input = null;
    if (typeof sel === 'string') {
      input = document.querySelector(sel);
    }
    if (!input) {
      const inputs = Array.from(document.querySelectorAll('input'));
      input = inputs.find(i => (i.value && i.value.includes('08')) || i.type === 'text' || i.type === 'number');
    }
    if (input) {
      const nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
      nativeSetter.call(input, val);
      input.dispatchEvent(new Event('input', { bubbles: true }));
      input.dispatchEvent(new Event('change', { bubbles: true }));
      return true;
    }
    return false;
  }, selector, value);
}

/**
 * Custom assertions
 */
export function assert(condition, message) {
  if (!condition) {
    throw new Error(`Assertion Failed: ${message}`);
  }
}

export function assertEqual(actual, expected, message) {
  if (actual !== expected) {
    throw new Error(`Assertion Failed: ${message || 'Values do not match'} (Expected: ${expected}, Actual: ${actual})`);
  }
}
