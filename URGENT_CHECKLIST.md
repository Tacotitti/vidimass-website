# 🔴 URGENT: Complete Security Fix Checklist

## ✅ ALREADY DONE (by automated fix)
- [x] Removed hardcoded API keys from all files
- [x] Created .env system for secure key storage
- [x] Added .gitignore to prevent future leaks
- [x] Pushed secure version to GitHub
- [x] Created cleanup scripts

---

## 🔴 YOU MUST DO NOW (< 15 minutes)

### Step 1: Clean Git History (5 min)
Old commits still contain the exposed key!

```powershell
cd C:\Users\Sebas\.openclaw\workspace\vidimass-website
.\cleanup-git-history.ps1
```

**After cleanup succeeds:**
```bash
git push --force origin main
```

### Step 2: Regenerate API Key (5 min)
1. Go to: https://www.deepl.com/pro-account/
2. Click **"API Keys"** section
3. **Delete** key: `47c6210a-e21d-4b9b-856a-06ad267eedb4`
4. Click **"Create new key"**
5. Copy the new key

### Step 3: Update Local .env (1 min)
```bash
cd C:\Users\Sebas\.openclaw\workspace\vidimass-website
notepad .env
```

Replace old key with new key:
```env
DEEPL_API_KEY=YOUR_NEW_KEY_HERE
```

Save and close.

### Step 4: Test Everything (2 min)
```bash
python deepl_test.py
```

**Expected:**
```
OK DeepL API works!
Translated (EN): Mass Posting for TikTok, Instagram & Spotify Charting
✅ API is ready to use!
```

### Step 5: Verify GitHub (1 min)
Search GitHub for old key:
https://github.com/Tacotitti/vidimass-website/search?q=47c6210a

**Should show:** 0 results ✅

---

## 📋 Quick Verification

Run these commands to verify everything is secure:

```powershell
# Check local files (should return nothing)
cd C:\Users\Sebas\.openclaw\workspace
Get-ChildItem -Recurse -File -Exclude .env | Select-String -Pattern "47c6210a"

# Check Git history (should return nothing after cleanup)
cd vidimass-website
git log --all -S "47c6210a" --oneline

# Test API with new key
python deepl_test.py
```

---

## ❓ If Something Goes Wrong

### Cleanup Script Fails
**Try alternative:** Download BFG Repo-Cleaner
1. Get from: https://rtyley.github.io/bfg-repo-cleaner/
2. Create `secrets.txt`:
   ```
   47c6210a-e21d-4b9b-856a-06ad267eedb4==>REDACTED
   ```
3. Run:
   ```bash
   java -jar bfg.jar --replace-text secrets.txt .git
   git reflog expire --expire=now --all
   git gc --prune=now --aggressive
   git push --force origin main
   ```

### New API Key Doesn't Work
1. Check `.env` file has correct format:
   ```env
   DEEPL_API_KEY=abc123-def456-...
   ```
   (No quotes, no spaces)

2. Verify key is active at DeepL dashboard

3. Try in browser: https://api.deepl.com/v2/usage
   - Add header: `Authorization: DeepL-Auth-Key YOUR_KEY`

### Git Push --force Rejected
```bash
git push --force-with-lease origin main
```

If still fails:
```bash
git push --force origin main --no-verify
```

---

## 📚 Documentation Created

All details in these files:
- `SECURITY_INCIDENT_REPORT.md` - Full incident report
- `README_SECURITY.md` - Security setup guide
- `cleanup-git-history.ps1` - Automated cleanup script
- `memory/2026-04-05-security-incident.md` - Memory log

---

**PRIORITY:** 🔴 CRITICAL - Complete within 15 minutes!

**Questions?** Check `SECURITY_INCIDENT_REPORT.md` for detailed explanations.
