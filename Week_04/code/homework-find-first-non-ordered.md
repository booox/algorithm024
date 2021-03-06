

# 查找旋转数组第一个无序位置: 

## 方法 1: 使用二分查找

### 思路

* 假设数组为 `[0, 1, 2, 4, 5, 6, 7]`，现在数组经旋转后变为 `[4, 5, 6, 7, 0, 1, 2]`
* 那第 1 个无序的位置即 `0` 的位置，其实也就是数组中的 **最小值**
* 那这个问题就变成下面两种情况
    * [153. 寻找旋转排序数组中的最小值](153-find-minimum-in-rotated-sorted-array.md) 
    * [154. 寻找旋转排序数组中的最小值 II](154-find-minimum-in-rotated-sorted-array-ii.md) （数组内元素可能会重复）

