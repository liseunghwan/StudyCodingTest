#배열 두 배 만들기

def solution(numbers):
    leng = len(numbers)
    for i in range(leng):
        numbers[i] = numbers[i] * 2
    answer = numbers.copy()
    return answer