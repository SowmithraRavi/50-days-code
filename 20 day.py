class Solution:
    def nthRowOfPascalTriangle(self,n):
        mod=10**9+7
        if n==1:
            return [1]
        prev=self.nthRowOfPascalTriangle(n-1)
        row=[1]
        for i in range(1,n-1):
            row.append((prev[i-1]+prev[i])%mod)
        row.append(1)
        return row
        
