## Table of Contents
- [Table of Contents](#table-of-contents)
- [Problem Staement](#problem-staement)
- [Source Code](#source-code)
- [Time Complexity](#time-complexity)

## Problem Staement
https://leetcode.com/problems/add-to-array-form-of-integer/

## Source Code
```
class Solution(object):
    def addToArrayForm(self, num, k):
        string = ""
        for n in num:
            string = string + str(n)
        
        output = []
        for num in str(int(string) + k):
            output.append(int(num))
        
        return output
```
## Time Complexity
- Initialization: `𝑂(1)`
- Loop runs `n` times. Each iteration has concatenation, Concatenation takes `𝑂(n)`. So, total time complexity for the loop is `𝑂(n^2)`
- 2nd loop runs `𝑂(n)`
- To calculate the total time complexity:
    ```
    𝑂(n) + 𝑂(n^2) + 𝑂(n)
    𝑂(n^2)
    So, total time complexty is: 𝑂(n^2)
   ```
        