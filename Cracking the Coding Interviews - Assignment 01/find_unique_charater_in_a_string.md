## Table of Contents
- [Table of Contents](#table-of-contents)
- [Problem Staement](#problem-staement)
- [Source Code](#source-code)
- [Time Complexity](#time-complexity)

## Problem Staement
https://leetcode.com/problems/first-unique-character-in-a-string/

## Source Code
```
class Solution(object):
    def firstUniqChar(self, s):
        dict = OrderedDict()
        for index, char in enumerate(s):
            if char in dict:
                dict[char][0] += 1
            else:
                dict[char] = [1, index]

        for char, (cnt, idx) in dict.items():
            if cnt == 1:
                return idx
        return -1
```
## Time Complexity
- Initialization: `𝑂(1)`
- Loop runs `n` times. Each iteration is  `𝑂(1)`. So, total time for the inner loop is `𝑂(n)`.
- 2nd loop runs `n` times. Each iteration is  `𝑂(1)`. So, total time for the inner loop is `𝑂(n)`.
- To calculate the total time complexity:
    ```
    𝑂(1) + 𝑂(n) + 𝑂(n)
    𝑂(2n)
    So, total time complexty is: 𝑂(n)
   ```