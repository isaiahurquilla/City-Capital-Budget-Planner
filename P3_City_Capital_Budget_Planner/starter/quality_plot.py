import csv
from statistics import mean
import matplotlib.pyplot as plt


def main():
    # quality_seed_results.csv must exist before this script runs.
    with open("quality_seed_results.csv", newline="") as file:
        rows = list(csv.DictReader(file))

    # Keep this list consistent with the sizes tested
    # in quality_benchmark.py.
    sizes = [20, 40, 100, 200]
    realistic_averages = []
    correlated_averages = []

     # Select the realistic results for the current project count.
    for n in sizes:
        realistic_losses = [
            float(row["loss_percent"])
            for row in rows
            if row["style"] == "realistic"
            and int(row["n"]) == n
        ]

        # Select the correlated results for the current project count.
        correlated_losses = [
            float(row["loss_percent"])
            for row in rows
            if row["style"] == "correlated"
            and int(row["n"]) == n
        ]

        # Each average currently uses the three fixed seeds tested
        # in quality_benchmark.py.
        realistic_averages.append(mean(realistic_losses))
        correlated_averages.append(mean(correlated_losses))

    plt.figure(figsize=(8, 5))

    plt.plot(
        sizes,
        realistic_averages,
        marker="o",
        label="Realistic"
    )

    plt.plot(
        sizes,
        correlated_averages,
        marker="o",
        label="Correlated"
    )

    plt.title("Average Greedy Loss Across Three Seeds")
    plt.xlabel("Number of projects (n)")
    plt.ylabel("Average benefit loss (%)")
    # Keep the x-axis labels limited to the exact tested sizes.
    plt.xticks(sizes)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    # Running the script again replaces the previous image.
    plt.savefig("greedy_gap_by_style.png")

    print("Created greedy_gap_by_style.png")

# Prevent the graph from being created when this file is imported.
if __name__ == "__main__":
    main()