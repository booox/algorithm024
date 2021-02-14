# 46. 全排列: 

## 类似题
* [46. 全排列](https://leetcode-cn.com/problems/permutations/)
* [47. 全排列 II](https://leetcode-cn.com/problems/permutations-ii/)

```
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

## 方法 : 

### 思路

* 

```python

```

### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()



# 47. 全排列 II: 

[47. 全排列 II](https://leetcode-cn.com/problems/permutations-ii/)

```
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

示例 1：

输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
示例 2：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

提示：

1 <= nums.length <= 8
-10 <= nums[i] <= 10

```

## 方法 : 

### 思路

* 与上一题的区别就是，本题包含重复的数字，难点在于如何去重
* 可以先将 `nums` 排序，而后通过下面语句来去重
    * `if i > 0 and nums[i] == nums[i - 1] and used[i - 1] = True:`

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 1. use dfs
        # 数字有重复，先排序
        size = len(nums)
        if size == 0:
            return [nums]
        
        # sort
        nums.sort()

        res, used = [], [False] * size
        self.__dfs(nums, 0, used, [], res)
        return res

    def __dfs(self, nums, depth, used, path, res):
        # terminator
        if depth == len(nums):
            res.append(path[:])
            return

        # process
        for i in range(len(nums)):
            if not used[i]:
                # pruning
                if i > 0 and nums[i] == nums[i - 1] and used[i - 1] == True:
                    continue

                used[i] = True
                path.append(nums[i])
                # drill down
                self.__dfs(nums, depth + 1, used, path, res)
                # revert states
                used[i] = False
                path.pop()
```

### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()
