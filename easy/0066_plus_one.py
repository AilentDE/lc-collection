from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(el) for el in str(int("".join(map(str, digits))) + 1)]


if __name__ == "__main__":
    s = Solution()

    sol1 = s.plusOne([1, 2, 3])
    assert sol1 == [1, 2, 4]

    sol2 = s.plusOne([4, 3, 2, 1])
    assert sol2 == [4, 3, 2, 2]

    sol3 = s.plusOne([9])
    assert sol3 == [1, 0]
