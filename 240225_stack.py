def create_stack():
    stack = []
    return stack

def is_empty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)

def pop(stack):
    if is_empty(stack):
        return "Stack is empty"
    return stack.pop()

def peek(stack):
    if is_empty(stack):
        return "Stack is empty"
    return stack[-1]

stack = [1,2,3]

stack.append(4)
# print(stack)
stack.append(5)
# print(stack)

stack.pop()
# print(stack)

stack1 = []
print(stack, stack1)
stack1.append(stack.pop()) # 4
print(stack, stack1)
stack.pop() # 3
print(stack, stack1)
stack.append(stack1.pop()) # 4
print(stack, stack1)


# B->C->D->A 순으로 출력
stack_a = ['A','B','C','D']
stack_temp = []
print(stack_a, stack_temp)

stack_temp.append(stack_a.pop())
print(stack_a, stack_temp)

stack_temp.append(stack_a.pop())
print(stack_a, stack_temp)

print(stack_a.pop())
print(stack_a, stack_temp)

# 스택을 다시 넣기
stack_a.append(stack_temp.pop())
print(stack_a, stack_temp)
# print(stack_a[-1])
print(stack_a.pop())

stack_a.append(stack_temp.pop())
print(stack_a, stack_temp)
# print(stack_a[-1])
print(stack_a.pop())

print(stack_a.pop())







