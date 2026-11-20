Project P3 - City Capital Budget Planner (0/1 knapsack)
DATA FOLDER
============================================================

These datasets are SYNTHETIC: produced by generate_data.py from a fixed random seed so that every student gets identical files,
with distributions modelled on the real-world situation described in the project brief.

FORMAT
projects_nXXX[_corr].json : {'budget_10k': B, 'projects': [{id, name, category, cost_10k, benefit}]}
Costs and the budget are integers in units of $10,000. '_corr' files are strongly correlated instances (benefit = cost + 10),
the hard case for the greedy rule.

REFERENCE VALUES
'reference.score' is the proven optimal total benefit. 'greedy_ratio_rule' is what best-ratio-first achieves.

MORE DATA
    python generate_data.py --help      (any size, any seed; the same seed always gives the same file)

FILES (from manifest.json)
    file                               label       size  suitable techniques                reference
    projects_n012.json                 small         12  bf,dnc,dp,greedy                   optimal = 359
    projects_n020.json                 small         20  bf,dnc,dp,greedy                   optimal = 578
    projects_n032.json                 medium        32  dnc,dp,greedy                      optimal = 1145
    projects_n040.json                 medium        40  dnc,dp,greedy                      optimal = 1349
    projects_n040_corr.json            medium        40  dnc,dp,greedy                      optimal = 1088
    projects_n100.json                 large        100  dp,greedy                          optimal = 3531
    projects_n100_corr.json            large        100  dp,greedy                          optimal = 2791
    projects_n1000.json                large       1000  dp,greedy                          optimal = 36320
    projects_n1000_corr.json           large       1000  dp,greedy                          optimal = 29135
    projects_n2000.json                stress      2000  dp,greedy                          optimal = 72614

Labels: small = hand-checkable / every technique; medium = exponential techniques still feasible; large = only the efficient techniques; stress = slow even for them (use for the top of your scaling curve).
A technique listed as 'suitable' for a file is expected to finish in under about a minute in CPython; a technique NOT listed is expected to be too slow (that is part of what you will measure).
