import time
import random
from datetime import datetime
from pathlib import Path

from run_dgp import CyberGodTester


class DGPTestSuite:

    def __init__(self):
        self.results = []
        self.start_time = time.time()

    def log(self, name, runs, failures):
        success = ((runs - failures) / runs) * 100 if runs else 0
        self.results.append((name, runs, failures, round(success, 2)))

    def basic_test(self):
        tester = CyberGodTester()
        runs = 100
        failures = 0

        for i in range(runs):
            badge, _ = tester.get_badge_for_level(i + 1)
            if badge == "unknown":
                failures += 1

        self.log("BASIC TEST", runs, failures)

    def extreme_test(self):
        tester = CyberGodTester()
        runs = 100
        failures = 0

        for i in range(runs):
            badge, _ = tester.get_badge_for_level((i % 100) + 1)
            if badge == "unknown":
                failures += 1

        self.log("EXTREME TEST", runs, failures)

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

        self.log("RANDOM TEST", runs, failures)

    def generate_report(self):
        total_runs = sum(r[1] for r in self.results)
        total_failures = sum(r[2] for r in self.results)

        duration = round(time.time() - self.start_time, 2)

        report = "\n💀 MASTER TEST REPORT\n"
        report += "========================\n"

        for name, runs, fail, rate in self.results:
            report += f"\n{name}\n"
            report += f"Runs: {runs}\n"
            report += f"Failures: {fail}\n"
            report += f"Success Rate: {rate}%\n"

        report += "\n========================\n"
        report += f"TOTAL RUNS: {total_runs}\n"
        report += f"TOTAL FAILURES: {total_failures}\n"
        report += f"TIME: {duration} sec\n"

        Path("../reports").mkdir(exist_ok=True)

        filename = f"../reports/master_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, "w") as f:
            f.write(report)

        print(report)
        print("\nSaved:", filename)


if __name__ == "__main__":
    suite = DGPTestSuite()

    suite.basic_test()
    suite.extreme_test()
    suite.random_test()

    suite.generate_report()
