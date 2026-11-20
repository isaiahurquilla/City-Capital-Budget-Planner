from pathlib import Path
import csv
import sys

from my_solutions import solve_greedy, solve_dp


DATA_FOLDER = Path(__file__).parent.parent / "data"
sys.path.append(str(DATA_FOLDER))

from generate_data import generate


def make_instance(raw):
    projects = raw["projects"]

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

    for style in ["realistic", "correlated"]:
        for n in [20, 40, 100, 200]:
            for seed in [1, 2, 3]:
                raw = generate(n, seed, style=style)
                inst = make_instance(raw)

                greedy_score = score(inst, solve_greedy(inst))
                dp_score = score(inst, solve_dp(inst))

                loss = ((dp_score - greedy_score) / dp_score) * 100

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

    with open("quality_seed_results.csv", "w", newline="") as file:
        writer = csv.writer(file)
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


if __name__ == "__main__":
    main()