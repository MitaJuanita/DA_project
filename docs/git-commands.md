# Git Commands for Project Updates

## First Time Setup
```bash
# Initialize repository if not already done
git init

# Add remote repository (replace with your repo URL)
git remote add origin https://github.com/MitaJuanita/DA_project.git
```

## Regular Workflow
```bash
# Check status of changes
git status

# Stage all changes
git add .

# Commit changes with descriptive message
git commit -m "Updated portfolio layout and blog content, improved mobile responsiveness"

# Push to main branch
git push origin main
```

## If Changes Are Rejected
```bash
# Pull latest changes first
git pull origin main

# Resolve any conflicts, then
git add .
git commit -m "Merged remote changes and resolved conflicts"
git push origin main
```
