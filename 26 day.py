class Solution:
    def searchKey(self, n, head, key):
        current = head

        for _ in range(n):
            if current.data == key:
                return 1
            current = current.next

        return 0
