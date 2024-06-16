## Table of Contents
- [Table of Contents](#table-of-contents)
- [Problem Staement](#problem-staement)
- [Source Code](#source-code)
- [Time Complexity](#time-complexity)

## Problem Staement
https://leetcode.com/problems/check-if-the-sentence-is-pangram/

## Source Code
```
class Solution(object):
    def checkIfPangram(self, sentence):
        dict = {}
        for char in sentence:
            if dict.get(char) == None:
                dict[char] = 1
            else:
                dict[char] = dict.get(char) + 1
        
        if(len(dict) == 26):
            return True
        return False
```
## Time Complexity
- Dictionary Initilization: `𝑂(1)`
- Loop runs `n` times. Each iteration is  `𝑂(1)`. So, total time for the loop is `𝑂(n)`.
- Checking of length of dictionary: `𝑂(1)`
- To calculate the total time complexity:
    ```
    𝑂(1) + 𝑂(n) + 𝑂(1)
    𝑂(n)
    So, total time complexty is: 𝑂(n)
   ```