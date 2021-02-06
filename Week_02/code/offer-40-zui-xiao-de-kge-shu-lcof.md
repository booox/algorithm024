# 剑指 Offer 40. 最小的k个数: 

[剑指 Offer 40. 最小的k个数](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/)

```
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

 

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]
```
## Python

### 方法 1: 先排序，再取前 k 个数

#### 思路

* 这个很容易实现，先排序，再取前 k 个数

```python
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        # 1. 使用暴力，先排序，再取
        arr.sort()
        return arr[:k]
        # time: O(nlogn); space: O(logn)
```

#### 复杂度分析

* 时间复杂度：O(nlogn)
    * 排序的时间复杂度为 O(nlogn)，也即整体的复杂度
* 空间复杂度：O(logn)
    * 排序所需额外的空间复杂度为 O(logn)

### 方法 2: 使用快排

#### 思路

* 这里要找的是「最小的 k 个数」，也是属于 TopK 问题
    * 这种类型的题，是不需要将整个数组进行 O(nlogn) 排序的


```python

```

#### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()

### 方法 3: 直接使用 heapq 的 `nsmallest`

#### 思路

* 在 heaqp 中有个 API 叫 `nsmallest` 可以直接返回对应的值
* 还有个对应的 `nlargest` 可以直接返回对应的值

```python
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        # 3. use heapq
        import heapq
        return heapq.nsmallest(k, arr)
```

#### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()

### 方法 4: 使用小顶堆

#### 思路

* 将所有元素压入堆中
* 循环执行 k 次取出最小值

```python
import heapq

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        # 使用小顶堆
        if k == 0 or arr == []:
            return []
        if len(arr) <= k:
            return arr

        heap, res = [], []

        # 将全部元素加到 heap 中
        for n in arr:
            heapq.heappush(heap, n)

        # 循环 k 次，
        while k > 0: 
            res.append(heapq.heappop(heap))   # heappop: 弹出并返回堆中最小值
            k -= 1
        return res

        # time: O(nlogn)
```

#### 复杂度分析

* 时间复杂度：O(nlogn)
    * n 为数组大小，将所有元素回到堆中，需要 O(nlogn) 的时间复杂度
* 空间复杂度：O()


### 方法 5: 大顶堆

#### 思路

* 要求前 k 小，维护一个容量为 k 的大根堆，每次poll出最大的数
* 堆中保留的就是「前 k 小」

```python
import heapq

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        # 5. 使用大顶堆
        if k == 0 or arr == []:
            return []
        if len(arr) <= k:
            return arr       

        heap = []
        for x in arr[:k]:
            heapq.heappush(heap, -x)
        
        for i in range(k, len(arr)):
            if arr[i] < -heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, -arr[i])
        return [-val for val in heap]
```

#### 复杂度分析

* 时间复杂度：O(nlogk)
* 空间复杂度：O()






