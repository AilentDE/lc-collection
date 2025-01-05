from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for x in s:
            if x in ["(", "[", "{"]:
                stack.append(x)
            else:
                if not stack:
                    return False
                if x == ")" and stack[-1] != "(":
                    return False
                if x == "]" and stack[-1] != "[":
                    return False
                if x == "}" and stack[-1] != "{":
                    return False
                stack.pop()
        return not stack


if __name__ == "__main__":
    s = Solution()

    sol1 = s.isValid("()")
    assert sol1 is True

    sol2 = s.isValid("()[]{}")
    assert sol2 is True

    sol3 = s.isValid("(]")
    assert sol3 is False

    sol4 = s.isValid("([)]")
    assert sol4 is False

    sol5 = s.isValid("{[]}")
    assert sol5 is True

    sol6 = s.isValid("}{[]")
    assert sol6 is False
