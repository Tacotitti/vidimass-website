"""Add CTA and common button translations to all languages"""

new_keys = {
    'en': {
        'cta_get_started': 'Get Started',
        'cta_contact': 'Contact',
        'footer_terms': 'Terms of Service',
        'footer_copyright': '© 2026 MediaMass. All rights reserved.'
    },
    'de': {
        'cta_get_started': 'Jetzt starten',
        'cta_contact': 'Kontakt',
        'footer_terms': 'Nutzungsbedingungen',
        'footer_copyright': '© 2026 MediaMass. Alle Rechte vorbehalten.'
    },
    'tr': {
        'cta_get_started': 'Başlayın',
        'cta_contact': 'İletişim',
        'footer_terms': 'Kullanım Şartları',
        'footer_copyright': '© 2026 MediaMass. Tüm hakları saklıdır.'
    },
    'pt': {
        'cta_get_started': 'Começar',
        'cta_contact': 'Contato',
        'footer_terms': 'Termos de Serviço',
        'footer_copyright': '© 2026 MediaMass. Todos os direitos reservados.'
    },
    'es': {
        'cta_get_started': 'Empezar',
        'cta_contact': 'Contacto',
        'footer_terms': 'Términos de Servicio',
        'footer_copyright': '© 2026 MediaMass. Todos los derechos reservados.'
    },
    'ru': {
        'cta_get_started': 'Начать',
        'cta_contact': 'Контакт',
        'footer_terms': 'Условия использования',
        'footer_copyright': '© 2026 MediaMass. Все права защищены.'
    },
    'zh': {
        'cta_get_started': '开始使用',
        'cta_contact': '联系我们',
        'footer_terms': '服务条款',
        'footer_copyright': '© 2026 MediaMass. 保留所有权利。'
    },
    'ar': {
        'cta_get_started': 'ابدأ',
        'cta_contact': 'اتصل بنا',
        'footer_terms': 'شروط الخدمة',
        'footer_copyright': '© 2026 MediaMass. جميع الحقوق محفوظة.'
    }
}

with open('translations.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Add after footer_contact
for lang, keys in new_keys.items():
    insertion = ''
    for key, value in keys.items():
        if key == 'footer_contact':
            continue  # Already exists
        value_escaped = value.replace('"', '\\"')
        insertion += f'\n        {key}: "{value_escaped}",'
    
    # Find footer_contact and insert after
    pattern = r'footer_contact: "[^"]*",'
    import re
    matches = list(re.finditer(pattern, content))
    
    lang_order = ['en', 'de', 'tr', 'pt', 'es', 'ru', 'zh', 'ar']
    lang_index = lang_order.index(lang)
    
    if lang_index < len(matches):
        match = matches[lang_index]
        content = content[:match.end()] + insertion + content[match.end():]
        print(f"✓ Added CTA/footer keys to {lang}")

with open('translations.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✅ Added CTA and footer translations to all 8 languages!")
