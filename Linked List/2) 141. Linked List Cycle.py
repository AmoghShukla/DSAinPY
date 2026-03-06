def hasCycle(head : ListNode) -> bool:
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