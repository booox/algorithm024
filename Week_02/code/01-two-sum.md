# 1. 两数之和: 

[1. 两数之和](https://leetcode-cn.com/problems/two-sum)

```

```
## Python

### 方法 1: 暴力解法

#### 思路

* 两层循环
    * 外层循环: i -> (0, n-1)
    * 外层循环: j -> (i + 1, n)
    * 因为只有一个正确解，找到满足条件的即返回

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. 暴力：两层循环
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

#### 复杂度分析

* 时间复杂度：O(n^2)
* 空间复杂度：O(1)


### 方法 2: 使用哈希表

#### 思路

* 对解法一进行优化，将内层循环通过使用哈希表使得查询时间为 O(1)

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 2. 使用哈希表
        d = {}
        for i, n in enumerate(nums):
            if target - n in d:
                return [d[target -n], i]
            else:
                d[n] = i
```

#### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(n)

