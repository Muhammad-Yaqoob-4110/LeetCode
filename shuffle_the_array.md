## Table of Contents
- [Table of Contents](#table-of-contents)
- [Problem Staement](#problem-staement)
- [Source Code](#source-code)
- [Time Complexity](#time-complexity)

## Problem Staement
https://leetcode.com/problems/shuffle-the-array/

## Source Code
```
class Solution(object):
    def shuffle(self, nums, n):
        firstHalf = nums[:n]
        secondHalf = nums[n:]
        ans = []
        for i in range(n):
            ans.append(firstHalf[i])
            ans.append(secondHalf[i])
        return ans
```
## Time Complexity
- nums[:n] takes `𝑂(n)`
- nums[n:] also takes `𝑂(n)`
- Initilization of `ans` list: `𝑂(1)`
- Loop runs `n` times. Each iteration is  `𝑂(1)` + `𝑂(1)`. So, total time for the inner loop is `𝑂(n)`.
- Returning an list takes `𝑂(1)`
- To calculate the total time complexity:
    ```
    𝑂(n) + 𝑂(n) + 𝑂(1) + 𝑂(n) + 𝑂(1)
    𝑂(2n)
    So, total time complexty is: 𝑂(n)
   ```
        