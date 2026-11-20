import csv
import matplotlib.pyplot as plt


def read_csv(filename):
    with open(filename, newline="") as file:
        return list(csv.DictReader(file))


def dp_scaling_plots():
    rows = read_csv("scaling_results.csv")

    change_n = [r for r in rows if r["experiment"] == "change_n"]
    change_n.sort(key=lambda r: int(r["n"]))

    n_values = [int(r["n"]) for r in change_n]
    n_times = [float(r["median_seconds"]) for r in change_n]

    plt.figure()
    plt.plot(n_values, n_times, marker="o")
    plt.title("DP Runtime as Number of Projects Increases")
    plt.xlabel("Number of projects (n)")
    plt.ylabel("Median runtime (seconds)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("dp_runtime_vs_n.png")
    plt.close()

    change_budget = [
        r for r in rows if r["experiment"] == "change_budget"
    ]
    change_budget.sort(key=lambda r: int(r["budget"]))

    budgets = [int(r["budget"]) for r in change_budget]
    budget_times = [float(r["median_seconds"]) for r in change_budget]

    plt.figure()
    plt.plot(budgets, budget_times, marker="o", color="orange")
    plt.title("DP Runtime as Budget Increases")
    plt.xlabel("Budget (B)")
    plt.ylabel("Median runtime (seconds)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("dp_runtime_vs_budget.png")
    plt.close()


def comparison_plots():
    rows = read_csv("benchmark_results.csv")

    labels = [
        r["dataset"].replace("projects_", "").replace(".json", "")
        for r in rows
    ]

    losses = [float(r["greedy_loss_percent"]) for r in rows]

    plt.figure(figsize=(10, 5))
    plt.bar(labels, losses, color="steelblue")
    plt.title("Greedy Benefit Loss Compared with DP")
    plt.xlabel("Dataset")
    plt.ylabel("Benefit loss (%)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("greedy_loss.png")
    plt.close()

    greedy_times = [
        float(r["greedy_median_seconds"]) for r in rows
    ]
    dp_times = [
        float(r["dp_median_seconds"]) for r in rows
    ]

    x = list(range(len(labels)))
    width = 0.4

    plt.figure(figsize=(10, 5))
    plt.bar(
        [i - width / 2 for i in x],
        greedy_times,
        width,
        label="Greedy"
    )
    plt.bar(
        [i + width / 2 for i in x],
        dp_times,
        width,
        label="DP"
    )
    plt.yscale("log")
    plt.title("Greedy and DP Runtime Comparison")
    plt.xlabel("Dataset")
    plt.ylabel("Median runtime in seconds (log scale)")
    plt.xticks(x, labels, rotation=45, ha="right")
    plt.legend()
    plt.tight_layout()
    plt.savefig("runtime_comparison.png")
    plt.close()


def main():
    dp_scaling_plots()
    comparison_plots()

    print("Created:")
    print(" dp_runtime_vs_n.png")
    print(" dp_runtime_vs_budget.png")
    print(" greedy_loss.png")
    print(" runtime_comparison.png")


if __name__ == "__main__":
    main()