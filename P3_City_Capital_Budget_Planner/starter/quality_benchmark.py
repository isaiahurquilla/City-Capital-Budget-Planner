from pathlib import Path
import csv
import sys

from my_solutions import solve_greedy, solve_dp

# This path works while the script remains inside the starter folder.
DATA_FOLDER = Path(__file__).parent.parent / "data"
# Add the data folder so generate_data.py can be imported.
sys.path.append(str(DATA_FOLDER))

from generate_data import generate #type: ignore


def make_instance(raw):
    projects = raw["projects"]

    # Convert the generator's format into the format expected
    # by solve_greedy() and solve_dp().
    return {
        "n": len(projects),
        "budget": raw["budget_10k"],
        "cost": [p["cost_10k"] for p in projects],
        "benefit": [p["benefit"] for p in projects]
    }


def score(inst, selected):
    return sum(inst["benefit"][i] for i in selected)


def main():
    results = []

    # Add another generator style here if generate_data.py supports it.
    for style in ["realistic", "correlated"]:
        # Change this list to test different project counts.
        for n in [20, 40, 100, 200]:
            for seed in [1, 2, 3]:
                # Fixed seeds make the generated datasets reproducible.
                # Add more seeds for a larger sample.
                raw = generate(n, seed, style=style)
                inst = make_instance(raw)

                greedy_score = score(inst, solve_greedy(inst))
                dp_score = score(inst, solve_dp(inst))

                # Generated instances have positive benefits.
                # Add a dp_score == 0 check if empty instances are introduced.
                loss = ((dp_score - greedy_score) / dp_score) * 100

                # Keep this order consistent with the CSV header below.
                results.append([
                    style,
                    n,
                    seed,
                    greedy_score,
                    dp_score,
                    loss
                ])

                print(
                    style,
                    "n =", n,
                    "seed =", seed,
                    "greedy =", greedy_score,
                    "dp =", dp_score,
                    "loss =", f"{loss:.2f}%"
                )

    # This replaces the previous results file each time the script runs.
    with open("quality_seed_results.csv", "w", newline="") as file:
        writer = csv.writer(file)
        # Keep these columns in the same order as results.append().
        writer.writerow([
            "style",
            "n",
            "seed",
            "greedy_score",
            "dp_score",
            "loss_percent"
        ])
        writer.writerows(results)

    print("\nResults saved to quality_seed_results.csv")

# Prevent the benchmark from running when this file is imported.
if __name__ == "__main__":
    main()