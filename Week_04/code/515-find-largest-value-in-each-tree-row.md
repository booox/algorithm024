# 515. 在每个树行中找最大值: 

[515. 在每个树行中找最大值](https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/)

```
您需要在二叉树的每一行中找到最大的值。

示例：

输入: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

输出: [1, 3, 9]
```
## 方法 1: 使用 BFS，广度优先搜索

### 思路

* 与层序遍历类似，直接使用 BFS 方法进行逐层搜索
* 在逐层搜索开始前，设置一个变量实时更新当前层最大值

```python
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        # use BFS

        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]

        level, res = [root], []
        while level:
            nodes = []
            max_value = float('-inf')
            for node in level:
                max_value = max(max_value, node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            res.append(max_value)
            level = nodes

        return res
```

### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(n)


## 方法 2: 极简的 BFS 代码

### 思路

* 同样的思路，但代码却极为简洁，值得学习
* 参考链接：[Python BFS @StefanPochmann](https://leetcode.com/problems/find-largest-value-in-each-tree-row/discuss/99000/Python-BFS)

```python
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
            
        level, res = [root], []
        while level:
            res.append(max(node.val for node in level))
            level = [kid for node in level for kid in (node.left, node.right) if kid]
        return res
```

### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()


## 方法 3: 使用 DFS，深度优先搜索

### 思路

* 使用深度优先搜索递归遍历二叉树中每一个元素
    * 以「前序遍历」为例
    * 它会先访问根节点，将节点值添加到结果集中
    * 再下探到左子树
    * 再下探到右子树
* 可以使用变量 `level` 来区分添加到结果集中节点，属于哪一层


```python
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        # 2. use dfs
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]

        res = []
        self.__dfs(root, 0, res)
        return res

    def __dfs(self, root, level, res):
        # terminator
        if not root:
            return

        # process
        if level == len(res):  # 递归访问到当前层的第一个元素，则直接添加
            res.append(root.val)
        else:                  # 递归访问到当前层的后面元素，则与已添加的值比较大小后更新
            res[level] = max(res[level], root.val)

        # drill down
        self.__dfs(root.left, level + 1, res)
        self.__dfs(root.right, level + 1, res)
```

### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()
