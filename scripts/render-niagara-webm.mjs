#!/usr/bin/env node
/**
 * Render Curio Bureau's deterministic HTML canvas film with a real Chromium browser.
 * This renders the checked-in baseline, NOT the finished Vox-style rebuild.
 *
 * Run: npm ci && npx playwright install chromium && node scripts/render-html.mjs
 */
import { chromium } from 'playwright';
import { mkdir, access } from 'node:fs/promises';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

const input = resolve(process.env.CURIO_HTML || 'dist/niagara-1969/Curio_Bureau_Niagara_1969_Editorial.html');
const output = resolve(process.env.CURIO_OUTPUT || 'dist/niagara-1969/Curio_Bureau_Niagara_1969_Editorial.webm');
await access(input);
await mkdir(resolve(output, '..'), { recursive: true });
const browser = await chromium.launch({ headless: true, args: ['--autoplay-policy=no-user-gesture-required'] });
try {
  const context = await browser.newContext({
    acceptDownloads: true,
    viewport: { width: 560, height: 1000 },
    deviceScaleFactor: 1
  });
  const page = await context.newPage();
  page.on('pageerror', e => console.error('BROWSER ERROR:', e.message));
  page.on('console', m => { if (m.type() === 'error') console.error('CONSOLE ERROR:', m.text()); });
  await page.goto(pathToFileURL(input).href, { waitUntil: 'load', timeout: 60000 });
  await page.waitForFunction(() => typeof window.exportCurioWebM === 'function');
  // The editorial film must NEVER export with fallback typography.
  const fonts = await page.evaluate(async () => {
    if(!window.CURIO_QA) return {legacy:true};
    await Promise.all([
      document.fonts.load('600 100px "Playfair Display"'),
      document.fonts.load('800 42px "Manrope"')
    ]);
    await document.fonts.ready;
    return {loaded:[...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family),geodata:window.CURIO_QA.mapLoaded,captions:window.CURIO_QA.captionCount};
  });
  if(!fonts.legacy && (!fonts.loaded.some(n=>n.includes('Playfair Display'))||!fonts.loaded.some(n=>n.includes('Manrope'))||!fonts.geodata||fonts.captions<35)) {
    throw new Error('Editorial render blocked: fonts, geography or captions missing: '+JSON.stringify(fonts));
  }
  console.log('Editorial prerequisite check:',JSON.stringify(fonts));
  const voicePath = process.env.CURIO_VOICE || '';
  if (voicePath) {
    await access(resolve(voicePath));
    await page.locator('#voiceFile').setInputFiles(resolve(voicePath));
    await page.waitForFunction(() => Boolean(window.player?.voice || window.player?.audioBuffers?.voice), null, { timeout: 60000 });
    console.log('Narration decoded and attached to film timeline.');
    console.log('User-supplied narration has been selected:', voicePath);
  } else {
    console.warn('NO NARRATION PROVIDED: this output is ONLY a preview, never a final video.');
  }
  const downloadPromise = page.waitForEvent('download', { timeout: 240000 });
  await page.locator('#export').click();
  const download = await downloadPromise;
  await download.saveAs(output);
  console.log('Render saved:', output);
  await context.close();
} finally {
  await browser.close();
}
