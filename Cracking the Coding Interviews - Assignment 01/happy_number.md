## Table of Contents
- [Table of Contents](#table-of-contents)
- [Problem Staement](#problem-staement)
- [Source Code](#source-code)
- [Time Complexity](#time-complexity)

## Problem Staement
https://leetcode.com/problems/happy-number/

## Source Code
```
class Solution(object):
    def isHappy(self, n):
        m = 0
        non_repeated = set()
        while True:
            for num in str(n):
                m += int(num) ** 2
            if m in non_repeated:
                return False
            non_repeated.add(m)
            n = m
            if m == 1:
                return True
            m = 0
```
## Time Complexity
- Each iteration of the `while` loop involves:
- for loop which runs `𝑂(log n)` time.
- InitializatChecking and updating the set: `𝑂(1)`
- Updating variables: `𝑂(1)`

- To calculate the total time complexity:
    ```
    So, total time complexty is: 𝑂(log n)
   ```