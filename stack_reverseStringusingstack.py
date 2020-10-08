def createStack():
    stack = []
    return stack

def push(stack,item):
    stack.append(item)

def pop(stack):
    if isEmpty(stack):
        return
    return stack.pop()

def isEmpty(stack):
    if len(stack) == 0:
        return True

def reverse(string):
    n = len(string)

    stack = createStack()

    for i in range(0,n):
        push(stack,string[i])

    string=""
    for i in range(0,n):
        string +=pop(stack)
    return string



string = "programming"
string = reverse(string)
print("reversed string is " +string)