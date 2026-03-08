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
