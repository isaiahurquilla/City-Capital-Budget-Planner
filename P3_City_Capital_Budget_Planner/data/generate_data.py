"""
generate_data.py - make a capital-budget instance of any size for Project P3.

    python generate_data.py --n 60 --seed 3 --budget-share 0.4 --out projects_n060.json

Each candidate project has a cost (integer units of $10,000) and a community-benefit score
(population served x impact, in points). Costs are right-skewed (many small repairs, a few mega-projects).
The budget is a fraction of the total cost of all projects (default 40%), so not everything can be funded.
The same seed always gives the same file.
"""
import argparse
import json
import random

CATEGORIES = {
    # category: (benefit points per $10k on average, [name templates])
    "Roads":         (1.0, ["Resurface {s}", "Bike lane on {s}", "Signal upgrade at {s} & 5th"]),
    "Water":         (1.3, ["Replace water main under {s}", "Storm drain at {s}", "Filter upgrade, plant {k}"]),
    "Parks":         (0.8, ["Playground renovation, park {k}", "Trail extension, park {k}", "Splash pad, park {k}"]),
    "Schools":       (1.2, ["Roof replacement, school {k}", "Science lab, school {k}", "Safe crossing near school {k}"]),
    "Transit":       (1.1, ["Bus shelters, route {k}", "Electric-bus charging depot {k}", "Bus lane on {s}"]),
    "Public Safety": (1.5, ["Fire station {k} renovation", "Emergency radio upgrade, zone {k}", "Street lighting on {s}"]),
    "Libraries":     (0.7, ["Branch library {k} expansion", "Digital lab, branch {k}"]),
    "Energy":        (0.9, ["Solar canopy, civic site {k}", "LED retrofit, zone {k}"]),
}
STREETS = ["Elm St", "Oak Ave", "Lincoln Blvd", "Mill Rd", "Cedar Ln", "Harbor Dr", "Main St", "Bay St", "Pine Ave"]


def generate(n, seed, budget_share=0.4, mega=True, style="realistic"):
    """style 'realistic': benefit is roughly proportional to cost (greedy does well).
    style 'correlated': benefit = cost + 10 (the classic hard case: every project has almost the same
    benefit/cost ratio, so greedy wastes budget and the exact methods have to earn their keep)."""
    rng = random.Random(seed)
    cats = list(CATEGORIES)
    projects = []
    for i in range(n):
        cat = rng.choice(cats)
        factor, templates = CATEGORIES[cat]
        cost = int(min(900, max(4, rng.lognormvariate(3.6, 0.9))))          # median about 36 units = $360k
        if mega and rng.random() < 0.04:
            cost = int(cost * rng.uniform(4, 7))                              # a few very large projects
        ratio = factor * rng.uniform(0.55, 1.6)
        benefit = max(1, int(round(cost * ratio + rng.gauss(4, 3))))
        if style == "correlated":
            benefit = cost + 10
        name = rng.choice(templates).format(s=rng.choice(STREETS), k=rng.randint(1, 30))
        projects.append({"id": i, "name": name, "category": cat, "cost_10k": cost, "benefit": benefit})
    total = sum(p["cost_10k"] for p in projects)
    return {"budget_10k": max(1, int(total * budget_share)), "projects": projects}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, required=True)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--budget-share", type=float, default=0.4)
    ap.add_argument("--style", choices=["realistic", "correlated"], default="realistic")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    with open(a.out, "w", encoding="utf-8") as fh:
        json.dump(generate(a.n, a.seed, a.budget_share, style=a.style), fh, indent=1)
    print("wrote", a.out)


if __name__ == "__main__":
    main()
