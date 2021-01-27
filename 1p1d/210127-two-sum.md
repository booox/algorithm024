
# 1. 两数之和

[1. 两数之和](https://leetcode-cn.com/problems/two-sum/)

## 解法

* 使用哈希表 


```
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

你可以按任意顺序返回答案。

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]
 

提示：

2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案
```


## Python

### 方法 1：使用哈希表 + range

#### 思路

* 如何通过嵌套循环来判断是否存在对应的值，时间复杂度至少会 O(n^2)
* 为了减少时间复杂度，可以 **用空间来换时间** 的思想
* 使用辅助的 **哈希表** 
*   key：  当前元素对应补数 (target - n)
*   value：当前元素对应索引 

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                return [d[nums[i]], i]
            else:
                d[target - nums[i]] = i
```


#### 复杂度分析

* 时间复杂度：O(n) 一次遍历
* 空间复杂度：O(n)

### 方法 2：使用哈希表 + enumerate

#### 思路

* 还是使用了哈希表，只是不再使用 `range`，而是使用 `enumerate`
* 比上面代码更简洁了，时间复杂度没有变化。 

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            if n in d:
                return [d[n], i]
            else:
                d[target - n] = i
```


#### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(n)


## Go

### 方法 1：使用哈希表 + range

#### 思路

* 与上述思路一样，只是将它翻译成对应的 Go 代码


```go
func twoSum(nums []int, target int) []int {
    d := make(map[int]int)

    for i, n := range nums {
        if _, ok := d[target - n]; ok {
            return []int {d[target - n], i}
        } else {
            d[n] = i
        }
    }
    return nil
}
```

#### 其它

* 一个月前学写的 Go 代码，忘得差不多了
