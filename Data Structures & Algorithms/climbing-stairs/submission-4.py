class Solution:
    def climbStairs(self, n: int) -> int:
        from functools import lru_cache
        @lru_cache(None)
        def dfs(i):
            if i >= n:
                return i == n
            return dfs(i + 1) + dfs(i + 2)

        return dfs(0)