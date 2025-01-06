class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


if __name__ == "__main__":
    s = Solution()

    sol1 = s.strStr("hello", "ll")
    assert sol1 == 2

    sol2 = s.strStr("aaaaa", "bba")
    assert sol2 == -1
