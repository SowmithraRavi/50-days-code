class Solution:   
    def peakElement(self,arr, n):
        n=max(arr)
        h=arr.index(n)
        return h

another solution
class Solution:   
    def peakElement(self,arr, n):
        low=0
        high=n-1
        while low<=high:
            mid=low+(high-low)//2
            if (mid==0 or arr[mid-1]<=arr[mid])and(mid==n-1 or arr[mid+1]<=arr[mid]):
                return mid
            elif mid>0 and arr[mid-1]>arr[mid]:
                high=mid-1
            else:
                low=mid+1
        return 0
