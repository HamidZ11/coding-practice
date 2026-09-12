
current = head
previous = None

while current:
    temp = current.next
    current.next = previous
    previous = current
    current = temp

