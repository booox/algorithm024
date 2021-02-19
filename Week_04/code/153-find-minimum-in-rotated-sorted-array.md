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
* 

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
                high = mid      # mid 也有可能是
```

### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()
