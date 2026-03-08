'''
Question No. : 141
Title : Linked List Cycle
Difficulty : Easy

Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.
'''

def hasCycle(head : list) -> bool:
    if not head:
        return False
    current = head
    seen = set()

    while current:
        if current in seen:
            return False
        seen.add(current)
        current = current.next
    return True

head  = [3, 2, 0, -4]
print(hasCycle(head))