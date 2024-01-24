class Solution:
    def isPerfectNumber(self, N):
        temp=N
        sum=0
        for i in range(1,N):
            if N%i==0:
                sum+=i
          
        if temp==sum:
            return 1
        else:
            return 0
