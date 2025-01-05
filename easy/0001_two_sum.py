from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        collection = {}
        for i, x in enumerate(nums):
            if target - x in collection:
                return [collection[target - x], i]
            collection[x] = i
        return []


if __name__ == "__main__":
    s = Solution()

    sol1 = s.twoSum([2, 7, 11, 15], 9)
    assert sol1 == [0, 1]

    sol2 = s.twoSum([3, 2, 4], 6)
    assert sol2 == [1, 2]

    sol3 = s.twoSum([3, 3], 6)
    assert sol3 == [0, 1]
