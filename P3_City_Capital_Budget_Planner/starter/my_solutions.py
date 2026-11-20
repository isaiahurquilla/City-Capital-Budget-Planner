"""
my_solutions.py - starter file for Project P3: City Capital Budget Planner (0/1 knapsack)

Implement the TWO techniques assigned to you (the keys are listed in TECHNIQUES below). Delete or ignore the others.
Every function receives the loaded instance (a dict; its fields are described at the top of problem.py)
and must return: a list of project ids to fund, e.g. [0, 4, 7].

Test your work from this folder:
    python run_checks.py my_solutions.py --only <key>[,<key>]      e.g.  --only bf,dnc
Rules: write the algorithms under study yourself (see the project brief for which library helpers are allowed).
"""


def solve_dp(inst):
    """Dynamic programming (0/1 knapsack table).

    Return: a list of project ids to fund, e.g. [0, 4, 7].
    """
    raise NotImplementedError("write the dp technique here")


def solve_greedy(inst):
    project_ids = list(range(inst["n"]))
    # Calculate benefit/cost ratios for each project

    project_ids.sort(
        key=lambda i: inst["benefit"][i] / inst["cost"][i], reverse=True
    )

    selected = []
    remaining_budget = inst["budget"]

    for i in project_ids:
        if inst["cost"][i] <= remaining_budget:
            selected.append(i)
            remaining_budget -= inst["cost"][i]

    return selected
    """Greedy (best benefit/cost ratio first).

    Return: a list of project ids to fund, e.g. [0, 4, 7].
    """
    


TECHNIQUES = {
    "dp": solve_dp,
    "greedy": solve_greedy,
}
