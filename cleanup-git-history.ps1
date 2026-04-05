# GIT HISTORY CLEANUP SCRIPT (PowerShell)
# Removes the exposed DeepL API key from all commits in Git history
# ⚠️ WARNING: This rewrites Git history! Make a backup first!

Write-Host "================================================" -ForegroundColor Yellow
Write-Host "GIT HISTORY CLEANUP - DeepL API Key Removal" -ForegroundColor Yellow
Write-Host "================================================" -ForegroundColor Yellow
Write-Host ""
Write-Host "⚠️  WARNING: This will rewrite Git history!" -ForegroundColor Red
Write-Host "⚠️  All collaborators will need to re-clone the repo!" -ForegroundColor Red
Write-Host ""
Write-Host "Exposed key: 47c6210a-e21d-4b9b-856a-06ad267eedb4"
Write-Host ""

$confirm = Read-Host "Do you want to continue? (yes/no)"

if ($confirm -ne "yes") {
    Write-Host "Aborted." -ForegroundColor Yellow
    exit 1
}

Write-Host ""
Write-Host "Creating backup branch..." -ForegroundColor Cyan
git branch backup-before-history-cleanup

Write-Host ""
Write-Host "Checking Python availability..." -ForegroundColor Cyan
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Python not found! Please install Python first." -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "Installing git-filter-repo..." -ForegroundColor Cyan
python -m pip install git-filter-repo --quiet

Write-Host ""
Write-Host "Creating replacement file..." -ForegroundColor Cyan
$replacementFile = "git-secrets-replacement.txt"
"47c6210a-e21d-4b9b-856a-06ad267eedb4==>REDACTED_DEEPL_API_KEY" | Out-File -FilePath $replacementFile -Encoding ASCII

Write-Host ""
Write-Host "Running git-filter-repo to clean history..." -ForegroundColor Cyan
Write-Host "(This may take a few minutes...)" -ForegroundColor Gray

# Try git-filter-repo first
$filterRepoAvailable = $false
try {
    git filter-repo --replace-text $replacementFile --force 2>&1 | Out-Null
    $filterRepoAvailable = $true
    Write-Host "✓ Git history cleaned with git-filter-repo!" -ForegroundColor Green
} catch {
    Write-Host "✗ git-filter-repo failed, trying alternative method..." -ForegroundColor Yellow
}

# Fallback to BFG if filter-repo failed
if (-not $filterRepoAvailable) {
    Write-Host ""
    Write-Host "Alternative: Manual commit replacement" -ForegroundColor Yellow
    Write-Host "This requires BFG Repo-Cleaner: https://rtyley.github.io/bfg-repo-cleaner/" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Download bfg.jar and run:" -ForegroundColor Cyan
    Write-Host "  java -jar bfg.jar --replace-text $replacementFile .git" -ForegroundColor White
    Write-Host ""
    
    $useBFG = Read-Host "Do you have BFG downloaded? (yes/no)"
    if ($useBFG -eq "yes") {
        $bfgPath = Read-Host "Enter path to bfg.jar"
        if (Test-Path $bfgPath) {
            Write-Host "Running BFG Repo-Cleaner..." -ForegroundColor Cyan
            java -jar $bfgPath --replace-text $replacementFile .git
            Write-Host "✓ BFG cleanup complete!" -ForegroundColor Green
        } else {
            Write-Host "✗ BFG file not found: $bfgPath" -ForegroundColor Red
            exit 1
        }
    } else {
        Write-Host ""
        Write-Host "✗ Manual cleanup required!" -ForegroundColor Red
        Write-Host "Options:" -ForegroundColor Yellow
        Write-Host "1. Download BFG: https://rtyley.github.io/bfg-repo-cleaner/" -ForegroundColor White
        Write-Host "2. Install git-filter-repo manually" -ForegroundColor White
        Write-Host "3. Contact support for assistance" -ForegroundColor White
        exit 1
    }
}

Write-Host ""
Write-Host "Cleaning up Git refs..." -ForegroundColor Cyan
git reflog expire --expire=now --all 2>&1 | Out-Null
git gc --prune=now --aggressive 2>&1 | Out-Null

Write-Host ""
Write-Host "Verifying cleanup..." -ForegroundColor Cyan
$remainingKeys = git log --all -S "47c6210a-e21d-4b9b-856a-06ad267eedb4" --oneline

if ($remainingKeys) {
    Write-Host "⚠️  WARNING: Old key still found in history!" -ForegroundColor Red
    Write-Host "Found in commits:" -ForegroundColor Yellow
    Write-Host $remainingKeys
    Write-Host ""
    Write-Host "Manual cleanup required - see README_SECURITY.md" -ForegroundColor Yellow
} else {
    Write-Host "✓ No traces of old key in history!" -ForegroundColor Green
}

Remove-Item $replacementFile -ErrorAction SilentlyContinue

Write-Host ""
Write-Host "================================================" -ForegroundColor Green
Write-Host "CLEANUP COMPLETE" -ForegroundColor Green
Write-Host "================================================" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Verify the cleanup: git log --all -S '47c6210a'" -ForegroundColor White
Write-Host "2. Force push to GitHub: git push --force origin main" -ForegroundColor White
Write-Host "3. Regenerate API key at https://www.deepl.com/pro-account/" -ForegroundColor White
Write-Host "4. Update .env with new key" -ForegroundColor White
Write-Host "5. Inform collaborators to re-clone the repo" -ForegroundColor White
Write-Host ""
Write-Host "Backup branch created: backup-before-history-cleanup" -ForegroundColor Yellow
Write-Host ""
