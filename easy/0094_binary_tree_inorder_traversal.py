from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return (
            self.inorderTraversal(root.left)
            + [root.val]
            + self.inorderTraversal(root.right)
        )


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

    root = deserialize([1, None, 2, 3])
    sol1 = s.inorderTraversal(root)
    assert sol1 == [1, 3, 2]

    root = deserialize([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])
    sol2 = s.inorderTraversal(root)
    assert sol2 == [4, 2, 6, 5, 7, 1, 3, 9, 8]

    root = deserialize([])
    sol3 = s.inorderTraversal(root)
    assert sol3 == []

    root = deserialize([1])
    sol4 = s.inorderTraversal(root)
    assert sol4 == [1]
