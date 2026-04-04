import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove entire Packages Section (from comment to closing tag)
pattern = r'\n    <!-- Packages Section -->.*?    </section>\n'
content = re.sub(pattern, '\n', content, count=1, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("OK - Removed Packages section from homepage")
