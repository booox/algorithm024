
# 88. 合并两个有序数组

[88. 合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array/)

```
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。

 

示例 1：

输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
示例 2：

输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
```


## Python

### 方法 1：暴力解法

#### 思路

* 先将两个数组合并，再排序 

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] + nums2)
```


#### 复杂度分析

* 时间复杂度：O((m+n)log(m+n))
    * 在 Python 中 `sorted` 排序的时间复杂度可以达到 `O(nlogn)`
    * 这里 `n` 为数组长度，本题中长度为 `m+n`
* 空间复杂度：O(1)

#### 问题与优化

* 要注意 `nums1[:]` 的写法，是为了保证在数组 **原地** 操作
* 没有利用原有数组 **已排序** 的条件，浪费了不少的操作

### 方法 2：双指针 start->end

#### 思路

* 对于已排序的数组合并，可以用 **双指针** 分别指向两个数组对应的元素
* 比较大小，向移动值较小的指针
* 因为结果要放在 `nums1` 中，所以要将 `nums1` 中前面真正的数据部分先复制出来
    * 就像整理书桌一样，可以先将书桌上所有的东西先移到另一个盒子里
    * 然后再逐一整理，放回书桌适当的位置，也包括需要新添的东西
* 实际写代码时，可以使用 **三指针**，代码会容易写一些

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 特判
        if not nums2: return nums1

        # make a copy of nums1 data
        nums1_copy = nums1[:m]

        p, p1, p2 = 0, 0, 0
        while p1 < m and p2 < n:
            if nums1_copy[p1] <= nums2[p2]:
                nums1[p] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1
            p += 1

        if p1 < m:
            nums1[p:] = nums1_copy[p1:]
        elif p2 < n:
            nums1[p:] = nums2[p2:]
```


#### 复杂度分析

* 时间复杂度：O(m+n)
    * 对于有序数组，通过 **双指针** 方法，可以达到 `O(m+n)` 的时间复杂度
* 空间复杂度：O(m)

#### 问题与优化

* 因为需要将 `nums1` 中的数据移动，所以额外使用了 `m` 的空间
* 能否对这一点进行优化呢？


### 方法 3：双指针 end -> start

#### 思路

* 对于已排序的数组合并，可以用 **双指针** 分别指向两个数组对应的元素
* 在 `nums1` 的后面是没有数据的，能否从后往前，每次将最大的值放入呢
    * 这样就不需要事先搬运数据了，从而降低了空间复杂度

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 特判
        if not nums2: return nums1

        # 3. 三指针：后->前
        p, p1, p2 = m + n - 1, m - 1, n - 1

        while p1 > -1 and p2 > -1:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        
        # if p1 > -1:   # 可以省略，因为最后要看的就是 nums1，数据不用动
        #     nums1[:p+1] = nums1[:p1+1]
        if p2 > -1:
            nums1[:p+1] = nums2[:p2+1]
```


#### 复杂度分析

* 时间复杂度：O(m+n)
    * 对于有序数组，通过 **双指针** 方法，可以达到 `O(m+n)` 的时间复杂度
* 空间复杂度：O(1)
