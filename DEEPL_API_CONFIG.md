# DeepL API Translation Tool Configuration

## API Access
**Service:** DeepL Pro API
**Endpoint:** https://api.deepl.com/v2/translate
**Auth Method:** Header-based (`Authorization: DeepL-Auth-Key {KEY}`)

## Current API Key
**Status:** ✅ Active (rotated 2026-04-05 12:49 GMT+2)
**Storage Location:** `.env` file (gitignored, secure)
**Key:** [Stored in .env file - NOT in Git]

## Previous Key
**Old Key:** 47c6210a-e21d-4b9b-856a-06ad267eedb4
**Status:** 🚫 REVOKED (exposed on GitHub 2026-04-05)
**Action Taken:** Rotated to new key

## Usage Instructions

### For Python Scripts
All translation scripts now use environment variables:

```python
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get API key securely
DEEPL_API_KEY = os.getenv('DEEPL_API_KEY')

# Use in API calls
headers = {
    "Authorization": f"DeepL-Auth-Key {DEEPL_API_KEY}",
    "Content-Type": "application/json"
}
```

### Scripts Updated with .env Support
- ✅ deepl_test.py
- ✅ translate_critical.py
- ✅ auto_translate_system.py
- ✅ Any future translation scripts

### To Use Translation Scripts:
1. Make sure `.env` file exists in project root
2. Verify API key is present: `DEEPL_API_KEY=...`
3. Run script: `python deepl_test.py`
4. Script automatically loads key from .env

## Security Best Practices

### ✅ DO:
- Store API keys in `.env` file
- Add `.env` to `.gitignore`
- Use environment variables in code
- Create `.env.example` as template
- Rotate keys if exposed

### ❌ DON'T:
- Hardcode API keys in source code
- Commit `.env` files to Git
- Share API keys in chat/email
- Store keys in memory files
- Include keys in documentation

## API Limits & Usage
- **Batch Translation:** Up to 50 texts per API call
- **Supported Languages:** EN, DE, TR, PT-PT, ES, RU, ZH, AR (we use 5: EN, DE, TR, PT, ES)
- **Format:** JSON request/response
- **Rate Limiting:** 1 second delay between batches recommended

## Backup & Recovery
If API key is lost:
1. Check `.env` file in project root
2. If missing, regenerate at https://www.deepl.com/pro-account/
3. Update `.env` file with new key
4. Test with `python deepl_test.py`

## Translation Cache
Translations are cached in `auto_translations.json` to reduce API calls and costs.

---

**Last Updated:** 2026-04-05 12:49 GMT+2
**Status:** ✅ Secure, key rotated, ready to use
