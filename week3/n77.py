#직사각형 넓이 구하기

def solution(dots):
    a,b = set([dots[i][0] for i in range(len(dots))])
    c,d = set([dots[i][1] for i in range(len(dots))])       
    return abs((a-b)*(c-d))