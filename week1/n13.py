#피자 나눠 먹기(1)
def solution(n):
    answer = n // 7 +1
    if n%7==0 :
        answer-=1
    return answer