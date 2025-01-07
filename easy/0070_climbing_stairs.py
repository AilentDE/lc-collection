from functools import lru_cache


@lru_cache(maxsize=50)
def climb_stairs(n: int) -> int:
    if n <= 3:
        return n
    else:
        return climb_stairs(n - 1) + climb_stairs(n - 2)


class Solution:

    def climbStairs(self, n: int) -> int:
        return climb_stairs(n)


if __name__ == "__main__":
    s = Solution()

    sol1 = s.climbStairs(2)
    assert sol1 == 2

    sol2 = s.climbStairs(3)
    assert sol2 == 3
