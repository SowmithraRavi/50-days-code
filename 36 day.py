class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        i=0
        j=1
        ans=0
        while(i<n and j<n):
            if(nums[j]-nums[i]==k):
                ans+=1
                j+=1
            elif(nums[j]-nums[i]>k):
                i+=1
            else:j+=1
            if(i==j):
                j+=1
            else:
                while(j<n and nums[j]==nums[j-1]):
                    j+=1
        return ans
        
