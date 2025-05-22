# Git Commands Reference

## Initial Setup
```bash
# Initialize repository
git init

# Configure user
git config --global user.name "Sherminta Lawrence"
git config --global user.email "shermintalawrence@gmail.com"
```

## Basic Workflow
```bash
# Check status
git status

# Add files
git add .                    # Add all files
git add specific-file.html   # Add specific file

# Commit changes
git commit -m "Description of changes"

# Push to remote
git push origin main
```

## Branching
```bash
# Create & switch to new branch
git checkout -b feature-name

# Switch branches
git checkout main

# Merge branch
git merge feature-name
```

## Updates & History
```bash
# Get latest changes
git pull origin main

# View commit history
git log
git log --oneline      # Compact view

# View specific commit
git show commit-hash
```

## Common Scenarios
```bash
# Undo last commit (keep changes)
git reset --soft HEAD~1

# Discard changes in working directory
git checkout -- file.html

# Create/apply patch
git diff > changes.patch
git apply changes.patch
```

## Best Practices
- Write clear commit messages
- Commit often, push regularly
- Branch for new features
- Keep main/master branch stable
