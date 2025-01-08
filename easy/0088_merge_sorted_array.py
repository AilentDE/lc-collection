from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if not nums1 or not nums2:
            return nums1.extend(nums2)

        nums1[m:] = nums2
        nums1.sort()


if __name__ == "__main__":
    s = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    s.merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 2, 3, 5, 6]

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    s.merge(nums1, m, nums2, n)
    assert nums1 == [1]

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    s.merge(nums1, m, nums2, n)
    assert nums1 == [1]
