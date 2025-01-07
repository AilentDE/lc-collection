from functools import lru_cache


class Solution:

    @lru_cache(maxsize=50)
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)


if __name__ == "__main__":
    s = Solution()

    sol1 = s.climbStairs(2)
    assert sol1 == 2

    sol2 = s.climbStairs(3)
    assert sol2 == 3
