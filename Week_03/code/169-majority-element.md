# 169. 多数元素: 

[169. 多数元素](https://leetcode-cn.com/problems/majority-element/)

```
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1：

输入：[3,2,3]
输出：3
示例 2：

输入：[2,2,1,1,1,2,2]
输出：2
 

进阶：

尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
```
## 方法 1: 用哈希表统计数频

### 思路

* 最容易想到的就是用哈希表统计数频
* 而且，再对遍历哈希表

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 1. 直观想法，用哈希表对数组中元素直接统计出现次数，再遍历，将大于 n / 2 的输出
        import collections
        cnt = collections.Counter(nums)
        count = len(nums) / 2
        for k, v in cnt.items():
            if v > count:
                return k
```

### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()
