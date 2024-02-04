class Solution:
    def union(self, head1,head2):
        uni = set()
        cur = head1
        while cur:
            uni.add(cur.data)
            cur = cur.next
        cur = head2
        while cur:
            uni.add(cur.data)
            cur = cur.next
        h=t=None
        for i in sorted(uni):
            if h==None:
                h=t=Node(i)
            else:
                t.next=Node(i)
                t=t.next
        return h

      
