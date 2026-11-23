"""
my_solutions.py - starter file for Project P3: City Capital Budget Planner (0/1 knapsack)

Implement the TWO techniques assigned to you (the keys are listed in TECHNIQUES below). Delete or ignore the others.
Every function receives the loaded instance (a dict; its fields are described at the top of problem.py)
and must return: a list of project ids to fund, e.g. [0, 4, 7].

Test your work from this folder:Greedy algorithm testing:
    python run_checks.py my_solutions.py --only <key>[,<key>]      e.g.  --only bf,dnc
Rules: write the algorithms under study yourself (see the project brief for which library helpers are allowed).
"""


def solve_dp(inst):
    n = inst["n"]
    budget = inst["budget"] 

    # best[amount] stores the highest benefit found with a budget limit of amount.
    best = [0] * (budget + 1)
    # Stores decisions for traceback; removing this saves memory but would prevent returning the selected project IDs.
    take = []

    # Process every project once.
    for i in range(n):
        cost = inst["cost"][i]
        benefit = inst["benefit"][i] 
        # bytearray uses about one byte per decision and less memory than a normal Python list.
        decisions = bytearray(budget+1)
        # Keep this loop moving backward. Moving forward would allow the same project to be selected more than once.
        for amount in range(budget, cost - 1, -1):
            new_benefit = best[amount - cost] + benefit
            # Using > keeps the previous selection when benefits are tied.
            if new_benefit > best[amount]:
                best[amount] = new_benefit
                decisions[amount] = 1

        take.append(decisions)

    selected = []
    amount = budget

    # Trace backward through the saved decisions to recover project IDs.
    for i in range(n-1, -1, -1):
        if take[i][amount]:
            selected.append(i)
            amount -= inst["cost"][i]
    selected.reverse()
    return selected


def solve_greedy(inst):
    project_ids = list(range(inst["n"]))
    # Calculate benefit/cost ratios for each project

    # Change this key only if testing a different greedy selection rule.
    # The current rule ranks projects by benefit received per unit of cost.
    project_ids.sort(
        key=lambda i: inst["benefit"][i] / inst["cost"][i], reverse=True
    )

    selected = []
    remaining_budget = inst["budget"]

    for i in project_ids:
        if inst["cost"][i] <= remaining_budget:
            selected.append(i)
            remaining_budget -= inst["cost"][i]
        # Continue after a project does not fit because a later,
        # less expensive project may still fit.    

    return selected
    

# run_checks.py uses these exact keys to find the solution functions
TECHNIQUES = {
    "dp": solve_dp,
    "greedy": solve_greedy,
}
