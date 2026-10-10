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

const input = resolve(process.env.CURIO_HTML || 'films/samoa-2011/legacy/Curio_Bureau_The_Day_That_Disappeared_REBUILT.html');
const output = resolve(process.env.CURIO_OUTPUT || 'dist/samoa-2011/preview-no-narration.webm');
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
  const voicePath = process.env.CURIO_VOICE || '';
  if (voicePath) {
    await access(resolve(voicePath));
    await page.locator('#voiceFile').setInputFiles(resolve(voicePath));
    await page.waitForFunction(() => Boolean(window.player?.audioBuffers?.voice) || /loaded|ready/i.test(document.querySelector('#voiceStatus')?.textContent || ''), { timeout: 30000 }).catch(() => {});
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
