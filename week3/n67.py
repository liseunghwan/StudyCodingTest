#자릿수 더하기

def solution(n):
    answer = 0

    li = list(str(n))
    for i in li:
        answer += int(i)

    return answer