# 104. 二叉树的最大深度: 

[104. 二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)

```
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。   
```
## Python

### 方法 递归：深度优先搜索: 

#### 思路

* 要求整棵树的最大深度，可以这样思考：
    * 如果能告诉我左子树的最大深度，和右子树的最大深度
    * 那最大深度为两者较大者，再加上 1（根节点）

```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 1. 看到二叉树，先想用「递归」
        # 最大深度 = max(左子树最大深度, 右子树最大深度) + 1
        # 可用递归求解
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

> 注意 `1 + max` 这个 Cody Style.

#### 复杂度分析

* 时间复杂度：O(n)
    * 二叉树中每个节点在递归中要被遍历一次
* 空间复杂度：O(height)
    * height 为二叉树的高度。


### 方法 2: 使用 BFS 广度优先搜索

#### 思路

* 这是一个很巧妙的方法，（[参考链接](https://leetcode.com/problems/maximum-depth-of-binary-tree/discuss/34345/Python-BFS-solution)）
* 设置 `level` 数组记录每层节点，初始只有 `root` 节点
* 然后逐层循环进行检查
    * 当前层中每一节点，是否有左右子节点
        * 如果有，则添加至临时层节点集合 `nodes` 中
    * 当前层检查完之后，将 `nodes` 赋给 `level`，执行下一次循环
        * 每次循环时将深度 `depth` 加 `1`
* 最后返回 `depth`

```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 2. use BFS
        if not root:
            return 0

        depth = 0
        level = [root]         # 每层节点集合，初始将 root 压入
        while level:           # 如果当前层不为空，就循环
            depth += 1      
            nodes = []         # 存储当前层节点的集合
            for el in level:   # 检查层内所有节点的左右子节点，若存在，则加入
                if el.left:    
                    nodes.append(el.left)
                if el.right:
                    nodes.append(el.right)
            level = nodes
        return depth
```

#### 复杂度分析

* 时间复杂度：O(n)
    * 每个节点都要访问一次
* 空间复杂度：O()
    * 此方法空间的消耗取决于队列存储的元素数量，其在最坏情况下会达到 O(n)。（leetcode 官方题解）


