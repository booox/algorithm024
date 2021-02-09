# 226. 翻转二叉树: 

[226. 翻转二叉树](https://leetcode-cn.com/problems/invert-binary-tree/)

```
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
备注:
这个问题是受到 Max Howell 的 原问题 启发的 ：

谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。
```
## Python

### 方法 1: 递归

参考：[动画演示 两种实现 226. 翻转二叉树](https://leetcode-cn.com/problems/invert-binary-tree/solution/dong-hua-yan-shi-liang-chong-shi-xian-226-fan-zhua/)

#### 思路

* 这是个有故事的题目
* 看到二叉树，首先去想，能不能用「递归」来解决
* 对于本题
  * 先交换当前节点的「左右节点」
  * 再递归交换当前节点的「左节点」，递归交换当前节点的「右节点」
* 具体实现，可以用「递归」的模板来写，共 4 个步骤
  * teminator
  * process
  * drill down
  * revert states

```python
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # terminator
        if not root:
            return root

        # process
        root.left, root.right = root.right, root.left

        # drill down
        self.invertTree(root.left)
        self.invertTree(root.right)

        # revert states

        return root
```


**换种思路**

* 先换递归换左右子树，再换内部


```python
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 2. use recursion
        # terminator
        if not root:
            return root

        # drill down
        self.invertTree(root.left)
        self.invertTree(root.right)

        # process
        root.left, root.right = root.right, root.left

        # revert states

        return root
```

#### 复杂度分析

* 时间复杂度：O(n)
  * 每个节点至少访问一次
* 空间复杂度：O(h)
  * h 为二叉树的高度


