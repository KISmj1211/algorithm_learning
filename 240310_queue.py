queue = []

def enqueue(item):
    queue.append(item)

def dequeue():
    if not is_empty():
        return queue.pop(0)
    else:
        return None

def is_empty():
    return len(queue) == 0

def size():
    return len(queue)


from collections import deque


