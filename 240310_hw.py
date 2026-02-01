# 스택으로 사용할 리스트 초기화
stack = []

# 막대기 쌓기
stack.append("A")
stack.append("B")
stack.append("C")

# 쌓아올린 막대기 출력
print("쌓아올린 막대기:")
for item in reversed(stack):
    print(item)

# 막대기 하나 제거
stack.pop()

# 막대기 하나를 제거하고 나서 출력
print("\n한 개의 막대기를 제거하고 나서:")
for item in reversed(stack):
    print(item)

