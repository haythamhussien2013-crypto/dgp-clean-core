import time
import random
import subprocess

RUNS = 100
failures = 0

start = time.time()

for i in range(RUNS):
    print(f"[{i+1}/{RUNS}] Running test...")

    try:
        result = subprocess.run(
            ["python", "core/run_dgp.py"],
            timeout=20,
            capture_output=True
        )

        if result.returncode != 0:
            failures += 1

    except Exception as e:
        failures += 1
        print("Error:", e)

end = time.time()

print("\n💀 EXTREME TEST RESULTS")
print("======================")
print("Runs:", RUNS)
print("Failures:", failures)
print("Success Rate:", (RUNS - failures) / RUNS * 100, "%")
print("Total Time:", round(end - start, 2), "sec")
