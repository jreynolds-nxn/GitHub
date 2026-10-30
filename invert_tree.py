from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    value: int
    left: Optional[TreeNode] = None
    right: Optional[TreeNode] = None


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """Mirror a binary tree in place by swapping the children of every node.

    Iterative to avoid recursion limits on deep (skewed) trees.
    Runs in O(n) time and O(w) extra space, where w is the tree's max width.
    """
    stack = [root] if root else []
    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return root


def to_list(root: Optional[TreeNode]) -> list:
    """Level-order representation, using None for missing children."""
    out, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            out.append(None)
            continue
        out.append(node.value)
        queue.extend([node.left, node.right])
    while out and out[-1] is None:
        out.pop()
    return out


if __name__ == "__main__":
    tree = TreeNode(
        4,
        TreeNode(2, TreeNode(1), TreeNode(3)),
        TreeNode(7, TreeNode(6), TreeNode(9)),
    )
    print("before:", to_list(tree))
    print("after: ", to_list(invert_tree(tree)))
    assert to_list(invert_tree(None)) == []
    assert to_list(invert_tree(TreeNode(1))) == [1]
    deep = TreeNode(0)
    cur = deep
    for i in range(1, 50_000):
        cur.left = TreeNode(i)
        cur = cur.left
    assert invert_tree(deep).right is not None
