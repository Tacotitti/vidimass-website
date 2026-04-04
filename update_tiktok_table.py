import re

with open('preisliste.html', 'r', encoding='utf-8') as f:
    content = f.read()

# TikTok pricing data with calculations
tiktok_prices = [
    ("1,000 Videos", "$79", 79/1000),
    ("5,000 Videos", "$199", 199/5000),
    ("15,000 Videos", "$399", 399/15000),
    ("30,000 Videos", "$749", 749/30000, "BELIEBT", "pink"),
    ("60,000 Videos", "$1,299", 1299/60000),
    ("125,000 Videos", "$2,199", 2199/125000),
    ("250,000 Videos", "$3,999", 3999/250000, "BEST VALUE", "violet"),
    ("500,000 Videos", "$6,999", 6999/500000),
    ("1,000,000 Videos", "$11,999", 11999/1000000),
]

# Build TikTok table body
tiktok_rows = []
for item in tiktok_prices:
    if len(item) == 3:
        # Normal row
        videos, price, per_video = item
        tiktok_rows.append(f'''                                <tr class="border-b border-white/5 hover:bg-white/5 transition-colors">
                                    <td class="py-3 md:py-5 px-2 md:px-6 font-semibold text-white text-sm md:text-base">{videos}</td>
                                    <td class="py-3 md:py-5 px-2 md:px-6 text-right text-xl md:text-2xl font-bold text-violet-400">{price}</td>
                                    <td class="py-3 md:py-5 px-2 md:px-6 text-right text-gray-400 text-sm md:text-base">~${per_video:.3f}</td>
                                </tr>''')
    else:
        # Special row with badge
        videos, price, per_video, badge, color = item
        bg_class = f"bg-{color}-500/10"
        badge_color = f"{color}-400" if color == "pink" else f"{color}-400"
        badge_bg = f"{color}-500/20" if color == "pink" else f"{color}-500/20"
        price_color = f"{color}-400" if color == "pink" else "pink-400"
        
        tiktok_rows.append(f'''                                <tr class="border-b border-white/5 hover:bg-white/5 transition-colors {bg_class}">
                                    <td class="py-3 md:py-5 px-2 md:px-6 font-semibold text-white text-sm md:text-base flex items-center gap-2">
                                        {videos}
                                        <span class="text-xs bg-{badge_bg} text-{badge_color} px-2 py-1 rounded-full">{badge}</span>
                                    </td>
                                    <td class="py-3 md:py-5 px-2 md:px-6 text-right text-xl md:text-2xl font-bold text-{price_color}">{price}</td>
                                    <td class="py-3 md:py-5 px-2 md:px-6 text-right text-gray-400 text-sm md:text-base">~${per_video:.3f}</td>
                                </tr>''')

tiktok_tbody = '\n'.join(tiktok_rows)

# New TikTok table matching Instagram format
new_tiktok_table = f'''                    <div class="overflow-x-auto -mx-6 md:mx-0">
                        <table class="w-full min-w-[360px]">
                            <thead>
                                <tr class="border-b border-white/10">
                                    <th class="text-left py-2 md:py-4 px-2 md:px-6 text-sm md:text-base text-gray-400 font-semibold">Videos</th>
                                    <th class="text-right py-2 md:py-4 px-2 md:px-6 text-sm md:text-base text-gray-400 font-semibold">Preis</th>
                                    <th class="text-right py-2 md:py-4 px-2 md:px-6 text-sm md:text-base text-gray-400 font-semibold">Pro Video</th>
                                </tr>
                            </thead>
                            <tbody>
{tiktok_tbody}
                            </tbody>
                        </table>
                    </div>'''

# Replace TikTok table (find pattern from <div class="overflow-x-auto"> to </table>\n                    </div>)
pattern = r'(<div class="glass-card p-6 md:p-12 rounded-2xl">.*?<p class="text-gray-400 text-base md:text-lg">Mass Video Posting für TikTok</p>\s*</div>\s*)(<div class="overflow-x-auto".*?</table>\s*</div>)'

def replace_tiktok(match):
    return match.group(1) + new_tiktok_table

content = re.sub(pattern, replace_tiktok, content, count=1, flags=re.DOTALL)

with open('preisliste.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("OK - Updated TikTok table with Instagram format and per-video pricing")
