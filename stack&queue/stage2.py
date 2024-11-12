#제로

import sys

stack = []
n = int(sys.stdin.readline())

for _ in range(n):
    command = int(sys.stdin.readline())
    stack.append(int(command))
    
    if command == 0:
        stack.pop()
        stack.pop()

print(sum(stack))