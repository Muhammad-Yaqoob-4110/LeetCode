## Table of Contents
- [Table of Contents](#table-of-contents)
- [Problem Staement](#problem-staement)
- [Source Code](#source-code)
- [Time Complexity 𝑂(n)](#time-complexity-𝑂n)

## Problem Staement
https://leetcode.com/problems/build-array-from-permutation/

## Source Code
```
  class Solution(object):

    def buildArray(self, nums):
        ans = []
        for num in range(len(nums)):
            ans.append(nums[nums[num]])
        
        return ans
```
## Time Complexity 𝑂(n)
- Initialization of `ans` list takes constant time, `𝑂(1)`
- **Loop Iteration**: Loop runs from `num = 0` to `num = len(nums) - 1`, which means it iterates `n` times, `𝑂(n)`.

- `nums[num]` is an element access in the list `nums`, which is an `𝑂(1) operation`.
  
- `nums[nums[num]]` is another element access in the list `nums`, which is also an `𝑂(1) operation`.
  
- `ans.append(...)` is an append operation to the list `ans`, which on average takes `𝑂(1)` amortized time.
- So, the total work done by the loop is `𝑂(1) × 𝑛 = 𝑂(𝑛)`

- The total time complexity of the code is:`𝑂(𝑛)`