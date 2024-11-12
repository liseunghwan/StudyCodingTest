#균형잡힌 세상

import sys

while True:
    sentence = sys.stdin.readline().rstrip()
    
    if(sentence == "."):
        break
    stack = []


    for i in sentence:
        if(i == "(" or i == "["):
            stack.append(i)
        elif(i == ")"):
            if(len(stack) != 0 and stack[-1] == "("):
                stack.pop()
            else:
                stack.append(")")
                break
        elif(i == "]"):
            if(len(stack) != 0 and stack[-1] == "["):
                stack.pop()
            else:
                stack.append("]")
                break


    if(len(stack) == 0):
        print("yes")
    else:
        print("no")