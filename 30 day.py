class Solution:    
    def pairWiseSwap(self, head):
        if not head or not head.next:
            return head
        dummy = Node(0)  
        dummy.next = head
        prev = dummy

        while head and head.next:
            first = head
            second = head.next
            prev.next = second
            first.next = second.next
            second.next = first
            prev = first
            head = first.next

        return dummy.next
