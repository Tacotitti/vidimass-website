# DeepL API Integration - Installation

## Setup Instructions

1. **Install Python dependencies:**
```bash
pip install requests python-dotenv beautifulsoup4
```

2. **Install Node.js dependencies:**
```bash
npm install
```

3. **Configure API Key:**
- Copy `.env.example` to `.env`
- Add your DeepL API key to `.env`
- **NEVER commit `.env` to Git!**

4. **Test API Connection:**
```bash
python deepl_test.py
```

## Security Notice

⚠️ **IMPORTANT:** The `.env` file contains your API key and is gitignored. Never commit API keys to version control!

If you accidentally expose your API key:
1. Immediately regenerate it at https://www.deepl.com/pro-account/
2. Update `.env` with the new key
3. Use `git filter-repo` or BFG to clean Git history
