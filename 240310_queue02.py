from collections import deque

queue = deque()

def enqueue(item):
    queue.append(item)

def dequeue():
    if not is_empty():
        return queue.popleft()
    else:
        return None

def is_empty():
    return len(queue) == 0

def size():
    return len(queue)    

# enqueue(1)
# enqueue(2)
# enqueue(3)

# print(queue)

# print(dequeue())
# print(queue)
# print(dequeue())
# print(queue)
# print(dequeue())
# print(queue)



# Quiz. queue2 를 만드세요. 
# 1,2,3,4,5를 넣고, 
# 1,2,3,4,5 순으로 (dequeue하면서) 출력하세요.
queue = deque()
number = [1,2,3,4,5]

for i in number:
    enqueue(i)

print(queue)

while not is_empty():
    print(dequeue())
    print(queue)