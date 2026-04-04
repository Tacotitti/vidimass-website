import re

with open('preisliste.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Make headers responsive
content = content.replace(
    '<h2 class="text-4xl font-bold mb-3 flex items-center justify-center gap-3">',
    '<h2 class="text-2xl md:text-4xl font-bold mb-3 flex flex-wrap items-center justify-center gap-2 md:gap-3">'
)

# 2. Make emoji responsive
content = content.replace(
    '<span class="text-5xl">',
    '<span class="text-3xl md:text-5xl">'
)

# 3. Make paragraph responsive
content = content.replace(
    '<p class="text-gray-400 text-lg">',
    '<p class="text-gray-400 text-base md:text-lg">'
)

# 4. Make card padding responsive
content = content.replace(
    '<div class="glass-card p-8 md:p-12 rounded-2xl">',
    '<div class="glass-card p-6 md:p-12 rounded-2xl">'
)

# 5. Make margin responsive
content = content.replace(
    '<div class="text-center mb-10">',
    '<div class="text-center mb-8 md:mb-10">'
)

# 6. Make overflow container full width on mobile
content = content.replace(
    '<div class="overflow-x-auto">',
    '<div class="overflow-x-auto -mx-6 md:mx-0">'
)

# 7. Add min-width to tables
content = content.replace(
    '<table class="w-full">',
    '<table class="w-full min-w-[500px]">'
)

# 8. Make table cells responsive
content = re.sub(
    r'<th class="text-left py-4 px-6',
    r'<th class="text-left py-3 md:py-4 px-4 md:px-6 text-sm md:text-base',
    content
)
content = re.sub(
    r'<th class="text-right py-4 px-6',
    r'<th class="text-right py-3 md:py-4 px-4 md:px-6 text-sm md:text-base',
    content
)

# 9. Make table body cells responsive
content = re.sub(
    r'<td class="py-5 px-6 font-semibold text-white',
    r'<td class="py-4 md:py-5 px-4 md:px-6 font-semibold text-white text-sm md:text-base',
    content
)
content = re.sub(
    r'<td class="py-5 px-6 text-right text-2xl',
    r'<td class="py-4 md:py-5 px-4 md:px-6 text-right text-xl md:text-2xl',
    content
)
content = re.sub(
    r'<td class="py-5 px-6 text-right text-gray-400">',
    r'<td class="py-4 md:py-5 px-4 md:px-6 text-right text-gray-400 text-sm md:text-base">',
    content
)

# 10. Make buttons responsive
content = content.replace(
    'class="inline-block px-8 py-4 bg-gradient',
    'class="inline-block px-6 md:px-8 py-3 md:py-4 bg-gradient'
)
content = content.replace(
    'rounded-full font-bold text-lg hover',
    'rounded-full font-bold text-base md:text-lg hover'
)

with open('preisliste.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("OK - Made preisliste mobile responsive")
