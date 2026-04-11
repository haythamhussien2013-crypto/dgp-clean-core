#!/data/data/com.termux/files/usr/bin/bash

echo "📊 Generating Smart Project Map..."

echo "## 📁 PROJECT STRUCTURE" > PROJECT_MAP.md
echo "" >> PROJECT_MAP.md

find . -type d | while read dir; do
    echo "## 📁 $dir" >> PROJECT_MAP.md

    find "$dir" -maxdepth 1 -type f | while read file; do
        echo "- $(basename "$file")" >> PROJECT_MAP.md
    done

    echo "" >> PROJECT_MAP.md
done

echo "✅ DONE"
