def Push(x,stack1,stack2):
    stack1.append(x)
    return stack1, stack2

def Pop(stack1,stack2):
    if not stack2:
        while stack1:
            stack2.append(stack1.pop())
    
    if not stack2:
        return -1
    return stack2.pop()
