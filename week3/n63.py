#문자열 계산하기

def solution(my_string):
    # 공백을 제거한 뒤 "+"와 "-"를 기준으로 나누어 계산
    tokens = my_string.split()
    result = int(tokens[0])  # 첫 번째 숫자로 초기화

    for i in range(1, len(tokens) - 1, 2):
        operator = tokens[i]
        operand = int(tokens[i + 1])

        if operator == '+':
            result += operand
        elif operator == '-':
            result -= operand

    return result
