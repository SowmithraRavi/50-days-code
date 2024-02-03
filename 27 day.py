def reverseList(self, head):
        prev = None
        current = head

        for i in range(n):
            nex = current.next
            current.next = prev
            prev = current
            current = nex

        return prev
