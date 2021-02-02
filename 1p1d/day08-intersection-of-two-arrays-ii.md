# day08: 350. 两个数组的交集 II

[350. 两个数组的交集 II](https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/)

```

```
## Python

### 方法 1: 暴力解法

#### 思路

* 先对两数组排序
* 再使用双层循环，外层为较短数组，内层为较长数组
* 为避免相同数字下次再被添加，使用变量 `idx` 记录上一次添加元素的索引

```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 1. 暴力解法：先对数组排序，遍历短的
        if len(nums2) < len(nums1):
            return self.intersect(nums2, nums1)

        nums1.sort()
        nums2.sort()

        res = []
        idx = -1
        for i, n in enumerate(nums1):
            for j, m in enumerate(nums2):
                if m == n and j > idx:
                    res.append(n)
                    idx = j
                    break
        return res
```

#### 复杂度分析

* 时间复杂度：O(n^2)
    * 排序 O(nlogn) + 循环 O(n^2)
* 空间复杂度：O(n)


### 方法 2: 使用哈希表

#### 思路

* 先排序，将较短数组元素及出现的次数放入哈希表
* 对较长数组进行遍历，判断元素是否存在哈希表中


```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
       if len(nums2) < len(nums1):
            return self.intersect(nums2, nums1)

        nums1.sort()
        nums2.sort()       

        d1, d2 = {}, {}
        for i, n in enumerate(nums1):
            d1[n] = d1.get(n, 0) + 1

        for i, n in enumerate(nums2):
            d2[n] = d2.get(n, 0) + 1

        res = []
        for k, v in d1.items():
            if d2.get(k, 0) > 0:
                res.extend([k] * min(d1[k], d2[k]))  # 会增加空间复杂度
        return res
```

#### 复杂度分析

* 时间复杂度：O(m+n+k)
    * m,n,k 分别为 nums1, nums2, 与 nums1 对应哈希表的长度
* 空间复杂度：O(m+n)

### 方法 3: 哈希表 2

#### 思路

* 先判断长短，处理短的；排序
* 将较短数组元素及出现的次数放入哈希表
* 对较长数组进行遍历，判断数值是否在哈希表中
    * 如果在，则将次数减 1；
    * ~~当次数为 0，则将值从哈希表中删除~~

```python

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 3. use hash table
        if len(nums2) < len(nums1):
            return self.intersect(nums2, nums1)

        nums1.sort()
        nums2.sort()       

        d1 = {}
        for i, n in enumerate(nums1):
            d1[n] = d1.get(n, 0) + 1

        res = []
        for n in nums2:
            if d1.get(n, 0) > 0:
                res.append(n)
                d1[n] -= 1
                # if d1[n] == 0:    # 多此一举了
                #     d1.pop(n)
        return res
```

#### 复杂度分析

* 时间复杂度：O(m+n)
    * m 和 n 分别是两个数组的长度
* 空间复杂度：O(m+n)


### 方法 4: 双指针

#### 思路

* 如果两个数组是有序的，对于有序数组的合并，就可以使用「双指针」
* 通过两个指针，依次遍历所有元素
    * 遇到相等的添加到结果集
    * 遇到不相等，较小的指针向后移动一位

```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        p1, p2 = 0, 0

        nums1.sort()
        nums2.sort()

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1

        return res
```

#### 复杂度分析

> m, n 分别为 nums1, nums2 的长度

* 时间复杂度：O(mlogm + nlogn)
    * 排序：O(mlogm + nlogn); 遍历：O(m + n)
    * 总的时间复杂度：O(mlogm + nlogn) 
* 空间复杂度：O( min(m + n) )
