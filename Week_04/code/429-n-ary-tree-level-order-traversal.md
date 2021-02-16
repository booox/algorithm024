# 429. N 叉树的层序遍历: 

[429. N 叉树的层序遍历](https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/)

```
给定一个 N 叉树，返回其节点值的层序遍历。（即从左到右，逐层遍历）。

树的序列化输入是用层序遍历，每组子节点都由 null 值分隔（参见示例）。

示例 1：

输入：root = [1,null,3,2,4,null,5,6]
输出：[[1],[3,2,4],[5,6]]
```
## 方法 1: 使用 BFS

### 思路

* 与 [二叉树的层序遍历](102-binary-tree-level-order-traversal.md) 一样使用 BFS
* 只是稍有不同的是，二叉是最多只包含 left 与 right 两个子节点
* 而 `n叉树` 中节点则可能包含多个子节点

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # use bfs
        if not root:
            return []

        level, res = [root], []
        while level:
            child_level = []  # 存储下一层节点
            node_vals = []
            for node in level:
                node_vals.append(node.val)
                # 如果节点还有子节点
                if node.children:
                    for cnode in node.children:
                        child_level.append(cnode)
                        
            res.append(node_vals)
            level = child_level
        return res
            
```

### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()


## 方法 2: 使用 DFS

### 思路

* 将 [二叉树的层序遍历](102-binary-tree-level-order-traversal.md) 中 DFS 代码稍做变化即可。 

```python
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # 2. use dfs
        if not root:
            return []

        res = []
        self.__dfs(root, 0, res)
        return res

    def __dfs(self, root, level, res):
        # terminator
        if not root:
            return

        # process
        if len(res) <= level:
            res.append([])
        
        res[level].append(root.val)

        # drill down
        for cnode in root.children:
            self.__dfs(cnode, level + 1, res)
```

### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()
