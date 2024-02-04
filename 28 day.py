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

another solution:
class Solution:
    def union(self, head1,head2):
        s=set()
        temp1=head1
        temp2=head2
        while temp1:
            s.add(temp1.data)
            temp1=temp1.next
        while temp2:
            s.add(temp2.data)
            temp2=temp2.next
        s=list(sorted(s))
        newnode=Node(-1)
        temp=newnode
        for i in s:
            temp.next=Node(i)
            temp=temp.next
        return newnode.next

      
