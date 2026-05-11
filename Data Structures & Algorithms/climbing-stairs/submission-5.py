class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        if n <= 1:
            return n
        
        for _ in range(n - 1):
            a, b = b, a + b
        return b