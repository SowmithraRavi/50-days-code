
class Solution:
    def tour(self,lis, n):
        start = 0
        capacity = 0
        defi = 0
        for i in range(n):
            petrol = lis[i][0]
            dist = lis[i][1]
            capacity += petrol - dist
            if capacity < 0:
                start = i + 1
                defi += capacity
                capacity = 0
                
        if capacity + defi >=0:
            return start
        return -1
      
