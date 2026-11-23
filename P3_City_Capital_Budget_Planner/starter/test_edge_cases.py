from my_solutions import solve_greedy, solve_dp

def totals(inst, selected):
    cost = sum(inst["cost"][i] for i in selected)
    benefit = sum(inst["benefit"][i] for i in selected)
    return cost, benefit

# Add new tests using this format:
# (test name, instance, expected greedy benefit, expected DP benefit)
tests = [
    ("No projects", {"n": 0, "budget": 10, "cost": [], "benefit": []},0,0),
    ("Zero budget", {"n": 2, "budget": 0, "cost": [2, 3], "benefit": [10, 20]},0,0),
    ("No projects fit", {"n": 2, "budget": 3, "cost": [4,5], "benefit": [20,30]},0,0),
    ("Greedy misses the optimum", {"n": 3, "budget": 50, "cost": [10,20,30], "benefit": [60,100,120]},160,220)
]

for name, inst, expected_greedy, expected_dp in tests:
    greedy_selection = solve_greedy(inst)
    dp_selection = solve_dp(inst)

    greedy_cost, greedy_benefit = totals(inst, greedy_selection)
    dp_cost, dp_benefit = totals(inst, dp_selection)

    print(name)
    print(" Greedy:", greedy_selection, greedy_cost, greedy_benefit)
    print(" DP:", dp_selection, dp_cost, dp_benefit)

    # These assertions check that both returned selections obey the budget.
    assert greedy_cost <= inst["budget"]
    assert dp_cost <= inst["budget"]
    # Update the expected values in the test tuple if a test instance changes.
    assert greedy_benefit == expected_greedy
    assert dp_benefit == expected_dp

print("All edge-case tests passed.")