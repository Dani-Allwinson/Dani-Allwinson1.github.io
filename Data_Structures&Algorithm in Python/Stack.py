def create_stack():
    stack=[]
    return stack
def it_empty(stack):
    return len(stack)==0
def push(stack,item):
    stack.append(item)
    print(item)
def pop():
    if it_empty(stack):
        return "Stack is empty"
    else:
        return stack.pop()

stack=create_stack()
print("The folllowing items are pushed into the stack:")
push(stack,str(1))
push(stack,str(2))
push(stack,str(3))
push(stack,str(4))
push(stack,str(5))
push(stack,str(6))

print("popped item: " + pop())
print("popped item: " + pop())
print("popped item: " + pop())
print("stack after popping an element: " + str(stack))
