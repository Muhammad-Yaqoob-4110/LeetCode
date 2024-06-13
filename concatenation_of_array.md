## Table of Contents
- [Table of Contents](#table-of-contents)
- [Problem Staement](#problem-staement)
- [Source Code](#source-code)
- [Time Complexity 𝑂(n)](#time-complexity-𝑂n)

## Problem Staement
https://leetcode.com/problems/concatenation-of-array/

## Source Code
```
class Solution(object):
    def getConcatenation(self, nums):
        ans = []
        for i in range(len(nums)):
            ans.append(nums[i])
        
        for i in range(len(nums)):
            ans.append(nums[i])
        
        return ans
```
## Time Complexity 𝑂(n)
- Initialization: `𝑂(1)`
- First Loop iterates `n` times. Each iteration is  `𝑂(n)`. So, total time for 1st loop is `𝑂(n)`.

- Second loop also runs `n` times, `𝑂(n)`. Each iteration is  `𝑂(n)`. So, total time for 1st loop is `𝑂(n)`.
  
- To calculate the total time complexity:
    ```
    𝑂(1) + 𝑂(n) + 𝑂(n)
    𝑂(n) + 𝑂(n) = 𝑂(2n)
    So, total time complexty is: 𝑂(n)
   ```

