from statistics import median
from time import perf_counter
import csv

from my_solutions import solve_dp


RUNS = 5


def make_instance(n, budget):
    costs = [((i * 17) % 50) + 1 for i in range(n)]
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

    return median(times)


def count_operations(inst):
    return sum(
        max(0, inst["budget"] - cost + 1)
        for cost in inst["cost"]
    )


def main():
    results = []

    print("Changing n while budget stays at 1000")

    for n in [20, 50, 100, 200, 400, 800]:
        inst = make_instance(n, 1000)
        runtime = measure(inst)
        operations = count_operations(inst)

        results.append(["change_n", n, 1000, runtime, operations])
        print("n =", n, "time =", f"{runtime:.6f}")

    print("\nChanging budget while n stays at 100")

    for budget in [100, 250, 500, 1000, 2000, 4000]:
        inst = make_instance(100, budget)
        runtime = measure(inst)
        operations = count_operations(inst)

        results.append(["change_budget", 100, budget, runtime, operations])
        print("budget =", budget, "time =", f"{runtime:.6f}")

    with open("scaling_results.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "experiment",
            "n",
            "budget",
            "median_seconds",
            "operations"
        ])
        writer.writerows(results)

    print("\nResults saved to scaling_results.csv")


if __name__ == "__main__":
    main()