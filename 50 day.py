class Solution:
   
    def mergeKArrays(self, arr, K):
        merged = []
        for row in arr:
            merged.extend(row)
        
       
        merged.sort()
        
        return merged
       
