/* MediaMass – on-demand page translation (Google Translate Website Element).
   Loads Google's script only after the visitor clicks the button (keeps pages fast). */
(function () {
  if (window.__mmTranslate) return; window.__mmTranslate = true;
  var LANGS = 'en,de,es,pt,fr,it,nl,pl,sv,ro,cs,el,uk,ru,tr,ar,id,vi,tl,hu,da,fi,no,sk,bg,hr,sr,kk,ja,ko,zh-CN,hi,sw,ms,th';
  var rtl = document.documentElement.dir === 'rtl';
  var css = '#mm-tr{position:fixed;bottom:18px;' + (rtl ? 'right' : 'left') + ':18px;z-index:2147483000;font-family:Inter,system-ui,sans-serif}' +
    '#mm-tr-btn{display:flex;align-items:center;gap:6px;padding:10px 14px;border-radius:999px;border:1px solid rgba(255,255,255,.18);background:rgba(15,15,26,.92);color:#fff;font-size:14px;font-weight:600;cursor:pointer;box-shadow:0 8px 24px rgba(0,0,0,.35)}' +
    '#mm-tr-btn:hover{border-color:rgba(139,92,246,.7)}' +
    '#mm-tr-box{display:none;margin-bottom:8px;padding:10px;border-radius:14px;background:#fff;color:#111;box-shadow:0 8px 24px rgba(0,0,0,.35)}' +
    '#mm-tr.open #mm-tr-box{display:block}#mm-tr-box select{max-width:220px}' +
    'body{top:0!important}.skiptranslate iframe,.goog-te-banner-frame{display:none!important}';
  var st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);
  var wrap = document.createElement('div'); wrap.id = 'mm-tr'; wrap.className = 'notranslate'; wrap.setAttribute('translate', 'no');
  wrap.innerHTML = '<div id="mm-tr-box"><div id="google_translate_element">Loading…</div></div>' +
    '<button id="mm-tr-btn" type="button" aria-label="Translate this page">🌐 <span>Translate</span></button>';
  function mount() { document.body.appendChild(wrap); }
  if (document.body) mount(); else document.addEventListener('DOMContentLoaded', mount);
  var loaded = false;
  window.mmGoogleTranslateInit = function () {
    document.getElementById('google_translate_element').textContent = '';
    new google.translate.TranslateElement({ pageLanguage: (document.documentElement.lang || 'en').split('-')[0], includedLanguages: LANGS, autoDisplay: false }, 'google_translate_element');
  };
  wrap.addEventListener('click', function (ev) {
    if (!ev.target.closest('#mm-tr-btn')) return;
    wrap.classList.toggle('open');
    if (!loaded) { loaded = true; var s = document.createElement('script'); s.src = 'https://translate.google.com/translate_a/element.js?cb=mmGoogleTranslateInit'; s.async = true; document.head.appendChild(s); }
  });
})();
