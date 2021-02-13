# 111. 二叉树的最小深度: 

[111. 二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/)

```
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明：叶子节点是指没有子节点的节点。

示例 1：

输入：root = [3,9,20,null,null,15,7]
输出：2
示例 2：

输入：root = [2,null,3,null,4,null,5,null,6]
输出：5
 
提示：

树中节点数的范围在 [0, 105] 内
-1000 <= Node.val <= 1000
```
## 方法 1: 使用递归：深度优先搜索    

### 思路

* 本题与 [104. 二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree) 类似
* 整棵树的最小深度，应为左子树的最小深度与右子树的最小深度
* 使用递归：
    * 终止条件：遇到空节点或叶子节点，直接返回
    * 向下递归：
        * 如果当前节点有左节点，「下探」到左节点，并与当前最小值比较，取较少者
        * 如果当前节点有右节点，「下探」到右节点，并与当前最小值比较，取较少者
    * 最终返回：最小值 + 1（根节点）
```python
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # 1. use dfs
        # 二叉树的最小深度 = 1 + min(左子树最小深度 + 右子树最小深度)
        
        # terminator
        if not root:        # 空树
            return 0
        if not root.left and not root.right:  # 叶子节点
            return 1

        # process & drill down
        depth = float('inf')
        if root.left:
            depth = min(depth, self.minDepth(root.left))
        if root.right:
            depth = min(depth, self.minDepth(root.right))
        
        # revert states

        return 1 + depth
```

**另一种 dfs**

```python
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # 1. 考虑递归，深度优先搜索
        if not root:
            return 0

        # corner cases
        if root.left and not root.right:
            return 1 + self.minDepth(root.left)
        if root.right and not root.left:
            return 1 + self.minDepth(root.right)
        
        # drill down
        min_left  = self.minDepth(root.left)
        min_right = self.minDepth(root.right)

        return 1 + min(min_left, min_right)
```

### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(n)


## 方法 2: 递归 - 广度优先搜索

### 思路

* 与求最大深度思路类似
* 不同的是：
    * 求最大深度：要遍历到最后一个节点，这里得到的深度是最大深度
    * 求最小深度：只要找到一个叶子节点，就把 depth 返回，这就是「最小」深度

```python
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # 2. use bfs
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        depth = 0
        level = [root]
        while level:
            depth += 1
            nodes = []

            for el in level:
                if not el.left and not el.right:  # 遇到第一个叶子节点，就返回
                    return depth
                if el.left:
                    nodes.append(el.left)
                if el.right:
                    nodes.append(el.right)
            level = nodes
```

### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(n)
