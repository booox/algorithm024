# 81. 搜索旋转排序数组 II: 

[81. 搜索旋转排序数组 II](https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/)

```
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

示例 1:

输入: nums = [2,5,6,0,0,1,2], target = 0
输出: true
示例 2:

输入: nums = [2,5,6,0,0,1,2], target = 3
输出: false
进阶:

这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？

```
## 方法 1: 部分使用二分查找

### 思路

* 参考题解：[一文解决 4 道「搜索旋转排序数组」题！](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/solution/yi-wen-jie-jue-4-dao-sou-suo-xuan-zhuan-pai-xu-s-3/)
* 本题与 [33. 搜索旋转排序数组](code/33-search-in-rotated-sorted-array.md) 类似，只是多了一个重复的可能性
* 在进行二分查找时，逻辑是一样的
    * 如果 `nums[mid] == target` ，则直接返回
    * 接着判断 `nums[mid]` 与 最左边元素 `nums[low]` 之间关系
        * 如果 `nums[low] == nums[mid]`，就让 low 向右移动一步
        * 如果 `nums[low] < nums[mid]`，说明 `low --> mid` 之间元素为 **递增**
            * 再判断 `nums[low] <= target < nums[mid]` 是否成立，这表明 target 在 mid 的左边，high 要向左移
            * 否则，low 要向右移
        * 如果 `nums[low] > nums[mid]`，说明 `mid --> high` 之间元素为 **递增**
            * 再判断 `nums[mid] < target <= nums[high]` 是否成立，这表明 target 在 mid 的右边，low 要向右移
            * 否则，high 要向左移

```python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        # use binary search

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return True

                        
            # low --> mid 相等，这一部分没有办法用二分查找了。
            if nums[low] == nums[mid]:
                low += 1
                continue
            # low --> mid 为递增
            elif nums[low] < nums[mid]:
                # target 在 mid 左边
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # mid --> high 为递增
            else:
                # target 在 mid 的右边
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False

```

### 复杂度分析

* 时间复杂度：O(logn + m)
    * n 为 nums 长度，m 为 相等元素的个数
* 空间复杂度：O(1)
