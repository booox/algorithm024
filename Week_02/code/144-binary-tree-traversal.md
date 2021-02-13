# 二叉树的遍历: 

对于一维数据，如数组、链表，如果要查询一个元素，则需要「遍历」。而对于二维数据，**树**，也如此，如果树中的数据是无序的，那更需要「遍历」，才能找到元素。

原文链接： [图解 二叉树的四种遍历 @腐烂的橘子](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/tu-jie-er-cha-shu-de-si-chong-bian-li-by-z1m/)

## 相关题目

* [144.二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/)
* [94. 二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)
* [145. 二叉树的后序遍历](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/)
* [102. 二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)


## 基本概念

### 树的一些概念

**高度（Height）**

* 节点到叶子节点的「最长路径」（边数）
* 树的高度：根节点的高度

**深度（Depth）**

* 根节点到这个节点所经历的「边的个数」

**层（Level）**

* 节点的深度 + 1


### 二叉树（Binary Tree）

* 每个节点最多有两个「叉」，也就是两个子节点，分别为「左子节点」和「右子节点」。
* 但并不要求每个节点都要有两个子节点。

**满二叉树**

* 叶子节点全都在最底层，除叶子节点之外，每个节点都有左右两个子节点。

**完全二叉树**

* 叶子节点都在最底下两层，最后一层的叶子节点都靠左排列
* 除最后一层，其他层的节点个数都要达到最大



### 遍历方式

如何将所有节点都遍历打印出来呢？

经典的方法有三种：

* 前序（Pre-order）：根-左-右
    * 对树中任意节点来说，先打印这个节点，再左子树，再右子树

* 中序（In-order）：左-根-右
    * 对树中任意节点来说，先打印左子树，再这个节点，再右子树 

* 后序（Post-order）：左-右-根
    * 对树中任意节点来说，先打印左子树，再右子树，再这个节点


## 递归实现（前中后）


### 前序遍历

```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(root):
            if not root:
                return
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)


        res = []
        dfs(root)
        return res
```

### 中序遍历

```python
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(root):
            if not root:
                return

            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        
        res = []
        dfs(root)
        return res
```

### 后序遍历

```python
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(root):
            if not root:
                return

            dfs(root.left)
            dfs(root.right)
            res.append(root.val)
        
        res = []
        dfs(root)
        return res
```

### 复杂度分析

* 时间复杂度：O(n)
    * 每个节点最多会被访问两次，所以时间复杂度与节点个数 n 成正比
* 空间复杂度：O(n)


## 迭代实现（前中后）

### 二叉树的前序遍历

#### 常规解法

我们使用「栈」来进行迭代，过程如下：

* 初始化栈，并将「根节点」入栈；
* 当栈不为空时：
    * 弹出栈顶元素 node，并将值添加到结果中；
    * 如果 node 的右子树非空，将右子树入栈；
    * 如果 node 的左子树非空，将左子树入栈；

由于栈是“先进后出”的顺序，所以入栈时先将右子树入栈，这样使得前序遍历结果为 “根->左->右”的顺序。

**参考代码**

```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return res
```

#### 模板解法

我们使用「栈」来进行迭代，过程如下：

* 它先将根节点 cur 和所有的左孩子入栈并加入结果中，直至 curr 为空，用一个 while 循环实现：
* 然后，每弹出一个栈顶元素，就到达它的右孩子，再将这个节点当作 curr 重新按上面的步骤来一遍，直至栈为空。这里又需要一个 while 循环。


**参考代码**

```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []

        curr, stack, res = root, [], []
        while curr or stack:
            while curr:  # 根节点和左子树入栈
                res.append(curr.val)
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()  # 每弹出一个元素，就到达了右子树
            curr = curr.right

        return res
```



### 二叉树的中序遍历

#### 模板解法

和前序遍历的代码完全相同，只是在出栈的时候才将节点 的值加入结果集中。

**参考代码**

```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []

        curr, stack, res = root, [], []
        while curr or stack:
            while curr:  # curr 入栈， 直到到达最左端叶子节点
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()  # 弹出一个元素，就是左边最小的
            res.append(curr.val) # 将值添加到结果集中
            curr = curr.right    # 指向右子树

        return res
```

### 二叉树的后序遍历

#### 模板解法

* 继续按照上面的思想，这次我们反着思考，节点 cur 先到达最右端的叶子节点并将路径上的节点入栈；
* 然后每次从栈中弹出一个元素后，cur 到达它的左孩子，并将左孩子看作 cur 继续执行上面的步骤。
* 最后将结果反向输出即可。


**参考代码**

```python
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []

        curr, stack, res = root, [], []
        while curr or stack:
            while curr:  # 先到达最右端
                res.append(curr.val)
                stack.append(curr)
                curr = curr.right
            curr = stack.pop()  # 每弹出一个元素，就到达了右子树
            curr = curr.left

        return res[::-1]  # 反向输出
```

> 然而，后序遍历采用模板解法并没有按照真实的栈操作，而是利用了结果的特点反向输出，不免显得技术含量不足。
> 因此掌握标准的栈操作解法是必要的。



#### 常规解法

* 类比前序遍历的常规解法，我们只需要将输出的“根 -> 左 -> 右”的顺序改为“左 -> 右 -> 根”就可以了。
* 如何实现呢？这里右一个小技巧，我们入栈时额外加入一个标识，比如这里使用 `flag = 0`；
* 然后每次从栈中弹出元素时，如果 flag 为 0,则需要将 flag 变为 1 并连同该节点再次入栈，只有当 flag 为 1 时才可将该节点加入到结果中。

**参考代码**

```python
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        stack, res = [(0, root)], []

        while stack:
            flag, node = stack.pop()
            if not node: continue
            if flag == 1:
                res.append(node.val)
            else:
                stack.append((1, node))
                stack.append((0, node.right)) # 右
                stack.append((0, node.left))  # 左

        return res
```

> 然而，后序遍历采用模板解法并没有按照真实的栈操作，而是利用了结果的特点反向输出，不免显得技术含量不足。
> 因此掌握标准的栈操作解法是必要的。



## 二叉树的层次遍历

### 方法 : 

#### 思路

* 二叉树的层次遍历的迭代方法与前面不用，因为前面的都采用了「深度优先搜索」的方式，
* 而层次遍历使用了「广度优先搜索」，广度优先搜索主要使用「队列」实现，也就不能使用前面的模板解法了。

广度优先搜索的步骤为：

* 初始化队列 q，并将根节点 root 加入到队列中；
* 当队列不为空时：
    * 队列中弹出节点 node，加入到结果中；
    * 如果左子树非空，左子树加入队列；
    * 如果右子树非空，右子树加入队列；
* 由于题目要求每一层保存在一个子数组中，所以我们额外加入了 level 保存每层的遍历结果，并使用 for 循环来实现。

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []

        res, q = [], [root]
        while q:
            n = len(q)
            level = []
            for i in range(n):
                node = q.pop(0)   # 这里 q 相当于一个队列
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res
```

#### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()
