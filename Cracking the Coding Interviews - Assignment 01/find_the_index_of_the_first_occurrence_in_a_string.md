## Table of Contents
- [Table of Contents](#table-of-contents)
- [Problem Staement](#problem-staement)
- [Source Code](#source-code)
- [Time Complexity](#time-complexity)

## Problem Staement
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

## Source Code
```
class Solution(object):
    def strStr(self, haystack, needle):
        return haystack.find(needle)
```
## Time Complexity
- `find()` method searches for the substring in  the string from left to right, and returns the index of the first occurrence. In the worst-case scenario, it has to search through the entire strig, resulting in a lineear time complexity of `𝑂(n)`.

- To calculate the total time complexity:
    ```
    𝑂(n)
    𝑂(n)
    So, total time complexty is: 𝑂(n)
   ```