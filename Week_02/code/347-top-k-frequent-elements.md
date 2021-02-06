# 347. 前 K 个高频元素: 

[347. 前 K 个高频元素](https://leetcode-cn.com/problems/top-k-frequent-elements/)

```
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

 

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]
 

提示：

你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
你可以按任意顺序返回答案。

```
## Python

### 方法 1: 使用哈希表，排序后输出（时间复杂度不符合要求）

#### 思路

* 这个思路是最容易想到的，维护一个哈希表，遍历数组，统计每个数出现的次数
* 对数组按值进行排序
* 再用切片输出前 k 个元素

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= 1: return nums

        # 1. 用哈希表统计词频，排序后输出
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        
        freq = sorted(d.items(), key=lambda x: x[1], reverse=True )

        return [x[0] for x in freq][:k]
```

#### 复杂度分析

* 时间复杂度：O(nlogn)
    * 第一步遍历：O(n); 
    * 关键是第二步排序: 可能会每个元素出现的次数都不相同，即有 n 个不同的次数，则复杂度为 O(nlogn)
* 空间复杂度：O(n)


### 方法 2: 使用哈希表统计词频，用小根堆处理 topK

#### 思路

* 遍历数组，维护一个大小为 k 的小根堆
* 当堆的容量小于 k 时，直接将当前数字加入堆中
* 否则，判断当前数字对应的次数，是否大于堆中最小次数
    * 若是，则删除堆中出现次数最少的那个数字，并将当前数字加入堆中 

```python
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= 1: return nums

        # 2. 用哈希表统计词频，再用小根堆
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1

        heap = []
        for key, value in d.items():
            if len(heap) < k:
                heapq.heappush(heap, (value, key))
            elif value > heap[0][0]:
                heapq.heapreplace(heap, (value, key))

        return [x[1] for x in heap]
```

#### 复杂度分析

* 时间复杂度：O(n+klogk)
* 空间复杂度：O(n)


### 方法 3: 用 Counter 统计词频，再用小根堆

#### 思路

* 

```python
import heapq
import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= 1: return nums

        cnt = collections.Counter(nums)

        heap = []
        for key in cnt:
            if len(heap) < k:
                heapq.heappush(heap, (cnt[key], key))
            elif cnt[key] > heap[0][0]:
                heapq.heapreplace(heap, (cnt[key], key))

        return [x[1] for x in heap]
```

#### 复杂度分析

* 时间复杂度：O(n+klogk)
* 空间复杂度：O(n))
