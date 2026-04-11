import os

REPORTS_DIR = "reports"
README_FILE = "README.md"

def get_latest_report():
    files = sorted(os.listdir(REPORTS_DIR))
    txt_files = [f for f in files if f.endswith(".txt")]

    if not txt_files:
        return None

    latest = txt_files[-1]
    with open(os.path.join(REPORTS_DIR, latest), "r") as f:
        return f.read(), latest


def update_readme(report_text, filename):
    section = f"""
## 🔥 Latest Execution Report

File: {filename}
"""

    if os.path.exists(README_FILE):
        with open(README_FILE, "r") as f:
            content = f.read()
    else:
        content = "# DGP Project\n"

    if "## 🔥 Latest Execution Report" in content:
        content = content.split("## 🔥 Latest Execution Report")[0]

    new_content = content + section

    with open(README_FILE, "w") as f:
        f.write(new_content)

    print("✅ README updated")


if __name__ == "__main__":
    result = get_latest_report()

    if result:
        report_text, filename = result
        update_readme(report_text, filename)
    else:
        print("❌ No reports found")
