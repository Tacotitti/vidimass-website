import re

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# New packages section
new_packages = '''    <!-- Packages Section -->
    <section id="packages" class="packages-section py-24 relative">
        <div class="container mx-auto px-6">
            <div class="text-center mb-16">
                <h2 class="text-4xl md:text-5xl font-bold mb-4">
                    Unsere <span class="bg-gradient-to-r from-violet-400 to-pink-400 bg-clip-text text-transparent"><span data-i18n="packages_title_2">Pakete</span></span>
                </h2>
                <p class="text-xl text-gray-400 max-w-2xl mx-auto">
                    Transparente Preise für TikTok und Instagram Distribution
                </p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-5xl mx-auto">
                <!-- TikTok Package -->
                <div class="package-card glass-card p-8 rounded-2xl hover:border-violet-500/50 transition-all">
                    <div class="flex items-center gap-3 mb-4">
                        <span class="text-4xl">🎵</span>
                        <div>
                            <div class="text-sm font-semibold text-violet-400">TIKTOK</div>
                            <div class="text-2xl font-bold">Video Distribution</div>
                        </div>
                    </div>
                    <p class="text-gray-400 mb-6">Mass Video Posting für TikTok</p>
                    
                    <div class="space-y-3 mb-8 bg-white/5 rounded-xl p-4">
                        <div class="flex justify-between items-center border-b border-white/5 pb-2">
                            <span class="text-gray-300">1K Videos</span>
                            <span class="font-bold text-violet-400">$79</span>
                        </div>
                        <div class="flex justify-between items-center border-b border-white/5 pb-2">
                            <span class="text-gray-300">5K Videos</span>
                            <span class="font-bold text-violet-400">$199</span>
                        </div>
                        <div class="flex justify-between items-center border-b border-white/5 pb-2">
                            <span class="text-gray-300">15K Videos</span>
                            <span class="font-bold text-violet-400">$399</span>
                        </div>
                        <div class="flex justify-between items-center bg-violet-500/10 -mx-4 px-4 py-2 border-b border-white/5">
                            <span class="text-white font-semibold flex items-center gap-2">
                                30K Videos
                                <span class="text-xs bg-pink-500/20 text-pink-400 px-2 py-0.5 rounded-full">BELIEBT</span>
                            </span>
                            <span class="font-bold text-pink-400">$749</span>
                        </div>
                        <div class="flex justify-between items-center border-b border-white/5 pb-2">
                            <span class="text-gray-300">60K Videos</span>
                            <span class="font-bold text-violet-400">$1,299</span>
                        </div>
                        <div class="flex justify-between items-center border-b border-white/5 pb-2">
                            <span class="text-gray-300">125K Videos</span>
                            <span class="font-bold text-violet-400">$2,199</span>
                        </div>
                        <div class="flex justify-between items-center bg-pink-500/10 -mx-4 px-4 py-2 border-b border-white/5">
                            <span class="text-white font-semibold flex items-center gap-2">
                                250K Videos
                                <span class="text-xs bg-violet-500/20 text-violet-400 px-2 py-0.5 rounded-full">BEST VALUE</span>
                            </span>
                            <span class="font-bold text-pink-400">$3,999</span>
                        </div>
                        <div class="flex justify-between items-center border-b border-white/5 pb-2">
                            <span class="text-gray-300">500K Videos</span>
                            <span class="font-bold text-violet-400">$6,999</span>
                        </div>
                        <div class="flex justify-between items-center">
                            <span class="text-gray-300">1M Videos</span>
                            <span class="font-bold text-violet-400">$11,999</span>
                        </div>
                    </div>

                    <a href="preisliste.html" class="block w-full py-3 bg-gradient-to-r from-violet-600 to-pink-600 hover:shadow-xl hover:shadow-violet-500/50 rounded-full font-semibold transition-all text-center">
                        Alle TikTok Pakete ansehen
                    </a>
                </div>

                <!-- Instagram Package -->
                <div class="package-card glass-card p-8 rounded-2xl hover:border-pink-500/50 transition-all">
                    <div class="flex items-center gap-3 mb-4">
                        <span class="text-4xl">📸</span>
                        <div>
                            <div class="text-sm font-semibold text-pink-400">INSTAGRAM</div>
                            <div class="text-2xl font-bold">Reels Distribution</div>
                        </div>
                    </div>
                    <p class="text-gray-400 mb-6">Unique Reels für Instagram Mass Posting</p>
                    
                    <div class="space-y-3 mb-8 bg-white/5 rounded-xl p-4">
                        <div class="flex justify-between items-center border-b border-white/5 pb-2">
                            <span class="text-gray-300">1K Reels</span>
                            <span class="font-bold text-pink-400">139€</span>
                        </div>
                        <div class="flex justify-between items-center border-b border-white/5 pb-2">
                            <span class="text-gray-300">5K Reels</span>
                            <span class="font-bold text-pink-400">399€</span>
                        </div>
                        <div class="flex justify-between items-center border-b border-white/5 pb-2">
                            <span class="text-gray-300">15K Reels</span>
                            <span class="font-bold text-pink-400">749€</span>
                        </div>
                        <div class="flex justify-between items-center bg-pink-500/10 -mx-4 px-4 py-2 border-b border-white/5">
                            <span class="text-white font-semibold flex items-center gap-2">
                                30K Reels
                                <span class="text-xs bg-orange-500/20 text-orange-400 px-2 py-0.5 rounded-full">BELIEBT</span>
                            </span>
                            <span class="font-bold text-orange-400">1,199€</span>
                        </div>
                        <div class="flex justify-between items-center border-b border-white/5 pb-2">
                            <span class="text-gray-300">60K Reels</span>
                            <span class="font-bold text-pink-400">1,999€</span>
                        </div>
                        <div class="flex justify-between items-center bg-orange-500/10 -mx-4 px-4 py-2 border-b border-white/5">
                            <span class="text-white font-semibold flex items-center gap-2">
                                125K+ Reels
                                <span class="text-xs bg-pink-500/20 text-pink-400 px-2 py-0.5 rounded-full">BEST VALUE</span>
                            </span>
                            <span class="font-bold text-pink-400">0.026€/Reel</span>
                        </div>
                        <div class="flex justify-between items-center bg-white/5 -mx-4 px-4 py-2 border-b border-white/5">
                            <span class="text-gray-300">125K Reels</span>
                            <span class="font-bold text-pink-400">3,250€</span>
                        </div>
                        <div class="flex justify-between items-center bg-white/5 -mx-4 px-4 py-2">
                            <span class="text-gray-300">250K Reels</span>
                            <span class="font-bold text-pink-400">6,500€</span>
                        </div>
                    </div>

                    <div class="mb-4 p-3 bg-orange-500/10 border border-orange-500/20 rounded-lg text-sm">
                        <p class="text-orange-300">
                            <strong>💡</strong> Custom Volumes ab 125K zum Flat-Rate-Preis
                        </p>
                    </div>

                    <a href="preisliste.html" class="block w-full py-3 bg-gradient-to-r from-pink-600 to-orange-600 hover:shadow-xl hover:shadow-pink-500/50 rounded-full font-semibold transition-all text-center">
                        Alle Instagram Pakete ansehen
                    </a>
                </div>

            </div>

            <!-- CTA Link to Full Pricing -->
            <div class="text-center mt-12">
                <a href="preisliste.html" class="inline-block text-lg text-violet-400 hover:text-pink-400 font-semibold transition-colors">
                    → Vollständige Preisliste ansehen
                </a>
            </div>
        </div>
    </section>'''

# Replace packages section
pattern = r'    <!-- Packages Section -->.*?    </section>'
content = re.sub(pattern, new_packages, content, count=1, flags=re.DOTALL)

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Packages section replaced!")
