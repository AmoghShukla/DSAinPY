'''
Question No : 21
Title : Merge Two Sorted Lists
Difficulty : Easy
Merge two sorted linked lists and return it as a new sorted list. 
The new list should be made by splicing together the nodes of the first two lists.

Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def MergeLists(List1 , List2):
    if not List1:
        return List2
    if not List2:
        return List1
    
    current1 = List1
    current2 = List2

    dummy = ListNode()
    current = dummy

    while current1 and current2:
        if current1.val < current2.val:
            current.next = current1
            current1 = current1.next
        else:
            current.next = current2
            current2 = current2.next
        current = current.next

    if current1:
        current.next = current1
    if current2:
        current.next = current2

    return dummy.next

l1 = [1,2,4]
l2 = [1,3,4]

print(MergeLists(l1, l2))