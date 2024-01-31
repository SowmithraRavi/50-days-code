class Solution:
    def pattern(self, N):
        l=[]
        m=N
        while(N>0):
            l.append(N)
            N=N-5
        l.append(N)
        n=N
        while(n!=m):
            n=n+5
            l.append(n)
        return l
        
