"""
P3 - City Capital Budget Planner (0/1 knapsack)
Instance loader, solution validator and technique registry used by run_checks.py.

Instance (dict returned by load_instance):
    budget     total budget in units of $10,000
    n          number of candidate projects
    cost       cost[i]     integer, units of $10,000
    benefit    benefit[i]  integer community-benefit points
    projects   list of dicts (id, name, category, cost_10k, benefit)   - descriptive

Solution format (what every technique returns):
    a list of project ids to fund (each id at most once) with total cost <= budget.
    Score = total benefit of the funded projects (bigger is better).
"""
import json

SENSE = "max"
TECHNIQUES = {
    "bf":     {"name": "Brute force (all 2^n subsets)", "exact": True},
    "dnc":    {"name": "Divide-and-conquer (meet in the middle)", "exact": True},
    "dp":     {"name": "Dynamic programming (0/1 knapsack table)", "exact": True},
    "greedy": {"name": "Greedy (best benefit/cost ratio first)", "exact": False},
}


def load_instance(path, params=None):
    with open(path, encoding="utf-8") as fh:
        raw = json.load(fh)
    projs = raw["projects"]
    return {"budget": raw["budget_10k"], "n": len(projs),
            "cost": [p["cost_10k"] for p in projs], "benefit": [p["benefit"] for p in projs],
            "projects": projs}


def validate(inst, sol, params=None):
    try:
        ids = [int(i) for i in sol]
    except (TypeError, ValueError):
        return False, None, "solution must be a list of project ids"
    if len(set(ids)) != len(ids):
        return False, None, "a project is listed twice"
    if any(i < 0 or i >= inst["n"] for i in ids):
        return False, None, "unknown project id"
    cost = sum(inst["cost"][i] for i in ids)
    if cost > inst["budget"]:
        return False, None, f"total cost {cost} exceeds budget {inst['budget']}"
    return True, sum(inst["benefit"][i] for i in ids), ""
