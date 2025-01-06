from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1


if __name__ == "__main__":
    s = Solution()

    sol1 = s.removeDuplicates([1, 1, 2])
    assert sol1 == 2

    sol2 = s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    assert sol2 == 5
