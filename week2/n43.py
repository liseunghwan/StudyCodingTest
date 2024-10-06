#최댓값 만들기(1)

def solution(numbers):
    numbers.sort(reverse=True)
    a = numbers[0]
    b = numbers[1]
    return a * b