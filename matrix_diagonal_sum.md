## Table of Contents
- [Table of Contents](#table-of-contents)
- [Problem Staement](#problem-staement)
- [Source Code](#source-code)
- [Time Complexity](#time-complexity)

## Problem Staement
https://leetcode.com/problems/matrix-diagonal-sum/

## Source Code
```
class Solution(object):
    def diagonalSum(self, mat):
        i = 0
        j = len(mat[0]) - 1
        sum = 0
        for r in mat:
            if(i != j):
                sum = sum + r[i] +  r[j]
            else:
                sum = sum + r[i]
            i = i + 1
            j = j - 1
        
        return sum
```
## Time Complexity
- Initilization: `𝑂(1)`
- Loop runs `n` times. Each iteration is  `𝑂(1)`.So, total time for the loop is `𝑂(n)`.
- To calculate the total time complexity:
    ```
    𝑂(1) + 𝑂(n)
    𝑂(n)
    So, total time complexty is: 𝑂(n)
   ```
        