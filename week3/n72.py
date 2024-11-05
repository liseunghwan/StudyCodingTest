#문자열 정렬하기(2)

def solution(my_string):
    answer = ''
    for i in my_string:
        answer += i.lower()
    return ''.join(sorted(answer))