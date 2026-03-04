# Rabbits and Recurrence Relations

## Problem Overview
This problem explores a modified Fibonacci sequence to model population growth. 
The key constraints are:
- Each pair reaches reproductive age after 1 month.
- Each reproductive pair produces a litter of **k** pairs each month.
- Rabbits never die in this model.

## Mathematical Model
The total number of pairs at month $n$ follows the recurrence relation:
$$F_n = F_{n-1} + (k \times F_{n-2})$$
Where:
- $F_n$: Total pairs in the current month.
- $F_{n-1}$: Pairs from the previous month (all survive).
- $k \times F_{n-2}$: New litters produced by pairs that were alive 2 months ago.

## Implementation
- **Algorithm:** Dynamic Programming (Iterative approach).
- **Efficiency:** $O(n)$ time complexity, ensuring fast calculations even for large $n$.