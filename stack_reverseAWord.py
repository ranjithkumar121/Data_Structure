
def reverse(string):
    stack = []
    temp = string.split()

    for i in temp:
        stack.append(i)
    while(len(stack)):
        print(stack.pop(),end=" ")
string = "I LOVE PROGRAMMING"
string = reverse(string)
