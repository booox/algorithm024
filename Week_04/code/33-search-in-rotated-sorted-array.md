# 33. 搜索旋转排序数组: 

[33. 搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/)

```
升序排列的整数数组 nums 在预先未知的某个点上进行了旋转（例如， [0,1,2,4,5,6,7] 经旋转后可能变为 [4,5,6,7,0,1,2] ）。

请你在数组中搜索 target ，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

示例 1：

输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4
示例 2：

输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1
示例 3：

输入：nums = [1], target = 0
输出：-1

提示：

1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
nums 中的每个值都 独一无二
nums 肯定会在某个点上旋转
-10^4 <= target <= 10^4
```
## 方法 1: 调用库函数

### 思路

* `nums.count(target)` 查看目标是否存在数组中
* `nums.index(target)` 查看目标在数组中的索引

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1. use python list func
        return nums.index(target) if nums.count(target) else -1
```

### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()


## 方法 2: 暴力遍历查找

### 思路

* 从头遍历数组，暴力查找目标，找到目标直接返回索引；没有找到返回 -1

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # # 2. 暴力遍历查找
        for i, n in enumerate(nums):
            if n == target:
                return i
        return -1
```

### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(1)

## 方法 3: 使用二分查找

### 思路

* 与通用二分查找有所不同，因为数组 `nums` 不是 **单调有序** 的
* 但还是有规律可循的：
    * 可以根据 `nums[mid]` 与 `nums[low]` 进行比较，可以得到 `mid` 位于左段还是右段，更直接来说，是 **较大的数** 还是 **较小的数** 
    * 确定 `mid` 位置之后，然后在每一段里，再根据 `target` 与 `mid` 位置，来更新 `low` 与 `high` 的值，直到找到 target 或没有找到退出循环。


```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 4. 二分查找
        # # nums[mid] == target，直接返回 mid
        # # 先对 nums[mid] 与 nums[low] 进行比较，确定 mid 在左段还是右段
        # # 而后在每一段，比较 mid 与 target 位置
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            # 确定 mid 在左段，还是右段
            ## mid 在左段 （较大的数 + 可能较小的数）
            if nums[mid] >= nums[low]:  
                ## 比较 mid 与 target 位置
                ### low -- target -- mid
                if nums[low] <= target < nums[mid]:
                # if target < nums[mid]:
                    high = mid - 1
                ### mid -- target -- high
                else:
                    low = mid + 1
            ## mid 在右段 (可能较大的数 + 较小的数 )
            else:  
                ## 比较 mid 与 target 位置
                ### mid -- target -- high
                if nums[mid] < target <= nums[high]:
                # if nums[mid] < target:
                    low = mid + 1
                ### low -- target -- mid
                else:
                    high = mid - 1

        return -1
```

### 复杂度分析

* 时间复杂度：O(logn)
* 空间复杂度：O(1)



## 方法 4: 将数组复原变成单调有序数组，再二分查找 (未通过)

### 思路

* 

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 3. 复原变成单调有序数组，再二分查找
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        # 保存旋转后数组对应索引
        d = {}
        for i, n in enumerate(nums):
            d[n] = i

        # 找到旋转位置，复原数组
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                j = i
                break
        nums = nums[j:] + nums[:j]
        print(nums)

        # 二分查找 target 新的位置
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return d[nums[mid]]
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1
```

### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()

