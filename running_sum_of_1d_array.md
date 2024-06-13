## Table of Contents
- [Table of Contents](#table-of-contents)
- [Problem Staement](#problem-staement)
- [Source Code](#source-code)
- [Time Complexity 𝑂(n)](#time-complexity-𝑂n)

## Problem Staement
https://leetcode.com/problems/running-sum-of-1d-array/

## Source Code
```
class Solution(object):
    def runningSum(self, nums):
        ans = []
        sum = 0
        for i in range(len(nums)):
            sum = sum + nums[i]
            ans.append(sum)
        
        return ans
```
## Time Complexity 𝑂(n)
- Initialization: `𝑂(1)`
- Initialization: `𝑂(1)`
- Loop iterates `n` times. Each iteration is  `𝑂(1)`. So, total time for the loop is `𝑂(n)`.
  
- To calculate the total time complexity:
    ```
    𝑂(1) + 𝑂(1) + 𝑂(n) x 𝑂(1)
    𝑂(2) + 𝑂(n)
    So, total time complexty is: 𝑂(n)
   ```




        