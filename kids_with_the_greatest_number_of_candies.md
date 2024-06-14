## Table of Contents
- [Table of Contents](#table-of-contents)
- [Problem Staement](#problem-staement)
- [Source Code](#source-code)
- [Time Complexity](#time-complexity)

## Problem Staement
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

## Source Code
```
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        ans = []
        max_candies = sorted(candies, reverse=True)[0]
        
        for candie in candies:
            if(candie + extraCandies >= max_candies):
                ans.append(True)
            else:
                ans.append(False)
        return ans
```
## Time Complexity
- Initilization: `𝑂(1)`
- Sorting of list: `𝑂(nlogn)`
- nums[:n] takes `𝑂(n)`
- nums[n:] also takes `𝑂(n)`
- Initilization of `ans` list: `𝑂(1)`
- Loop runs `n` times. Each iteration is  `𝑂(1)` So, total time for the loop is `𝑂(n)`.
- Returning an list takes `𝑂(1)`
- To calculate the total time complexity:
    ```
    𝑂(1) + 𝑂(nlogn) + 𝑂(n)
    𝑂(nlogn)
    So, total time complexty is: 𝑂(nlogn)
   ```
        

        