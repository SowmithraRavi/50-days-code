class Solution:
    
    #Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self,a, n):
        n=len(a)
        for i in range(n//2):
            for j in range(i,n-i-1):
                temp=a[i][j]
                a[i][j]=a[j][n-i-1]
                a[j][n-i-1]=a[n-i-1][n-j-1]
                a[n-i-1][n-j-1]=a[n-j-1][i]
                a[n-j-1][i]=temp
