#등수매기기

def solution(score):
    answer = [1 for i in range(len(score))]
    avg = []
    for eng,math in score:
        avg.append((eng+math)/2)
    for i, val_i in enumerate(avg):
        for j, val_j in enumerate(avg):
            if avg[i] > avg[j]:
                answer[j] += 1
    return answer