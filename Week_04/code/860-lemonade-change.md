# 860. 柠檬水找零: 

[860. 柠檬水找零](https://leetcode-cn.com/problems/lemonade-change/)

```
在柠檬水摊上，每一杯柠檬水的售价为 5 美元。

顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。

每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。

注意，一开始你手头没有任何零钱。

如果你能给每位顾客正确找零，返回 true ，否则返回 false 。

示例 1：

输入：[5,5,5,10,20]
输出：true
解释：
前 3 位顾客那里，我们按顺序收取 3 张 5 美元的钞票。
第 4 位顾客那里，我们收取一张 10 美元的钞票，并返还 5 美元。
第 5 位顾客那里，我们找还一张 10 美元的钞票和一张 5 美元的钞票。
由于所有客户都得到了正确的找零，所以我们输出 true。
示例 2：

输入：[5,5,10]
输出：true
示例 3：

输入：[10,10]
输出：false
示例 4：

输入：[5,5,10,10,20]
输出：false
解释：
前 2 位顾客那里，我们按顺序收取 2 张 5 美元的钞票。
对于接下来的 2 位顾客，我们收取一张 10 美元的钞票，然后返还 5 美元。
对于最后一位顾客，我们无法退回 15 美元，因为我们现在只有两张 10 美元的钞票。
由于不是每位顾客都得到了正确的找零，所以答案是 false。
 

提示：

0 <= bills.length <= 10000
bills[i] 不是 5 就是 10 或是 20 
```
## 方法 1: 贪心算法

### 思路

* *这题初看起来还比较简单，但其中却包含了典型的「贪心思想」
* 要能给每位顾客正确的找零，其实也就是让手头的零钱，能够找最多的顾客
* 涉及到的钞票面额共有 `[20, 10, 5]` 三种
* 需要注意的是：**这三种面额有整除关系**，这也是适用 **贪心** 的要求
    * 为什么？因为，如果 20 可以找，那用 10 或 5 也是可以的，且用 20 的，也会在最大概率上可以够找下面的顾客
    * 这与生活的常识是吻合的。

**Python**

```python
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for n in bills:
            if n == 5:
                five += 1
            elif n == 10:
                if five > 0:
                    ten += 1
                    five -= 1
                else:
                    return False
            elif n == 20:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
```

**Go**

```go
func lemonadeChange(bills []int) bool {
    five, ten := 0, 0
    for _, n := range bills {
        if n == 5 {
            five += 1
        } else if n == 10 {
            if five > 0 {
                ten += 1
                five -= 1
            } else {
                return false
            }
        } else if n == 20 {
            if ten > 0 && five > 0 {
                ten -= 1
                five -= 1
            } else if five >= 3 {
                five -= 3
            } else {
                return false
            }
        }
    }
    return true
}


```

### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(1)
