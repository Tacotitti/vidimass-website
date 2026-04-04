import re

with open('preisliste.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Reduce table min-width from 500px to 360px (fits most phones)
content = content.replace(
    '<table class="w-full min-w-[500px]">',
    '<table class="w-full min-w-[360px]">'
)

# 2. Reduce padding on mobile - make cells more compact
content = re.sub(
    r'<th class="text-left py-3 md:py-4 px-4 md:px-6',
    r'<th class="text-left py-2 md:py-4 px-2 md:px-6',
    content
)
content = re.sub(
    r'<th class="text-right py-3 md:py-4 px-4 md:px-6',
    r'<th class="text-right py-2 md:py-4 px-2 md:px-6',
    content
)

# 3. Reduce padding in table body cells
content = re.sub(
    r'<td class="py-4 md:py-5 px-4 md:px-6',
    r'<td class="py-3 md:py-5 px-2 md:px-6',
    content
)

# 4. Make "Pro Video" column even smaller on mobile
content = re.sub(
    r'<th class="text-right py-2 md:py-4 px-2 md:px-6 text-sm md:text-base text-gray-400 font-semibold">Pro Video</th>',
    r'<th class="text-right py-2 md:py-4 px-2 md:px-6 text-xs md:text-base text-gray-400 font-semibold hidden sm:table-cell">Pro Video</th>',
    content
)

# 5. Hide "Pro Video" column on extra small screens
content = re.sub(
    r'(<td class="py-3 md:py-5 px-2 md:px-6 text-right text-gray-400 text-sm md:text-base">\$0\.\d+</td>)',
    r'<td class="py-3 md:py-5 px-2 md:px-6 text-right text-gray-400 text-xs md:text-base hidden sm:table-cell">\g<1></td>'.replace(r'\g<1>', ''),
    content
)

# Better approach - just add hidden class to existing pro-video cells
content = content.replace(
    '<td class="py-3 md:py-5 px-2 md:px-6 text-right text-gray-400 text-sm md:text-base">$',
    '<td class="py-3 md:py-5 px-2 md:px-6 text-right text-gray-400 text-xs md:text-base hidden sm:table-cell">$'
)
content = content.replace(
    '<td class="py-3 md:py-5 px-2 md:px-6 text-right text-gray-400 text-sm md:text-base">€',
    '<td class="py-3 md:py-5 px-2 md:px-6 text-right text-gray-400 text-xs md:text-base hidden sm:table-cell">€'
)

with open('preisliste.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("OK - Made tables more compact for mobile")
