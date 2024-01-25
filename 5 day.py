class Solution:
    def yShapedPattern(self, N):
        half=N//2
        result=''
        for i in range(half):
            left=" "*i
            mid=" "*(N-2-(2*i)+1)
            string=left+"*"+mid+"*"+"\n"
            result+=string
        for j in range(half-1):
            left=" "*(N//2)
            result+=(left+"*"+"\n")
        result+=(" "*(N//2)+"*")
        return result
