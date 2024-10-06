#문자열 정렬하기(1)

def solution(my_string):
    answer = []
    mylist = list(my_string)
    
    for i in mylist:
        if i.isdigit():
            answer.append(int(i))
            
    answer.sort()
    return answer