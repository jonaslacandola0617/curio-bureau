// Owner-locked London Bridge R1 ending, adopted 13 October 2026.
// Keep the coordinates, fonts, colors, wording and opacity curve identical.
(function(root){
 const ENDING=Object.freeze({id:'london-bridge-v1',background:'#0D1C2B',foreground:'#F5F0E7',title:'Curio Bureau',tagline:'Stories, systems, and surprises.',titleX:540,titleY:840,titleSize:104,taglineX:540,taglineY:1190,taglineSize:29,fadeStartBeforeEnd:1.1,fadeEndBeforeEnd:.5});
 function drawEndcard(q,t,duration){if(t<=duration-ENDING.fadeStartBeforeEnd)return;let u=Math.max(0,Math.min(1,(t-(duration-1.1))/.6));q.save();q.globalAlpha=u*u*(3-2*u);q.fillStyle=ENDING.background;q.fillRect(0,0,1080,1920);q.fillStyle=ENDING.foreground;q.textAlign='center';q.font='900 104px "Playfair Display"';q.fillText(ENDING.title,540,840);q.font='700 29px "Manrope"';q.fillText(ENDING.tagline,540,1190);q.restore();}
 root.CurioBrand={ENDING,drawEndcard};
})(globalThis);
