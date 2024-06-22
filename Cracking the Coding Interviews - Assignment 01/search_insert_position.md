## Table of Contents
- [Table of Contents](#table-of-contents)
- [Problem Staement](#problem-staement)
- [Source Code](#source-code)
- [Time Complexity](#time-complexity)

## Problem Staement
https://leetcode.com/problems/search-insert-position/

## Source Code
```
class Solution(object):
    def searchInsert(self, nums, target):
        start_idx = 0
        end_idx = len(nums) - 1
        while start_idx <= end_idx:
            mid_idx = (start_idx + end_idx) // 2
            if(nums[mid_idx] == target):
                return mid_idx
            elif target > nums[mid_idx]:
                start_idx = mid_idx + 1
            elif target < nums[mid_idx]:
                end_idx = mid_idx - 1
        
        return start_idx
```
## Time Complexity
- Initialization: `𝑂(1)`
- Loop performs a binary search which takes `𝑂(log n)`.
- To calculate the total time complexity:
    ```
    𝑂(1) + 𝑂(log n)
    𝑂(log n)
    So, total time complexty is: 𝑂(log n)
   ```