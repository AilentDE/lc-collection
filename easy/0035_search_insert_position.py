import bisect
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)


if __name__ == "__main__":
    s = Solution()

    sol1 = s.searchInsert([1, 3, 5, 6], 5)
    assert sol1 == 2

    sol2 = s.searchInsert([1, 3, 5, 6], 2)
    assert sol2 == 1

    sol3 = s.searchInsert([1, 3, 5, 6], 7)
    assert sol3 == 4
