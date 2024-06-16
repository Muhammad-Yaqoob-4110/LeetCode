## Table of Contents
- [Table of Contents](#table-of-contents)
- [Problem Staement](#problem-staement)
- [Source Code](#source-code)
- [Time Complexity](#time-complexity)

## Problem Staement
https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

## Source Code
```
class Solution(object):
    def findNumbers(self, nums):
        even = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                even = even + 1

        return even
```
## Time Complexity
- Initilization: `𝑂(1)`
- Loop runs `n` times. Each iteration is  `𝑂(d)`. Where d is the number of digits in a number.in the worst case, 
𝑑 can be approximated as `𝑂(logk)` So, total time for the loop is `𝑂(n x logk)`.
- Sorting:  `𝑂((n + 1)log(n + 1))`
- To calculate the total time complexity:
    ```
    𝑂(1) + 𝑂(n x logk)
    𝑂(n x logk)
    So, total time complexty is: 𝑂(nlogk)
   ```
    
