from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q or p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":

    def deserialize(data):
        if not data:
            return None
        root = TreeNode(data[0])
        queue = [root]
        index = 1
        while queue:
            node = queue.pop(0)
            move = 0
            if index < len(data):
                node.left = TreeNode(data[index]) if data[index] is not None else None
                if node.left:
                    queue.append(node.left)
                move += 1
            if index + 1 < len(data):
                node.right = (
                    TreeNode(data[index + 1]) if data[index + 1] is not None else None
                )
                if node.right:
                    queue.append(node.right)
                move += 1
            index += move

        return root

    s = Solution()

    p = deserialize([1, 2, 3])
    q = deserialize([1, 2, 3])
    assert s.isSameTree(p, q) is True

    p = deserialize([1, 2])
    q = deserialize([1, None, 2])
    assert s.isSameTree(p, q) is False

    p = deserialize([1, 2, 1])
    q = deserialize([1, 1, 2])
    assert s.isSameTree(p, q) is False
