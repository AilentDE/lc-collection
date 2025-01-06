class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


if __name__ == "__main__":
    s = Solution()

    sol1 = s.lengthOfLastWord("Hello World")
    assert sol1 == 5
