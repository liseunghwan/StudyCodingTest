#저주의 숫자3

def solution(n):
    answer = 0  # 결과 값을 저장할 변수 초기화

    for i in range(n):
        answer += 1  # answer 값을 1 증가시킴

        # answer가 3의 배수이거나 숫자 '3'이 포함된 경우 반복해서 건너뜀
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1  # 조건을 만족할 때 answer 값을 1 더해 건너뜀

    return answer  # 최종 결과 반환
