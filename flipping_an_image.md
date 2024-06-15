## Table of Contents
- [Table of Contents](#table-of-contents)
- [Problem Staement](#problem-staement)
- [Source Code](#source-code)
- [Time Complexity](#time-complexity)

## Problem Staement
https://leetcode.com/problems/flipping-an-image/

## Source Code
```
class Solution(object):
    def flipAndInvertImage(self, image):
        output = []
        for row in image:
            temp = []
            for i in range(len(row) - 1, -1, -1):
                if(row[i] == 0):
                    temp.append(1)
                else:
                    temp.append(0)
            output.append(temp)
            
        return output
```
## Time Complexity
- Initilization: `𝑂(1)`
- Outer loop runs `n` times. So, total time for the outer loop is `𝑂(n)`.
- Inner loop runs  `m`. Each iteration is  `𝑂(1)`. So, total time for the loop is `𝑂(m)`.
- Returning takes `𝑂(1)`
- To calculate the total time complexity:
    ```
    𝑂(1) + 𝑂(n) * 𝑂(m) + 𝑂(1)
    𝑂(n x m)
    So, total time complexty is: 𝑂(n x m)
   ```
        