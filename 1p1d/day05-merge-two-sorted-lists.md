
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

* 终止条件：当两个链表都为空时，表示链表已经完成合并。
* 调用递归：先判断 l1 与 l2 头结点哪个更小，然后较小结点的 `next` 指针指向 **其余结点的合并结果**。
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




如何计算递归的时间复杂度和空间复杂度呢？

时间复杂度可以这样计算：

> 给出一个递归算法，其时间复杂度 {\mathcal{O}(T)}O(T) 通常是递归调用的数量（记作 {R}R） 和计算的时间复杂度的乘积（表示为 {\mathcal{O}(s)}O(s)）的乘积：O(T)=R∗O(s)



m, n 分别为 l1 与 l2 的节点个数。

* 时间复杂度：O(m+n)

m，n 为 l1 和 l2 的元素个数。递归函数每次去掉一个元素，直到两个链表都为空，因此需要调用 `R=O(m + n)` 次。而在递归函数中我们只进行了 `next` 指针的赋值操作，复杂度为 `O(1)`，故递归的总时间复杂度为 `O(T)=R∗O(1)=O(m+n)`  。

* 空间复杂度：O(m+n)

对于递归调用 `self.mergeTwoLists()`，当它遇到终止条件准备回溯时，已经递归调用了 `m+n` 次，使用了 `m+n` 个栈帧，故最后的空间复杂度为 `O(m+n)`。

作者：z1m
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists/solution/yi-kan-jiu-hui-yi-xie-jiu-fei-xiang-jie-di-gui-by-/
来源：力扣（LeetCode）

