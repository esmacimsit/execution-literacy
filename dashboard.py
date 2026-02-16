import sys
import subprocess
from datetime import datetime
from pathlib import Path

RESULTS_FILE = Path("dashboard.log")

if len(sys.argv) < 2:
    print("Usage:")
    print("  python dashboard.py path/to/script.py")
    print("  python dashboard.py path/to/folder")
    sys.exit(1)

target = Path(sys.argv[1])

def run_script(script_path):
    print(f"\nRunning: {script_path}\n")

    proc = subprocess.run(
        ["python3", str(script_path)],
        capture_output=True,
        text=True
    )

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = (
        f"\n===== {timestamp} =====\n"
        f"Script: {script_path}\n\n"
        f"{proc.stdout}\n"
    )

    if proc.stderr:
        log_entry += f"\n[ERROR]\n{proc.stderr}\n"

    print(proc.stdout)

    if proc.stderr:
        print("Error:")
        print(proc.stderr)

    with RESULTS_FILE.open("a", encoding="utf-8") as f:
        f.write(log_entry)


if target.is_file():
    run_script(target)

elif target.is_dir():
    # klasördeki tüm .py dosyalarını çalıştır
    scripts = sorted(target.glob("*.py"))
    for script in scripts:
        run_script(script)

else:
    print("Invalid path.")