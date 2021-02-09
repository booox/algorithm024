# 98. 验证二叉搜索树: 

[98. 验证二叉搜索树](https://leetcode-cn.com/problems/validate-binary-search-tree/)

```
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

```
## Python

### 方法 1: 递归 + 帮助函数

#### 思路

* 先复习一下，什么是「二叉搜索树」？
    * 在树中的任意一个节点，其「左子树」节点的值均小于该节点的值，其「右子树」节点的值均大于该节点的值
    * 需要注意的是，这里的「左右子树」是指全部的子树节点，不只是当前节点的「左右孩子」节点
* 再来看这题的解题思路
    * 先要明确，这个问题存在「重复子问题」，所以可以用「递归」来解决
        * 所谓「重复子问题」，在根节点，如果不为空（为空也是有效节点），则必须满足 左 < 根 < 右
        * 当下探到下面层级时，也同样需要满足 左 < 根 < 右，不同的是，这里的根变成了新节点
    * 先判断 左边 < 根 及 根 < 右边，是否成立，不成立直接返回 False
    * 判断完根节点，需要「下探」到下一级节点，直接递归调用原函数
        * 只是：在左边，原来的根变成新的屋顶；在右边，原来的根变成新的地板了。


* [官方题解](https://leetcode-cn.com/problems/validate-binary-search-tree/solution/yan-zheng-er-cha-sou-suo-shu-by-leetcode-solution/)

```python
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # use recursion, with dfs func
        def dfs(node, lower=float('-inf'), upper=float('inf')):
            # 1. 终止条件
            if not node:
                return True
            if val <= lower or val >= upper:
                return False
            # 2. 处理（这里不需要）

            # 3. 下探到下一层
            val = node.val            
            if not dfs(node.right, val, upper):
                return False
            if not dfs(node.left, lower, val):
                return False
            
            # 4. 清理当前层（不需要）
            return True

        return dfs(root)
```

上述代码还可以再优化
第 3 步 “下探到下一层” 可以写成一句

```python
            val = node.val            
            if not dfs(node.right, val, upper):
                return False
            if not dfs(node.left, lower, val):
                return False

            # ====>
            return dfs(node.left, node.val, upper) and \
                   dfs(node.right, lower, node.val)

```

参考[国际站](https://leetcode.com/problems/validate-binary-search-tree/discuss/32178/Clean-Python-Solution/31031)

```python
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 2. use recursion - 2
        def dfs(node, floor=float('-inf'), ceiling=float('inf')):
            if not node:
                return True
            if node.val <= floor or node.val >= ceiling:
                return False
            return dfs(node.left, floor, node.val) and \
                   dfs(node.right, node.val, ceiling)
        return dfs(root)
```

如果修改给定函数参数，上述方法中，还可以连定义辅助函数也省了，但不建议这样做。

```python
class Solution:
    # def isValidBST(self, root: TreeNode) -> bool:

    # 3. 直接修改原函数
    def isValidBST(self, root: TreeNode, floor=float('-inf'), ceiling=float('inf')) -> bool:
        if not root:
            return True
        if root.val <= floor or root.val >= ceiling:
            return False

        return self.isValidBST(root.left, floor, root.val) and \
                self.isValidBST(root.right, root.val, ceiling)
```


#### 复杂度分析

* 时间复杂度：O(n)
    * 二叉树的节点共有 n 个，在递归调用时，每个节点最多被访问一次
* 空间复杂度：O(n)
    * 在递归调用时，需要为每一层递归函数分配栈空间，所以这里需要额外的空间
    * 且该额外的空间取决于递归的深度，即「树的高度」
    * 最坏情况下，二叉树为一条链，高度为 n，递归深度为 n，此时空间复杂度为 O(n)


### 方法 2: 中序遍历（额外数组）

#### 思路

* 前序知识：
    * 二叉搜索树「中序遍历」得到的值构成的序列一定是「升序」的
    * 二叉搜索树中不能有重复元素。
* 直接将二叉搜索树遍历出来，值存入数组中
* 而后再对数组进行遍历，判断是否存在当前值 > 下一个值的情况，若存在，则返回 False


```python
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 4. use inorder, array
        res = []
        self.inOrder(root, res)

        for i in range(len(res) - 1):
            if res[i] >= res[i + 1]:
                return False
        return True

    def inOrder(self, root, res):
        if not root:
            return
        
        self.inOrder(root.left, res)
        res.append(root.val)
        self.inOrder(root.right, res)
```

#### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(n)

> 需要两次完整的遍历，明显慢了许多: 在第一次遍历时，是否可以进行判断？
> 需要将值全部压入数组：能否不存入数组？


* 用排序代替遍历，可以将这一部分的时间复杂度由 O(n) 提升到 O(logn)，总的并不会改变，还是 O(n)

```python
        for i in range(len(res) - 1):
            if res[i] >= res[i + 1]:
                return False
        return True

        # ===>
        return res == sorted(res) and len(res) == len(set(res))
```



### 方法 3: 中序遍历：一次遍历

#### 思路

* 前序知识：
    * 二叉搜索树「中序遍历」得到的值构成的序列一定是「升序」的
* 只要在中序遍历的时候，实时检查当前节点的值是否大于前一个中序遍历到的节点的值即可。
* 如果均大于说明这个序列是升序的，整棵树是二叉搜索树，否则不是
* 可以使用「栈」来模拟中序遍历的过程。

* 比较容易理解的是，直接套用「二叉树的中序遍历」的模板代码，适当修改即可。

```python
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 6. use inorder, template
        if not root:
            return True

        curr, stack, inorder = root, [], float('-inf')
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            if curr.val <= inorder:
                return False

            inorder = curr.val
            curr = curr.right
        return True
```

#### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(n)

