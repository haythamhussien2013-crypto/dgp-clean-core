import time
import random
from pathlib import Path
from datetime import datetime
from core.run_dgp import CyberGodTester


class DGPTestSuite:

    def __init__(self):
        self.results = []
        self.start_time = time.time()

    def log(self, name, runs, failures):
        success_rate = ((runs - failures) / runs) * 100 if runs else 0

        result = {
            "name": name,
            "runs": runs,
            "failures": failures,
            "success_rate": round(success_rate, 2)
        }

        self.results.append(result)

    # 🧪 1. Basic Test
    def basic_test(self):
        tester = CyberGodTester()
        runs = 100
        failures = 0

        for i in range(runs):
            badge, _ = tester.get_badge_for_level(i + 1)
            if badge == "unknown":
                failures += 1

        self.log("BASIC VALIDATION", runs, failures)

    # 🧪 2. Extreme Test
    def extreme_test(self):
        tester = CyberGodTester()
        runs = 100
        failures = 0

        for i in range(runs):
            badge, _ = tester.get_badge_for_level((i % 100) + 1)
            if badge == "unknown":
                failures += 1

        self.log("EXTREME TEST", runs, failures)

    # 🧪 3. Random Input
    def random_test(self):
        tester = CyberGodTester()
        runs = 1000
        failures = 0

        for _ in range(runs):
            level = random.randint(-500, 2000)
            badge, _ = tester.get_badge_for_level(level)

            if 1 <= level <= 100:
                if badge == "unknown":
                    failures += 1
            else:
                if badge != "unknown":
                    failures += 1

        self.log("RANDOM INPUT TEST", runs, failures)

    # 🧪 4. Stress Test
    def stress_test(self):
        tester = CyberGodTester()
        runs = 2000
        failures = 0

        for i in range(runs):
            badge, _ = tester.get_badge_for_level((i % 100) + 1)
            if badge == "unknown":
                failures += 1

        self.log("STRESS TEST", runs, failures)

    # 📊 تقرير نهائي
    def generate_report(self):
        total_runs = sum(r["runs"] for r in self.results)
        total_failures = sum(r["failures"] for r in self.results)

        duration = round(time.time() - self.start_time, 2)

        report = "\n💀 DGP MASTER TEST REPORT\n"
        report += "============================\n"

        for r in self.results:
            report += f"\n{r['name']}\n"
            report += f"Runs: {r['runs']}\n"
            report += f"Failures: {r['failures']}\n"
            report += f"Success Rate: {r['success_rate']}%\n"

        report += "\n============================\n"
        report += f"TOTAL RUNS: {total_runs}\n"
        report += f"TOTAL FAILURES: {total_failures}\n"
        report += f"TOTAL SUCCESS RATE: {round((total_runs-total_failures)/total_runs*100,2)}%\n"
        report += f"TIME: {duration} sec\n"

        Path("reports").mkdir(exist_ok=True)

        filename = f"reports/master_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, "w") as f:
            f.write(report)

        print(report)
        print(f"\n📄 Saved to: {filename}")


# 🔥 التشغيل
if __name__ == "__main__":
    suite = DGPTestSuite()

    suite.basic_test()
    suite.extreme_test
