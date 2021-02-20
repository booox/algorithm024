# 74. 搜索二维矩阵: 

[74. 搜索二维矩阵](https://leetcode-cn.com/problems/search-a-2d-matrix/)

```
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。

示例 1：

输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true
示例 2：


输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false
 

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
```
## 方法 1: 先将二维转为一维，再用二分查找

### 思路

* 这样的确有些绕远了，增加了时间与空间复杂度，但也不失为一种很容易想到的方法

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # use binary search
        # 1. 将二维矩阵变成一给矩阵，而后使用二分查找
        nums = [n for row in matrix for n in row]

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return False
```

### 复杂度分析

* 时间复杂度：O(logmn + ?)
    * 时间复杂度由两部分组成
        * 二维到一维的时间
        * 二分查找的时间
* 空间复杂度：O(n)


## 方法 2: 直接用二分查找

### 思路

* 不要把给定数组看成二维，而是一维数组，那就可以直接用「二分查找」了
* 只是要把虚拟的一维数组的索引，转变为二维数组的索引
    * `nums[mid]` --> `matrix[mid // n][mid % n]`
        * `m`, `n` 为 matrix 的行数与列数

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 2. 直接使用二分查找
        m, n = len(matrix), len(matrix[0])
        if m == 1 and n == 1:
            return matrix[0][0] == target

        low, high = 0, m * n - 1
        while low <= high:
            mid = low + ((high - low) >> 1)
            curr = matrix[mid // n][mid % n]

            if curr == target:
                return True
            elif curr > target:
                high = mid - 1
            else:
                low = mid + 1

        return False
```

### 复杂度分析

* 时间复杂度：O(logmn)
    * m: matrix 的行数
    * n: matrix 的列数
* 空间复杂度：O( 1)
