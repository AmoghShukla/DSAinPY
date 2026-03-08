'''
Question Number : 142. 
Title : Linked List Cycle II
Difficulty : Medium

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
Do not modify the linked list.

Example :

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
'''


def detectCycle(head : list):
    current = head

    visited = set()
    while current:
        if current not in visited:
            visited.add(current)
            current = current.next
        elif current in visited:
            return current
        else:
            return -1

head = [3,2,0,-4]
print(detectCycle(head))

