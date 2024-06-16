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
    def smallerNumbersThanCurrent(self, nums):
        ans = []
        for num in nums:
            count = 0
            for num2 in nums:
                if(num2 < num):
                    count = count + 1
            ans.append(count)
        
        return ans
```
## Time Complexity
- Initilization: `𝑂(1)`
- Outer loop runs `n` times. So, total time for the outer loop is `𝑂(n)`.
- Inner loop also runs  `n` times. Each iteration is  `𝑂(1)`. So, total time for the loop is `𝑂(n)`.
- Returning a variable takes `𝑂(1)`
- To calculate the total time complexity:
    ```
    𝑂(1) + 𝑂(n) * 𝑂(n)
    𝑂(n^2)
    So, total time complexty is: 𝑂(n^2)
   ```
    
