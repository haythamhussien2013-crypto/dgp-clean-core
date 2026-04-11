#!/data/data/com.termux/files/usr/bin/bash

echo "📊 Generating Smart Project Map..."

OUTPUT="PROJECT_MAP.md"
> "$OUTPUT"

echo "## 📁 PROJECT STRUCTURE" >> "$OUTPUT"
echo "" >> "$OUTPUT"

find . -type d -print0 | while IFS= read -r -d '' dir; do
    echo "## 📁 $dir" >> "$OUTPUT"

    find "$dir" -maxdepth 1 -type f -print0 | while IFS= read -r -d '' file; do
        echo "- $(basename "$file")" >> "$OUTPUT"
    done

    echo "" >> "$OUTPUT"
done

echo "✅ DONE"	
