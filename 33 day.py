#User function Template for python3
class Solution:
    def InfixtoPostfix(self, exp):
        result = []
        stack = []
        for i in range(len(exp)):
            c = exp[i]
            if ('a'<=c<='z') or ('A'<=c<='Z') or ('0'<=c<='9'):
                result.append(c)
            elif c == '(':
                stack.append(c)
            elif c == ')':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop()
            else:
                while stack and (self.precedence(stack[-1]) >= self.precedence(exp[i]) or (self.precedence(stack[-1]) == self.precedence(exp[i]) and self.associativity(exp[i]) == 'L')):
                    result.append(stack.pop())
                stack.append(c)
        while stack:
            result.append(stack.pop())
        return ''.join(result)
    def precedence(self,c):
        if c == '+' or c == '-':
            return 1
        elif c == '*' or c == '/':
            return 2
        elif c == '^':
            return 3
        else:
            return -1
    def associativity(self,c):
        if c == '^':
            return 'R'
        return 'L'






