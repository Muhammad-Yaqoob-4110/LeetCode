## Table of Contents
- [Table of Contents](#table-of-contents)
- [Problem Staement](#problem-staement)
- [Source Code](#source-code)
- [Time Complexity](#time-complexity)

## Problem Staement
https://leetcode.com/problems/find-the-highest-altitude/

## Source Code
```
class Solution(object):
    def largestAltitude(self, gain):
        altitudes = []
        altitude = 0
        altitudes.append(0)
        for i in range(len(gain)):
            altitude = altitude + gain[i]
            altitudes.append(altitude)
        
        return sorted(altitudes, reverse = True)[0]
```
## Time Complexity
- Initilization: `𝑂(1)`
- Loop runs `n` times. Each iteration is  `𝑂(1)`.So, total time for the loop is `𝑂(n)`.
- Sorting:  `𝑂((n + 1)log(n + 1))`
- To calculate the total time complexity:
    ```
    𝑂(1) + 𝑂(n) + 𝑂((n + 1)log(n + 1))
    𝑂((n + 1)log(n + 1))
    So, total time complexty is: 𝑂(nlogn)
   ```
    
