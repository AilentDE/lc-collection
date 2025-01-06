from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer = 0

        for el in nums:
            if el != val:
                nums[pointer] = el
                pointer += 1
        return pointer


if __name__ == "__main__":
    s = Solution()

    sol1 = s.removeElement([3, 2, 2, 3], 3)
    assert sol1 == 2

    sol2 = s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
    assert sol2 == 5
