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
