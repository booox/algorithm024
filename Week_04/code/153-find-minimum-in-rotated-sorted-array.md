# 153. 寻找旋转排序数组中的最小值: 

[153. 寻找旋转排序数组中的最小值](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/)

```
假设按照升序排序的数组在预先未知的某个点上进行了旋转。例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] 。

请找出其中最小的元素。

示例 1：

输入：nums = [3,4,5,1,2]
输出：1
示例 2：

输入：nums = [4,5,6,7,0,1,2]
输出：0
示例 3：

输入：nums = [1]
输出：1
 

提示：

1 <= nums.length <= 5000
-5000 <= nums[i] <= 5000
nums 中的所有整数都是 唯一 的
nums 原来是一个升序排序的数组，但在预先未知的某个点上进行了旋转
```
## 方法 1: 二分查找

### 思路

* 参考题解：[一文解决 4 道「搜索旋转排序数组」题！](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/solution/yi-wen-jie-jue-4-dao-sou-suo-xuan-zhuan-pai-xu-s-3/)
* 本题中元素均为唯一，没有重复
* 假设数组为 `[0, 1, 2, 4, 5, 6, 7]`，现在数组经旋转后变为 `[4, 5, 6, 7, 0, 1, 2]`
    * 原来数组是依次 **递增** ，而现在数组则变成 先**递增**，再**递减**
* 使用二分查找，要清楚如何收缩区间?
    * 如果 `nums[low] <= nums[mid]`，则说明从 `low --> mid` 之间元素为递增，那最小值肯定不在这个区间 
        * 那就把前面排除掉，所以 `low = mid + 1`
    * 否则 `nums[low] > nums[mid]`，则说明已经从 **递增** 区间，过渡 **递减** 区间了，那最小值肯定就在这个区间
        * 按照二分查找的思路，应该把后面的排除掉，即 `high = mid - 1`
        * 但我们并不清楚，`mid` 是不是最小的，不能直接去掉，所以只能是 `high = mid`
* 那什么时候返回 **最小值** 呢？
    * 当 `low` 与 `high` 逐渐收缩到一个 **递增** 区间，即上面旋转后数组的 `[..., 0, 1, 2]` 部分时
    * 直接返回最左边的元素即可，即 `nums[low]`

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # 使用二分查找
        low, high = 0, len(nums) - 1
        while low <= high:
            # 收敛到一个区间，nums[low] <= nums[high]
            # 说明这个区间，为递增，直接返回最左边元素，即 nums[low]
            if nums[low] <= nums[high]:
                return nums[low]

            mid = low + (high - low) // 2
            
            # low --> mid 为递增，则 最小值，一定不在此区域
            if nums[low] <= nums[mid]:
                low = mid + 1   # mid 也排除掉了
            # low --> mid 不是连续的，则最小值一定在这里
            else:
                high = mid      # mid 也有可能是最小的
```

### 复杂度分析

* 时间复杂度：O(logn)
* 空间复杂度：O(1)
