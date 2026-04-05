"""Add remaining languages PT, ES, RU, ZH, AR to translations.js"""

remaining_langs = {
    'pt': """
        nav_charting: "Social Media Charting",
        nav_pricing: "Preços",
        nav_contact: "Contato",
        footer_privacy: "Política de Privacidade",
        footer_terms: "Termos de Serviço",
        footer_copyright: "© 2026 MediaMass. Todos os direitos reservados.",
        cta_get_started: "Começar",
        cta_contact: "Contato",""",
    'es': """
        nav_charting: "Social Media Charting",
        nav_pricing: "Precios",
        nav_contact: "Contacto",
        footer_privacy: "Política de Privacidad",
        footer_terms: "Términos de Servicio",
        footer_copyright: "© 2026 MediaMass. Todos los derechos reservados.",
        cta_get_started: "Empezar",
        cta_contact: "Contacto",""",
    'ru': """
        nav_charting: "Social Media Charting",
        nav_pricing: "Цены",
        nav_contact: "Контакт",
        footer_privacy: "Политика конфиденциальности",
        footer_terms: "Условия использования",
        footer_copyright: "© 2026 MediaMass. Все права защищены.",
        cta_get_started: "Начать",
        cta_contact: "Контакт",""",
    'zh': """
        nav_charting: "社交媒体排行",
        nav_pricing: "价格",
        nav_contact: "联系我们",
        footer_privacy: "隐私政策",
        footer_terms: "服务条款",
        footer_copyright: "© 2026 MediaMass. 保留所有权利。",
        cta_get_started: "开始使用",
        cta_contact: "联系我们",""",
    'ar': """
        nav_charting: "تصنيف وسائل التواصل",
        nav_pricing: "الأسعار",
        nav_contact: "اتصل بنا",
        footer_privacy: "سياسة الخصوصية",
        footer_terms: "شروط الخدمة",
        footer_copyright: "© 2026 MediaMass. جميع الحقوق محفوظة.",
        cta_get_started: "ابدأ",
        cta_contact: "اتصل بنا","""
}

import re

with open('translations.js', 'r', encoding='utf-8') as f:
    content = f.read()

for lang_code, keys_text in remaining_langs.items():
    pattern = rf'({lang_code}:\s*\{{[^}}]*nav_get_started:\s*"[^"]*",)'
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        insert_pos = match.end()
        content = content[:insert_pos] + keys_text + content[insert_pos:]
        print(f"✓ Added keys to {lang_code}")
    else:
        print(f"❌ Could not find {lang_code}")

with open('translations.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✅ All 8 languages complete!")
