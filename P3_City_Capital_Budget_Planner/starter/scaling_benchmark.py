from statistics import median
from time import perf_counter
import csv

from my_solutions import solve_dp

# Increase this for more stable timings, but the experiment will take longer.
RUNS = 5


def make_instance(n, budget):
    costs = [((i * 17) % 50) + 1 for i in range(n)]
    # These formulas create repeatable costs and benefits without randomness.
    # Change them only if you want a different synthetic data distribution.
    benefits = [((i * 23) % 100) + 10 for i in range(n)]

    return {
        "n": n,
        "budget": budget,
        "cost": costs,
        "benefit": benefits
    }


def measure(inst):
    times = []

    for _ in range(RUNS):
        start = perf_counter()
        solve_dp(inst)
        times.append(perf_counter() - start)

    # Median reduces the effect of unusually fast or slow runs.
    return median(times)


def count_operations(inst):
    # Counts how many times the DP inner budget loop executes.
    return sum(
        max(0, inst["budget"] - cost + 1)
        for cost in inst["cost"]
    )


def main():
    results = []

    print("Changing n while budget stays at 1000")

    # Change these values to test more project counts.
    # Keep the budget fixed to isolate the effect of n.
    for n in [20, 50, 100, 200, 400, 800]:
        inst = make_instance(n, 1000)
        runtime = measure(inst)
        operations = count_operations(inst)

        # Keep this order consistent with the CSV header below.
        results.append(["change_n", n, 1000, runtime, operations])
        print("n =", n, "time =", f"{runtime:.6f}")

    print("\nChanging budget while n stays at 100")

    # Change these values to test more budgets.
    # Keep n fixed to isolate the effect of B.
    for budget in [100, 250, 500, 1000, 2000, 4000]:
        inst = make_instance(100, budget)
        runtime = measure(inst)
        operations = count_operations(inst)

        # Keep this order consistent with the CSV header below.
        results.append(["change_budget", 100, budget, runtime, operations])
        print("budget =", budget, "time =", f"{runtime:.6f}")

    # This replaces the previous results file each time the script runs.
    with open("scaling_results.csv", "w", newline="") as file:
        writer = csv.writer(file)
        # Keep these columns in the same order as results.append().
        writer.writerow([
            "experiment",
            "n",
            "budget",
            "median_seconds",
            "operations"
        ])
        writer.writerows(results)

    print("\nResults saved to scaling_results.csv")

# Prevent the benchmark from running when this file is imported.
if __name__ == "__main__":
    main()