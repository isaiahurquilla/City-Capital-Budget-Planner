import csv
from statistics import mean
import matplotlib.pyplot as plt


def main():
    with open("quality_seed_results.csv", newline="") as file:
        rows = list(csv.DictReader(file))

    sizes = [20, 40, 100, 200]
    realistic_averages = []
    correlated_averages = []

    for n in sizes:
        realistic_losses = [
            float(row["loss_percent"])
            for row in rows
            if row["style"] == "realistic"
            and int(row["n"]) == n
        ]

        correlated_losses = [
            float(row["loss_percent"])
            for row in rows
            if row["style"] == "correlated"
            and int(row["n"]) == n
        ]

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
    plt.xticks(sizes)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("greedy_gap_by_style.png")

    print("Created greedy_gap_by_style.png")


if __name__ == "__main__":
    main()