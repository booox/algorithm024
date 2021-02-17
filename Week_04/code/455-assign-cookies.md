# 455. 分发饼干: 

[455. 分发饼干](https://leetcode-cn.com/problems/assign-cookies/description/)

```
假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。

对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j] 。如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。

示例 1:

输入: g = [1,2,3], s = [1,1]
输出: 1
解释: 
你有三个孩子和两块小饼干，3个孩子的胃口值分别是：1,2,3。
虽然你有两块小饼干，由于他们的尺寸都是1，你只能让胃口值是1的孩子满足。
所以你应该输出1。
示例 2:

输入: g = [1,2], s = [1,2,3]
输出: 2
解释: 
你有两个孩子和三块小饼干，2个孩子的胃口值分别是1,2。
你拥有的饼干数量和尺寸都足以让所有孩子满足。
所以你应该输出2.

提示：

1 <= g.length <= 3 * 104
0 <= s.length <= 3 * 104
1 <= g[i], s[j] <= 231 - 1
```
## 方法 1: 使用贪心算法

### 思路

* 要「尽可能满足越多数量的孩子」，当把刚好能满足孩子的胃口的饼干发给孩子时，这样饼干才不会浪费
* 对饼干与孩子分别进行排序
* 使用双指针：
    * 在孩子数量 `child` 与饼干数量 `cookie` 都小于给定数量时，执行下面循环
        * 如果 `s[cookie] >= g[child]` ，则满足的孩子数量加 1
        * 不论是否满足，饼干的计数都要增加

**Python**

```python
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        child, cookie = 0, 0
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                child += 1
            cookie += 1

        return child
```

**Go**

```golang
import (
    "sort"
)

func findContentChildren(g []int, s []int) int {
    sort.Ints(g)
    sort.Ints(s)

    child, cookie := 0, 0
    for ; child < len(g) && cookie < len(s); {
        if s[cookie] >= g[child] {
            child++
        }
        cookie++
    }
    return child
}
```


### 复杂度分析

* 时间复杂度：O(mlogm + nlogn)
    * m, n 分别为 g, s 的长度
    * 对两个数组排序的时间复杂度是 O(mlogm+nlogn)，
    * 遍历数组的时间复杂度是 O(m+n)
* 空间复杂度：O(logm+logn)
    * 空间复杂度主要是排序的额外空间开销。