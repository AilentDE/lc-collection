class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == "__main__":
    s = Solution()

    sol1 = s.addBinary("11", "1")
    assert sol1 == "100"

    sol2 = s.addBinary("1010", "1011")
    assert sol2 == "10101"
