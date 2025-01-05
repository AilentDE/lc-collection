class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        result = 0

        for i, x in enumerate(s):
            if i < len(s) - 1 and mapping[x] < mapping[s[i + 1]]:
                result -= mapping[x]
            else:
                result += mapping[x]

        return result


if __name__ == "__main__":
    s = Solution()
    sol1 = s.romanToInt("III")
    assert sol1 == 3

    sol2 = s.romanToInt("LVIII")
    assert sol2 == 58

    sol3 = s.romanToInt("MCMXCIV")
    assert sol3 == 1994
