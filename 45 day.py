class Solution:
    def maxLength(self, S):
        max_length = 0
        stack = []
        stack.append(-1)

        for i in range(len(S)):
            if S[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])

        return max_length
 
