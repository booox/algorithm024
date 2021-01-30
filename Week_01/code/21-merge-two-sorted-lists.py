# 题 目：21. 合并两个有序链表
# 链 接：https://leetcode-cn.com/problems/merge-two-sorted-lists/
# 描 述：将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # # 1. 使用哨兵，通过一次遍历，判断两个有序链表头结点对应值的大小
        # sentinel = ListNode(0)
        # curr = sentinel

        # while l1 and l2:
        #     if l1.val <= l2.val:
        #         curr.next = l1
        #         l1 = l1.next
        #     else:
        #         curr.next = l2
        #         l2 = l2.next
        #     curr = curr.next

        # curr.next = l1 if l1 else l2

        # return sentinel.next


        # 2. 使用递归
        # 终止条件：若两个链表都为空，则完成合并
        # 使用递归：先比较 l1 与 l2 哪个小，接着将较小的节点的 `next` 指向 **其余节点的合并结果**
        if not l1: return l2
        if not l2: return l1

        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        