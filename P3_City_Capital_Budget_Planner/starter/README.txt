Project P3 - City Capital Budget Planner (0/1 knapsack)
STARTER FOLDER
============================================================

problem.py       Loads a data file into a Python dict (inst), checks an answer (validate) and lists the technique keys.
                 READ ITS DOCSTRING FIRST: it defines the instance fields and the exact format every technique must return.
my_solutions.py  Template. Fill in your two techniques; keep the TECHNIQUES dictionary at the bottom.
run_checks.py    Test harness. It runs your functions on the files listed in ../data/manifest.json, validates every answer
                 and compares it with the reference value.

Quick start (Python 3.10+, standard library only):
    python run_checks.py my_solutions.py --only bf,dnc --labels small

Technique keys for this project:
    bf          Brute force (all 2^n subsets)  [exact]
    dnc         Divide-and-conquer (meet in the middle)  [exact]
    dp          Dynamic programming (0/1 knapsack table)  [exact]
    greedy      Greedy (best benefit/cost ratio first)  [heuristic]

The harness is for CORRECTNESS. For the timing / operation-count experiments in your report, write your own benchmark script
(time.perf_counter, repeated runs, growing n) - the project brief and the master document explain the protocol.
