from pathlib import Path
from statistics import median
from time import perf_counter
import csv

from problem import load_instance
from my_solutions import solve_greedy, solve_dp

# This path works when benchmark.py remains inside the starter folder.
DATA_FOLDER = Path(__file__).parent.parent / "data"
# Increase RUNS for more stable timings, but the benchmark will take longer
RUNS = 5


def score(inst, selected):
    return sum(inst["benefit"][i] for i in selected)


def median_time(function, inst):
    times = []

    for _ in range(RUNS):
        start = perf_counter()
        function(inst)
        times.append(perf_counter() - start)

    # Median reduces the effect of unusually fast or slow runs.
    return median(times)


def main():
    results = []

    # Change the file pattern here to benchmark a different group of datasets.
    for path in sorted(DATA_FOLDER.glob("projects_*.json")):
        inst = load_instance(path)

        greedy_selected = solve_greedy(inst)
        dp_selected = solve_dp(inst)

        greedy_score = score(inst, greedy_selected)
        dp_score = score(inst, dp_selected)

        greedy_time = median_time(solve_greedy, inst)
        dp_time = median_time(solve_dp, inst)

        # Keep this check to avoid division by zero on empty instances.
        if dp_score == 0:
            loss = 0
        else:
            loss = ((dp_score - greedy_score) / dp_score) * 100

        # These are main-loop operation counts.
        # Greedy's count does not include sorting comparisons.
        greedy_operations = inst["n"]
        # Each term counts the number of budget values checked
        # for one project in the DP inner loop
        dp_operations = sum(
            max(0, inst["budget"] - cost + 1)
            for cost in inst["cost"]
        )

        # Keep this order consistent with the CSV header below.
        results.append([
            path.name,
            inst["n"],
            inst["budget"],
            greedy_score,
            dp_score,
            round(loss, 2),
            greedy_time,
            dp_time,
            greedy_operations,
            dp_operations
        ])

        print(
            path.name,
            "Greedy:", greedy_score,
            "DP:", dp_score,
            "Loss:", f"{loss:.2f}%",
            "Greedy time:", f"{greedy_time:.6f}",
            "DP time:", f"{dp_time:.6f}"
        )

    # This replaces the previous CSV each time the benchmark runs.
    with open("benchmark_results.csv", "w", newline="") as file:
        writer = csv.writer(file)
        # Keep these columns in the same order as results.append().
        writer.writerow([
            "dataset",
            "n",
            "budget",
            "greedy_score",
            "dp_score",
            "greedy_loss_percent",
            "greedy_median_seconds",
            "dp_median_seconds",
            "greedy_operations",
            "dp_operations"
        ])
        writer.writerows(results)

    print("\nResults saved to benchmark_results.csv")

# Prevent the benchmark from running when this file is imported.
if __name__ == "__main__":
    main()