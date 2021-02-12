# 78. 子集: 

[78. 子集](https://leetcode-cn.com/problems/subsets/)

```
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

 

示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：

输入：nums = [0]
输出：[[],[0]]
 

提示：

1 <= nums.length <= 10
-10 <= nums[i] <= 10
nums 中的所有元素 互不相同
```
## Python

**总体思路**

* 对于组合、排列这类问题，要首先画出递归结构树，有利于思考
* 因为是组合问题，只需按顺序读字符，就不需要设置 used 数组； 
* `nums` 中每个元素都有两种状态：选，或不选* 


### 方法 1: 使用递归，深度优先搜索

#### 思路

* 执行一次深度优先遍历，一条路走到底，走不通的时候，返回回来，继续执行，一直这样下去，直到回到起点。


```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 1. 回溯算法，
        # 在回溯中记录深度，将每个深度得到的子集添加到结果中
        size = len(nums)
        if size == 0:
            return [nums]

        res = []
        for i in range(size + 1):
            self.__dfs(nums, size, i, 0, [], res)

        return res

    def __dfs(self, nums, size, depth, begin, path, res):
        # 如果 path 长度等于 depth，进行结算
        if len(path) == depth:
            res.append(path[:])
            return

        for i in range(begin, size):
            path.append(nums[i])
            # 因为元素不重复，所以总是取 i + 1
            self.__dfs(nums, size, depth, i + 1, path, res)
            path.pop()
```

#### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(n)

### 方法 2: 使用递归，深度优先搜索 

#### 思路

* 回溯算法，回溯过程中记录节点
* 参考：[回溯 + 位运算技巧（Java、Python）- @liweiwei](https://leetcode-cn.com/problems/subsets/solution/hui-su-python-dai-ma-by-liweiwei1419/)

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 回溯算法，回溯过程中记录节点
        size = len(nums)
        if size == 0:
            return [nums]
        
        res = []
        self.__dfs(nums, size, 0, [], res)
        return res

    def __dfs(self, nums, size, begin, path, res):
        # 遇到节点就添加
        res.append(path[:])

        for i in range(begin, size):
            path.append(nums[i])
            self.__dfs(nums, size, i + 1, path, res)
            path.pop()

```

#### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(n)

### 方法 3: 回溯，深度优先搜索

#### 思路

* 本题可以借鉴「生成括号」那一题的思路
    * 将 `nums` 中 n 个数，看成有 n 个格子
    * 每个格式有 1 个数，而这个数有两种状态：「选」和「不选」

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 回溯，dfs
        # 将 `nums` 中 n 个数，看成有 n 个格子
        # 每个格子有 1 个数，而这个数有两种状态：「选」和「不选」
        size = len(nums)
        if size == 0:
            return [nums]

        res = []
        self.__dfs(nums, 0, [], res)
        return res

    def __dfs(self, nums, depth, path, res):
        # terminator
        # 当深度等于长度时，进行结算
        if depth == len(nums):
            res.append(path[:])
            return

        # process
        # drill down
        # 每个格子有两种状态，选与不选
        
        self.__dfs(nums, depth + 1, path, res) # 选
        path.append(nums[depth])
        
        self.__dfs(nums, depth + 1, path, res) # 不选
        path.pop()
        # revert states
```

**最后四句代码的顺序不同，效果一样，返回不一样**

```python
        # 1.
        path.append(nums[depth])
        self.__dfs(nums, depth + 1, path, res) # 选
        
        path.pop()
        self.__dfs(nums, depth + 1, path, res) # 不选

        # 2.
        self.__dfs(nums, depth + 1, path, res) # 选
        path.append(nums[depth])
        
        self.__dfs(nums, depth + 1, path, res) # 不选
        path.pop()

```

#### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()


### 方法 4: 使用迭代的方法

#### 思路

* 先找到它的重复性：
    * 结果集初始为 `[]` 空数组
    * 对 `nums` 元素，依次放入结果集中

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # # 4. use iterate
        if len(nums) == 0:
            return [nums]

        # 方法 1
        res = [[]]
        for n in nums:
            tmp = []
            for x in res:
                tmp.append(x + [n])
            res += tmp
        return res

        # 方法 2
        res = [[]]
        for n in nums:
            res += [x + [n] for x in res]
        return res
```

#### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()
