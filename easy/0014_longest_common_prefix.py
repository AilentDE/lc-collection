from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        current_prefix = ""
        for i in zip(*strs):
            if len(set(i)) == 1:
                current_prefix += i[0]
            else:
                break
        return current_prefix


if __name__ == "__main__":
    s = Solution()

    sol1 = s.longestCommonPrefix(["flower", "flow", "flight"])
    assert sol1 == "fl"

    sol2 = s.longestCommonPrefix(["dog", "racecar", "car"])
    assert sol2 == ""
