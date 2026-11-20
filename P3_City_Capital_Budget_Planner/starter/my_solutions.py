"""
my_solutions.py - starter file for Project P3: City Capital Budget Planner (0/1 knapsack)

Implement the TWO techniques assigned to you (the keys are listed in TECHNIQUES below). Delete or ignore the others.
Every function receives the loaded instance (a dict; its fields are described at the top of problem.py)
and must return: a list of project ids to fund, e.g. [0, 4, 7].

Test your work from this folder:
    python run_checks.py my_solutions.py --only <key>[,<key>]      e.g.  --only bf,dnc
Rules: write the algorithms under study yourself (see the project brief for which library helpers are allowed).
"""

def solve_bf(inst):
    """Brute force (all 2^n subsets).

    Return: a list of project ids to fund, e.g. [0, 4, 7].
    """
    raise NotImplementedError("write the bf technique here")


def solve_dnc(inst):
    """Divide-and-conquer (meet in the middle).

    Return: a list of project ids to fund, e.g. [0, 4, 7].
    """
    raise NotImplementedError("write the dnc technique here")


def solve_dp(inst):
    """Dynamic programming (0/1 knapsack table).

    Return: a list of project ids to fund, e.g. [0, 4, 7].
    """
    raise NotImplementedError("write the dp technique here")


def solve_greedy(inst):
    """Greedy (best benefit/cost ratio first).

    Return: a list of project ids to fund, e.g. [0, 4, 7].
    """
    raise NotImplementedError("write the greedy technique here")


TECHNIQUES = {
    "bf": solve_bf,
    "dnc": solve_dnc,
    "dp": solve_dp,
    "greedy": solve_greedy,
}
