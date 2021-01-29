
# 21. 合并两个有序链表

[21. 合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/)

```
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例 1：

输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
示例 2：

输入：l1 = [], l2 = []
输出：[]
示例 3：

输入：l1 = [], l2 = [0]
输出：[0]

提示：

两个链表的节点数目范围是 [0, 50]
-100 <= Node.val <= 100
l1 和 l2 均按 非递减顺序 排列
```


## Python

### 方法 1：使用哨兵 + 一次遍历

#### 思路

* 原有的两个链表已为有序链表
    * 则可以考虑设置每次从两个链表中各拿出一个进行比较
    * 值较小的先记录下来，并再取值较小元素对应链表的下一个元素进行比较
    * 重复此操作，直到一个链表所有元素被取完

```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        sentinel = ListNode(0)
        curr = sentinel

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 if l1 else l2
        return sentinel.next
```


#### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(n)

### 方法 2：使用递归

#### 思路

* 参考：[一看就会，一写就废？详解递归](https://leetcode-cn.com/problems/merge-two-sorted-lists/solution/yi-kan-jiu-hui-yi-xie-jiu-fei-xiang-jie-di-gui-by-/)

```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1

        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
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
