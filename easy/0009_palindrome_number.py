class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]


if __name__ == "__main__":
    s = Solution()

    sol1 = s.isPalindrome(121)
    assert sol1 is True

    sol2 = s.isPalindrome(-121)
    assert sol2 is False

    sol3 = s.isPalindrome(10)
    assert sol3 is False
