## Table of Contents
- [Table of Contents](#table-of-contents)
- [Problem Staement](#problem-staement)
- [Source Code](#source-code)
- [Time Complexity](#time-complexity)

## Problem Staement
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

## Source Code
```
class Solution(object):
    def removeDuplicates(self, nums):
        unique_elements_set = set(nums)
        unique_elements_list = sorted(list(unique_elements_set))
        for i in range(len(unique_elements_list)):
            nums[i] = unique_elements_list[i]
        
        return len(unique_elements_list)
```
## Time Complexity
- Creating a set from the list: `𝑂(n)`
- Converting the set to a sorted list:  `𝑂(n) + 𝑂(mlogm)`
- Loop runs `n` times. Each iteration takes `𝑂(1)`. So, total time complexity for the loop is `𝑂(m)`
- To calculate the total time complexity:
    ```
    𝑂(n) + 𝑂(n) + 𝑂(mlogm) + 𝑂(m)
    In the worst case, where all elements are unique, 𝑚 = 𝑛
    𝑂(n) + 𝑂(n) + 𝑂(nlogn) + 𝑂(n)
    So, total time complexty is: 𝑂(nlogn)
   ```