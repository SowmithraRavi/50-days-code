class Solution:
    
    def Sorted(self, s):
        def find(s,i,j):
            if i==j:
                return 
            if s[i]>s[i+1]:
                s[i],s[i+1]=s[i+1],s[i]
            find(s,i+1,j)
            return 
        
        for i in range(n):
            find(s,0,n-i-1)
