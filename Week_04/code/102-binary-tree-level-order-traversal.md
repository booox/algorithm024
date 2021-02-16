# 102. 二叉树的层序遍历: 

[102. 二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)

```
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

 

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层序遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
```
## 方法 1: 广度优先搜索

### 思路

* 要按层对二叉树进行遍历，可以先对当前层遍历，同时在遍历时收集下一层的节点
* 直到最后没有再下一层的节点为止

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # level order traversal
        if not root:
            return []

        level, res = [root], []  # 当前层需要遍历的所有节点集合，最终的结果集
        while level:
            nodes = []
            tmp = []
            for node in level:
                tmp.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            res.append(tmp)
            level = nodes

        return res
```

当然，对于 `for` 循环这样写也是一种思路，但上面更简洁：

```python
            for i in range(len(level)):
                child.append(level[i].val)
                if level[i].left:
                    nodes.append(level[i].left)
                if level[i].right:
                    nodes.append(level[i].right)
```

### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O()

## 方法 2: 深度优先搜索 DFS

### 思路

* 深度优先搜索遍历的顺序，是沿着一条路「走到底」
    * 根 - 左 - 左 - 左 - ……
* 这样就会存在一个问题，在遍历时，并不清楚当前节点属于第几层
    * 就需要用一个变量 `level` 记录当前处于第几层

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # use dfs
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
            res.append(list())

        res[level].append(root.val)

        # drill down
        if root.left:
            self.__dfs(root.left, level + 1, res)
        if root.right:
            self.__dfs(root.right, level + 1, res)

        # revert states
```

### 复杂度分析

* 时间复杂度：O(n)
    * n 为节点数 
* 空间复杂度：O(n) + O(h)
    * n 为节点数，h 为树的高度
