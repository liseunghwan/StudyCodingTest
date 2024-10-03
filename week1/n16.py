#배열의 평균값
def solution(numbers):
    sum = 0 
    for i in numbers:
        sum += i 
    answer = sum / len(numbers)
    return answer