stack = []

stack.append("mon")
stack.append("tue")
stack.append("wed")
print("initial stack:",end = " ")
print(stack)
print(stack.pop())
print("top of the stack:",end=" ")
print(stack[-1])
print(stack.pop())
print(stack.pop())
print("stack after popped:",end = " ")
print(stack)