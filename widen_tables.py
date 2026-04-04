import re

# Read preisliste.html
with open('preisliste.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace table min-width
content = content.replace(
    '<table class="w-full">',
    '<table class="w-full min-w-[650px]">'
)

# Write back
with open('preisliste.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("OK - Tables widened")
