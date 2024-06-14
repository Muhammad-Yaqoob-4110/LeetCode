## Table of Contents
- [Table of Contents](#table-of-contents)
- [Problem Staement](#problem-staement)
- [Source Code](#source-code)
- [Time Complexity](#time-complexity)

## Problem Staement
https://leetcode.com/problems/number-of-good-pairs/

## Source Code
```
class Solution(object):
    def numIdenticalPairs(self, nums):
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i] == nums[j]):
                    count = count + 1
        return count
```
## Time Complexity
- Initilization: `𝑂(1)`
- Outer loop runs `n` times. So, total time for the outer loop is `𝑂(n)`.
- Inner loop runs  `(n-1)/2`. Each iteration is  `𝑂(1)`. So, total time for the loop is `𝑂((n -1)/2)`.
- Returning a variable takes `𝑂(1)`
- To calculate the total time complexity:
    ```
    𝑂(1) + 𝑂(n) * 𝑂((n -1)/2)
    𝑂(n(n - 1)/2)
    So, total time complexty is: 𝑂(n^2)
   ```
        

        


        