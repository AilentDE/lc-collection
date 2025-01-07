class Solution:
    def mySqrt(self, x: int) -> int:
        pointer = x // 2
        while pointer * pointer > x:
            pointer = pointer // 2
        while pointer * pointer <= x:
            pointer += 1
        return pointer - 1


if __name__ == "__main__":
    s = Solution()

    sol1 = s.mySqrt(4)
    assert sol1 == 2

    sol2 = s.mySqrt(8)
    assert sol2 == 2
