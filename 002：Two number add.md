002：Two number add

---

## Problem Description

给出两个 **非空** 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 **逆序** 的方式存储的，并且它们的每个节点只能存储 **一位** 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

**示例：**

```
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
```

## Problem Solving

使用链表保存数据，循环遍历即可。

## Python solution

```python
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        up = 0
        root = head = ListNode(0)
        while l1 or l2 or up:
            l1, val1 = [l1.next, l1.val] if l1 else [0, 0]
            l2, val2 = [l2.next, l2.val] if l2 else [0, 0]
            up,down = divmod(val1+val2+up, 10)
            head.next = ListNode(down)
            head = head.next
        return root.next

```

## C++ solution

```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

class Solution
{
  public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {
        ListNode *head,*p;
        head=p=new ListNode(0);
        int fullFlag = 0;
        while (l1 != NULL || l2 != NULL ||fullFlag){
            int val1=(l1==NULL)?0:l1->val;
            int val2=(l2==NULL)?0:l2->val;
            
            p=p->next = new ListNode((val1 + val2 + fullFlag)%10);
            fullFlag=(val1 + val2 + fullFlag)/10;
            
            if(l1)l1=l1->next;
            if(l2)l2=l2->next;
        }
        return head->next;
    }
};
```

## Java solution

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head,p;
        head=p=new ListNode(0);
        int carry=0;
        while(l1!=null||l2!=null||carry>0){
            int val1=(l1==null)?0:l1.val;
            int val2=(l2==null)?0:l2.val;
            l1=l1!=null?l1.next:null;
            l2=l2!=null?l2.next:null;
            int sum=val1+val2+carry;
            p=p.next=new ListNode((sum)%10);
            carry=(sum)/10;
            
        }
        return head.next;
    }
}
```

