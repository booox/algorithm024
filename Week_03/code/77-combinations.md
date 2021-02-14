# 77. 组合: 

[77. 组合](https://leetcode-cn.com/problems/combinations/)

```
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
```
## 方法 : 

### 思路

* 找题目中的关键字「所有可能」，这意味着要对所有情况进行「遍历」
* 注意「组合」与「排列」之间的区别
    * 排列：顺序不同，表示不同的排列
    * 组合：与顺序无关
* 「排列」与「组合」，首先考虑使用「回溯算法」
    * 「回溯算法」是在树上进行「深度优先搜索」
* 使用「递归」模板
    * teminator
    * process
    * drill down 
    * revert states 


```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 看到组合，想到用回溯
        if n < 1 or k < 1:
            return [[]]

        nums = list(range(1, n + 1))
        size = len(nums)

        res = []
        self.__dfs(nums, size, k, 0, 0, [], res)
        return res

    def __dfs(self, nums, size, k, depth, begin, path, res):
        # terminator
        if depth == k:
            res.append(path[:])
            return

        # process
        for i in range(begin, size):
            path.append(nums[i])
            # drill down
            self.__dfs(nums, size, k, depth + 1, i + 1, path, res)
            # revert states
            path.pop()
```

### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()

