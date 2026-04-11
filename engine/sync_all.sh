#!/bin/bash

echo "🚀 START SYNC SYSTEM..."

# sync from onedrive
rclone sync onedrive: ~/global_project/onedrive_backup

# enter project
cd ~/global_project || exit

# add changes
git add .

# commit with date
git commit -m "auto sync $(date)"

# push to gitlab
git push origin main

echo "✅ SYNC COMPLETE"

