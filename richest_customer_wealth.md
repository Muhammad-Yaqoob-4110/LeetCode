## Table of Contents
- [Table of Contents](#table-of-contents)
- [Problem Staement](#problem-staement)
- [Source Code](#source-code)
- [Time Complexity](#time-complexity)

## Problem Staement
https://leetcode.com/problems/richest-customer-wealth/

## Source Code
```
class Solution(object):
    def maximumWealth(self, accounts):
        wealth = []
        for account in accounts:
            balanceSum = 0
            for balance in account:
                balanceSum = balanceSum + balance
            wealth.append(balanceSum)
        
        sortedWealth = sorted(wealth,reverse=True)
        return sortedWealth[0]
```
## Time Complexity
- Initialization: `𝑂(1)`
- Outer Loop Runs `𝑚` times.
- Inner loop runs `n` times. Each iteration is  `𝑂(1)`. So, total time for the inner loop is `𝑂(n)`.
- Total time for the loops is `𝑂(m x n)`
- Sorting takes `𝑂(nlogn)`
- To calculate the total time complexity:
    ```
    𝑂(1) + 𝑂(m x n) + 𝑂(nlogn)
    𝑂(m x n + nlogn)
    So, total time complexty is: 𝑂(m x n + nlogn)
   ```

        