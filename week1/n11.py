#최빈값 구하기

import statistics

def solution(array):
    
    if len(statistics.multimode(array)) > 1:
        return -1
    else:
        answer = statistics.mode(array)
    return answer