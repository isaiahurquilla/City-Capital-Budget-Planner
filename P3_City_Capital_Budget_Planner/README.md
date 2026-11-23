# City Capital Budget Planner

## Student

Isaiah Urquilla

## Group B Responsibilities

Project P3: City Capital Budget Planner

This project was completed individually using the two Group B algorithms:

- Greedy benefit-per-cost
- Knapsack dynamic programming

## How to Run

Open a terminal in the `starter` folder.

Run the official checks for both algorithms:

```powershell
python run_checks.py my_solutions.py --only greedy,dp
```

Run individual checks and experiments:

```powershell
python run_checks.py my_solutions.py --only greedy
python run_checks.py my_solutions.py --only dp
python test_edge_cases.py
python benchmark.py
python quality_benchmark.py
python scaling_benchmark.py
python make_plots.py
python quality_plot.py
```

## Data Sources

The `data` folder contains the JSON datasets supplied with the project. Each file contains a budget and a list of project IDs, costs, and benefits.

Additional reproducible datasets were created by the benchmark programs using fixed sizes and seeds. Using the same seeds allows the datasets and results to be generated again.

Small, medium, and large inputs were tested, ranging from 12 to 2,000 projects. Runtime experiments were repeated five times, and the median runtime was reported. No runs timed out.

## Help Received

The project brief, supplied starter code, tests, and datasets were used to complete the project. AI was used to help explain requirements, and revise report wording. I wrote, ran, and verified the algorithms and results.

## Recommendation Comparing Both Algorithms

Dynamic programming is the best choice when the city needs a guaranteed optimal funding plan. It found the optimal benefit on every tested dataset. However, its runtime and memory use increased as the number of projects and budget increased.

Greedy benefit-per-cost is the better choice when a result is needed quickly or the dataset is too large for dynamic programming. It was much faster and usually produced a result close to the optimum, but it was not always exact.

I recommend dynamic programming when accuracy is the main concern and the dataset fits within the available time and memory. I recommend greedy when speed is more important or when a quick estimate is acceptable.

## Verification Log

This project was completed individually, so partner cross-validation was not applicable.

Check: Result 
Official test harness: 20 passed, 0 failed 
Four edge-case tests: All passed 
Greedy solution validity: All returned solutions stayed within budget
Dynamic programming correctness: Matched every reference optimum
Small, medium, and large benchmarks: Completed successfully