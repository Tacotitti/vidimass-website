import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# New simple packages section with link to preisliste
new_packages = '''    <!-- Packages Section -->
    <section id="packages" class="packages-section py-24 relative">
        <div class="container mx-auto px-6">
            <div class="text-center mb-16">
                <h2 class="text-4xl md:text-5xl font-bold mb-4">
                    Unsere <span class="bg-gradient-to-r from-violet-400 to-pink-400 bg-clip-text text-transparent"><span data-i18n="packages_title_2">Pakete</span></span>
                </h2>
                <p class="text-xl text-gray-400 max-w-2xl mx-auto">
                    Flexible Preise für TikTok und Instagram Mass Posting
                </p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-6xl mx-auto">
                <!-- Starter Package -->
                <div class="package-card glass-card p-8 rounded-2xl hover:border-violet-500/50 transition-all">
                    <div class="text-sm font-semibold text-violet-400 mb-2">STARTER</div>
                    <div class="text-4xl font-bold mb-4"><span data-i18n="package_starter_price">$99</span></div>
                    <p class="text-gray-400 mb-6"><span data-i18n="package_starter_desc">Perfect for individual creators</span></p>
                    <ul class="space-y-3 mb-8">
                        <li class="flex items-start gap-2">
                            <svg class="w-5 h-5 text-green-400 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                            </svg>
                            <span class="text-gray-300">Up to 1,000 videos/day</span>
                        </li>
                        <li class="flex items-start gap-2">
                            <svg class="w-5 h-5 text-green-400 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                            </svg>
                            <span class="text-gray-300">1 Plattform</span>
                        </li>
                        <li class="flex items-start gap-2">
                            <svg class="w-5 h-5 text-green-400 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                            </svg>
                            <span class="text-gray-300">Analytics</span>
                        </li>
                        <li class="flex items-start gap-2">
                            <svg class="w-5 h-5 text-green-400 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                            </svg>
                            <span class="text-gray-300">Dedicated support</span>
                        </li>
                        <li class="flex items-start gap-2">
                            <svg class="w-5 h-5 text-green-400 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                            </svg>
                            <span class="text-gray-300">Custom integration</span>
                        </li>
                    </ul>
                    <a href="preisliste.html" class="block w-full py-3 bg-white/10 hover:bg-white/20 rounded-full font-semibold transition-all text-center">
                        Preise ansehen
                    </a>
                </div>

                <!-- Pro Package (Featured) -->
                <div class="package-card glass-card p-8 rounded-2xl border-2 border-violet-500 relative transform md:scale-105 hover:border-violet-400 transition-all">
                    <div class="absolute -top-4 left-1/2 transform -translate-x-1/2 px-4 py-1 bg-gradient-to-r from-violet-600 to-pink-600 rounded-full text-sm font-bold">
                        POPULAR
                    </div>
                    <div class="text-sm font-semibold text-violet-400 mb-2">PRO</div>
                    <div class="text-4xl font-bold mb-4"><span data-i18n="package_pro_price">$299</span></div>
                    <p class="text-gray-400 mb-6"><span data-i18n="package_pro_desc">For growing brands</span></p>
                    <ul class="space-y-3 mb-8">
                        <li class="flex items-start gap-2">
                            <svg class="w-5 h-5 text-green-400 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                            </svg>
                            <span class="text-gray-300">Up to 50,000 videos/day</span>
                        </li>
                        <li class="flex items-start gap-2">
                            <svg class="w-5 h-5 text-green-400 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                            </svg>
                            <span class="text-gray-300">1 Plattform</span>
                        </li>
                        <li class="flex items-start gap-2">
                            <svg class="w-5 h-5 text-green-400 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                            </svg>
                            <span class="text-gray-300">Analytics</span>
                        </li>
                        <li class="flex items-start gap-2">
                            <svg class="w-5 h-5 text-green-400 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                            </svg>
                            <span class="text-gray-300">Dedicated support</span>
                        </li>
                        <li class="flex items-start gap-2">
                            <svg class="w-5 h-5 text-green-400 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                            </svg>
                            <span class="text-gray-300">Custom integration</span>
                        </li>
                    </ul>
                    <a href="preisliste.html" class="block w-full py-3 bg-gradient-to-r from-violet-600 to-pink-600 hover:shadow-xl hover:shadow-violet-500/50 rounded-full font-semibold transition-all text-center">
                        Preise ansehen
                    </a>
                </div>

                <!-- Enterprise Package -->
                <div class="package-card glass-card p-8 rounded-2xl hover:border-violet-500/50 transition-all">
                    <div class="text-sm font-semibold text-violet-400 mb-2">ENTERPRISE</div>
                    <div class="text-4xl font-bold mb-4"><span data-i18n="package_enterprise_price">Custom</span></div>
                    <p class="text-gray-400 mb-6"><span data-i18n="package_enterprise_desc">For large organizations</span></p>
                    <ul class="space-y-3 mb-8">
                        <li class="flex items-start gap-2">
                            <svg class="w-5 h-5 text-green-400 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                            </svg>
                            <span class="text-gray-300">Up to 250,000 videos/day</span>
                        </li>
                        <li class="flex items-start gap-2">
                            <svg class="w-5 h-5 text-green-400 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                            </svg>
                            <span class="text-gray-300">1 Plattform</span>
                        </li>
                        <li class="flex items-start gap-2">
                            <svg class="w-5 h-5 text-green-400 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                            </svg>
                            <span class="text-gray-300">Analytics</span>
                        </li>
                        <li class="flex items-start gap-2">
                            <svg class="w-5 h-5 text-green-400 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                            </svg>
                            <span class="text-gray-300">Dedicated support</span>
                        </li>
                        <li class="flex items-start gap-2">
                            <svg class="w-5 h-5 text-green-400 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                            </svg>
                            <span class="text-gray-300">Custom integration</span>
                        </li>
                    </ul>
                    <a href="preisliste.html" class="block w-full py-3 bg-white/10 hover:bg-white/20 rounded-full font-semibold transition-all text-center">
                        Kontakt aufnehmen
                    </a>
                </div>
            </div>

            <!-- CTA to Pricing Page -->
            <div class="text-center mt-16">
                <a href="preisliste.html" class="inline-block px-10 py-5 bg-gradient-to-r from-violet-600 to-pink-600 rounded-full font-bold text-xl hover:shadow-2xl hover:shadow-violet-500/50 transition-all transform hover:scale-105">
                    → Vollständige Preisliste ansehen
                </a>
            </div>
        </div>
    </section>'''

# Replace
pattern = r'    <!-- Packages Section -->.*?    </section>'
content = re.sub(pattern, new_packages, content, count=1, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("OK - Restored simple packages")
