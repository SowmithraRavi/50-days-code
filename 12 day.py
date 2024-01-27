class Solution:
   
    def minRow(self,N,M,A):
        mi=M
        ind=0
        for i  in range(N):
            S=A[i].count(1)
            if mi>S:
                mi=S
                ind=i
        return ind+1
