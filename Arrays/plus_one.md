## Table of Contents
- [Table of Contents](#table-of-contents)
- [Problem Staement](#problem-staement)
- [Source Code](#source-code)
- [Time Complexity](#time-complexity)

## Problem Staement
https://leetcode.com/problems/plus-one/

## Source Code
```
class Solution(object):
    def plusOne(self, digits):
        ans = []
        digits_str = ""
        for digit in digits:
            digits_str  = digits_str + str(digit)

        plus_one_str = str(int(digits_str) + 1)

        for i in range(len(plus_one_str)):
            ans.append(int(plus_one_str[i]))
        
        return ans
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