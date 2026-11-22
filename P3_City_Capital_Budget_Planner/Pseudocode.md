# GREEDY ALGORITHM

## INPUT 

- Number of projects 'n'
- Budget 'B'
- Cost of each project
- Benefit of each project

## OUTPUT

- List of selected project IDs

## EXAMPLE

For 'projects_n012.json', the budget is '232'.

Projects sorted by benefit-to-cost ratio:

'9, 8, 1, 6, 3, 7, 0, 11, 2, 4, 10, 5'

Greedy decisions:

- Take 9: budget left = 223
- Take 8: budget left = 200
- Take 1: budget left = 194
- Take 6: budget left = 141
- Take 3: budget left = 69
- Take 7: budget left = 38
- Skip 0 because its cost is 43
- Take 11: budget left = 1
- Skip the remaining projects because they do not fit

Selected projects:

'[9, 8, 1, 6, 3, 7, 11]'

Total cost:

'9 + 23 + 6 + 53 + 72 + 31 + 37 = 231'

Total benefit:

'25 + 39 + 10 + 85 + 115 + 41 + 40 = 355'

## EXAMPLE WHERE GREEDY IS NOT OPTIMAL

Budget: 50

| Project | Cost | Benefit | Benefit/Cost |
|---|---:|---:|---:|
| 0 | 10 | 60 | 6 |
| 1 | 20 | 100 | 5 |
| 2 | 30 | 120 | 4 |

Greedy sorts the projects in the order 0, 1, 2.

- Take project 0: remaining budget = 40
- Take project 1: remaining budget = 20
- Skip project 2 because its cost is 30

Greedy selects projects `[0, 1]`.

- Total cost = 30
- Total benefit = 160

Dynamic programming selects projects `[1, 2]`.

- Total cost = 50
- Total benefit = 220

This example shows that selecting projects by the highest benefit-to-cost ratio does not always produce the optimal result.

## PSEUDOCODE

```

GREEDY-PROJECTS(projects, B)

    Sort project IDs from highest to lowest by:
        benefit[i] / cost[i]

    selected = empty list
    remaining_budget = B

    for each project i in sorted order:
        if cost[i] <= remaining_budget:
            add i to selected
            remaining_budget = remaining_budget - cost[i]

    return selected 
 ```

The algorithm skips projects that do not fit and continues checking the rest.

# DYNAMIC PROGRAMMING ALGORITHM

## INPUT 
    
- Number of projects 'n'
- Budget 'B'
- Cost of each project
- Benefit of each project

## OUTPUT

- List of selected project IDs that produce the maximum benefit without exceeding the budget

## EXAMPLE

For 'projects_n012.json', the budget is '232'.

During traceback, the algorithm makes these decisions:

- Skip project 11
- Skip project 10
- Take project 9
- Take project 8
- Take project 7
- Take project 6
- Skip project 5
- Skip project 4
- Take project 3
- Skip project 2
- Skip project 1
- Take project 0

Selected projects:

[0, 3, 6, 7, 8, 9]

Total cost:

43 + 72 + 53 + 31 + 23 + 9 = 231

Total benefit:

54 + 115 + 85 + 41 + 39 + 25 = 359

Dynamic programming finds a benefit of 359, which is 4 points higher than the greedy result.

### DP Definition

`F(i, w)` is the maximum benefit possible using the first `i` projects with budget `w`.

Base cases:

- `F(0, w) = 0`
- `F(i, 0) = 0`

Recurrence:

`F(i, w) = max(F(i - 1, w), F(i - 1, w - cost[i]) + benefit[i])`

If `cost[i] > w`, then `F(i, w) = F(i - 1, w)` because project `i` cannot fit within the current budget.


## PSEUDOCODE
```

DYNAMIC-PROGRAMMING(projects, B)

        best[0 through B] = 0
        take = empty list

        for each project i:
            decisions[0 through B] = false

            for w from B down to cost[i]:
                new_benefit =
                    best[w - cost[i]] + benefit[i]

                if new_benefit > best[w]:
                    best[w] = new_benefit
                    decisions[w] = true

            add decisions to take

        selected = empty list
        w = B

        for i from n - 1 down to 0:
            if take[i][w] is true:
                add i to selected
                w = w - cost[i]

        reverse selected
        return selected
```

The budget loop moves from right to left so the same project cannot be selected more than once.


