#!/bin/bash
# GIT HISTORY CLEANUP SCRIPT
# Removes the exposed DeepL API key from all commits in Git history
# ⚠️ WARNING: This rewrites Git history! Make a backup first!

echo "================================================"
echo "GIT HISTORY CLEANUP - DeepL API Key Removal"
echo "================================================"
echo ""
echo "⚠️  WARNING: This will rewrite Git history!"
echo "⚠️  All collaborators will need to re-clone the repo!"
echo ""
echo "Exposed key: 47c6210a-e21d-4b9b-856a-06ad267eedb4"
echo ""
read -p "Do you want to continue? (yes/no): " confirm

if [ "$confirm" != "yes" ]; then
    echo "Aborted."
    exit 1
fi

echo ""
echo "Creating backup branch..."
git branch backup-before-history-cleanup

echo ""
echo "Step 1: Creating replacement file..."
cat > /tmp/git-secrets.txt << 'EOF'
47c6210a-e21d-4b9b-856a-06ad267eedb4==>REDACTED_DEEPL_API_KEY
EOF

echo ""
echo "Step 2: Checking if git-filter-repo is available..."
if command -v git-filter-repo &> /dev/null; then
    echo "✓ git-filter-repo found"
    echo ""
    echo "Step 3: Running git-filter-repo (RECOMMENDED METHOD)..."
    git-filter-repo --replace-text /tmp/git-secrets.txt --force
    
    echo ""
    echo "✓ Git history cleaned with git-filter-repo!"
else
    echo "✗ git-filter-repo not found"
    echo ""
    echo "Installing git-filter-repo..."
    python -m pip install git-filter-repo
    
    if [ $? -eq 0 ]; then
        echo "✓ Installation successful"
        echo ""
        echo "Step 3: Running git-filter-repo..."
        git-filter-repo --replace-text /tmp/git-secrets.txt --force
        echo "✓ Git history cleaned!"
    else
        echo ""
        echo "✗ Could not install git-filter-repo"
        echo ""
        echo "Falling back to git filter-branch (slower)..."
        echo "Step 3: Running git filter-branch..."
        
        git filter-branch --tree-filter '
            for file in deepl_test.py translate_critical.py auto_translate_system.py translate_batch.js translate_legal.js; do
                if [ -f "$file" ]; then
                    sed -i "s/47c6210a-e21d-4b9b-856a-06ad267eedb4/REDACTED_DEEPL_API_KEY/g" "$file"
                fi
            done
        ' --tag-name-filter cat -- --all
        
        echo ""
        echo "✓ Git history cleaned with filter-branch!"
    fi
fi

echo ""
echo "Step 4: Cleaning up Git refs..."
rm -rf .git/refs/original/
git reflog expire --expire=now --all
git gc --prune=now --aggressive

echo ""
echo "Step 5: Verifying cleanup..."
if git log --all -S "47c6210a-e21d-4b9b-856a-06ad267eedb4" --oneline | grep -q .; then
    echo "⚠️  WARNING: Old key still found in history!"
    echo "Manual cleanup may be required."
else
    echo "✓ No traces of old key in history!"
fi

echo ""
echo "================================================"
echo "CLEANUP COMPLETE"
echo "================================================"
echo ""
echo "Next steps:"
echo "1. Verify the cleanup: git log --all -S '47c6210a'"
echo "2. Force push to GitHub: git push --force origin main"
echo "3. Regenerate API key at https://www.deepl.com/pro-account/"
echo "4. Update .env with new key"
echo "5. Inform collaborators to re-clone the repo"
echo ""
echo "Backup branch created: backup-before-history-cleanup"
echo ""
