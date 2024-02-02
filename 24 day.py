class Solution:
    def solve(self,n,k,stalls):
        stalls.sort()
        res = -1
        low = 0
        high = stalls[n - 1] - stalls[0]

        while low <= high:
            mid = (low + high) // 2
            if self.cow(mid, stalls, k, n):
                res = mid
                low = mid + 1
            else:
                high = mid - 1

        return res if res != -1 else None


    def cow(self,mid, stalls, k, n):
        low = stalls[0]
        count = 1

        for i in range(1, n):
            if stalls[i] - low >= mid:
                low = stalls[i]
                count += 1

        return count >= k
       
