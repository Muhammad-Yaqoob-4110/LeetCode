## Table of Contents
- [Table of Contents](#table-of-contents)
- [Problem Staement](#problem-staement)
- [Source Code](#source-code)
- [Time Complexity](#time-complexity)

## Problem Staement
https://leetcode.com/problems/valid-anagram/s

## Source Code
```
class Solution(object):
    def isAnagram(self, s, t):
        # Initialize a count array for 26 letters
        count = [0] * 26

        # Process the first string
        for char in s:
            count[ord(char) - ord('a')] += 1
            
        # Process the second string
        for char in t:
            count[ord(char) - ord('a')] -=1
            
        # Check if all counts are zero
        for cnt in count:
            if cnt != 0:
                return False
            
        return True
```
## Time Complexity
- Initialization: `𝑂(1)`
- First Loop runs `n` times. Each iteration is  `𝑂(1)`. So, total time for the inner loop is `𝑂(n)`.
- 2nd loop also runs `n` times. Each iteration is  `𝑂(1)`. So, total time for the inner loop is `𝑂(n)`.
- Third loop runs for fixed size of 26. Since the size of the array is constant, this loop runs in `𝑂(1)` time.
- To calculate the total time complexity:
    ```
    𝑂(1) + 𝑂(n) + 𝑂(n) + 𝑂(1)
    𝑂(2n)
    So, total time complexty is: 𝑂(n)
   ```