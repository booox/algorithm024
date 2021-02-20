# 154. 寻找旋转排序数组中的最小值 II: 

[154. 寻找旋转排序数组中的最小值 II](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/)

```
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

注意数组中可能存在重复的元素。

示例 1：

输入: [1,3,5]
输出: 1
示例 2：

输入: [2,2,2,0,1]
输出: 0
说明：

这道题是 寻找旋转排序数组中的最小值 的延伸题目。
允许重复会影响算法的时间复杂度吗？会如何影响，为什么？
```
## 方法 1: 使用二分查找

### 思路

* 与 [153. 寻找旋转排序数组中的最小值](code/153-find-minimum-in-rotated-sorted-array.md) 方法类似
* 不同之处在于如何处理 **重复元素**
    * 当找到重复元素的时候，可以把 `low` 向右移到一位后，再继续用 **二分查找**
    * 这里就有点像遍历了，如果整个数组全部为重复的，则整体时间复杂度会退化为 `O(n)`
* 还有一点需要注意，就是最后的返回值
    * 查找到最后, 会找到一个递增的区间，为 `nums[low] <= nums[high]`，此时只需要返回 `nums[low]` 即可
    * 但，如果 low 与 high 两者对应的元素值相等的话，则会出现问题
    * 此时，判断的条件修改为：`nums[low] < nums[high] or low == high`

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + ((high - low) >> 1)
            # 遇到递增的区间，或所剩区间只有一个元素，直接返回
            if nums[low] < nums[high] or low == high:
                return nums[low]
            
            # low --> mid 
            if nums[low] == nums[mid]:
                low += 1
                continue

            # low --> mid 为递增，则最小值肯定不在这个区间
            elif nums[low] < nums[mid]:
                low = mid + 1
            else:
                high = mid   # mid 也可能是最小的
```

### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()
