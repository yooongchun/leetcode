"""
给你一棵二叉树的根节点 root ，返回树的 最大宽度 。

树的 最大宽度 是所有层中最大的 宽度 。

每一层的 宽度 被定义为该层最左和最右的非空节点（即，两个端点）之间的长度。将这个二叉树视作与满二叉树结构相同，两端点间会出现一些延伸到这一层的 null 节点，这些 null 节点也计入长度。

题目数据保证答案将会在  32 位 带符号整数范围内。

 

示例 1：


输入：root = [1,3,2,5,3,null,9]
输出：4
解释：最大宽度出现在树的第 3 层，宽度为 4 (5,3,null,9) 。
示例 2：


输入：root = [1,3,2,5,null,null,9,6,null,7]
输出：7
解释：最大宽度出现在树的第 4 层，宽度为 7 (6,null,null,null,null,null,7) 。
示例 3：


输入：root = [1,3,2,5]
输出：2
解释：最大宽度出现在树的第 2 层，宽度为 2 (3,2) 。
 

提示：

树中节点的数目范围是 [1, 3000]
-100 <= Node.val <= 100

"""
# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """BFS 搜索"""
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 对节点进行编号
        nodes = [[root, 0]]
        max_width = 1
        while nodes:
            max_width = max([max_width, nodes[-1][1] - nodes[0][1]+1])
            new_nodes = []
            for node, i in nodes:
                if node.left:
                    new_nodes.append([node.left, 2*i])
                if node.right:
                    new_nodes.append([node.right, 2*i+1])
            nodes = new_nodes
        return max_width


class Solution2:
    """DFS 搜索"""
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        level_min_index = {} # 每层最小节点的 index
        def dfs(node: TreeNode, depth: int, index: int)->int:
            if not node:
                return 0
            if depth not in level_min_index:
                level_min_index[depth] = index
            
            lwidth = dfs(node.left,depth+1,index*2)
            rwidth = dfs(node.right, depth+1,index*2+1)
            cur_width = index - level_min_index[depth]+1
            return max(lwidth, rwidth, cur_width)
        return dfs(root, 1, 1)
