from typing import List, Optional

class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value  # 存储节点的值
        self.next = next  # 指向下一个节点的引用

class Solution:
    # l1 和 l2 为当前遍历的节点，carry 为进位
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
        if l1 is None and l2 is None:  # 递归边界
            return ListNode(carry) if carry else None  # 如果进位了，就额外创建一个节点
        if l1 is None:  # 如果 l1 是空的，那么此时 l2 一定不是空节点
            l1, l2 = l2, l1  # 交换 l1 与 l2，保证 l1 非空，从而简化代码
        s = carry + l1.val + (l2.val if l2 else 0)  # 节点值和进位加在一起
        l1.val = s % 10  # 每个节点保存一个数位（直接修改原链表）
        l1.next = self.addTwoNumbers(l1.next, l2.next if l2 else None, s // 10)  # 进位
        return l1
s=Solution()

l1 = ListNode(2)
print(f"l1 1:{l1.val},{l1.next}")
l1.next = ListNode(4)
print(f"l1 2:{l1.val},{l1.next}")
l1.next.next = ListNode(3)
print(f"l1 3:{l1.val},{l1.next}")
while l1:
    # print(f"l1:{l1.val},{l1.next}")
    print(l1.val, end=" -> " if l1.next else "\n")
    l1 = l1.next

# 构建 l2: 5 -> 6 -> 4
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

res = s.addTwoNumbers(l1, l2)
print(res)
# 打印结果
while res:
    print(res.val, end=" -> " if res.next else "\n")
    res = res.next
# 输出: 7 -> 0 -> 8