class Solution:
    def search(self, patt, s):
        ans=[]
        ind=0
        while ind<len(s):
            ind=s.find(patt,ind)
            if ind==-1:
                break
            ans.append(ind+1)
            ind+=1
        if ans:
            return ans
        else:
            ans.append(-1)
            return ans
