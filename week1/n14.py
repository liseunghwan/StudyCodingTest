#피자 나눠 먹기(2)
import math

def solution(n):
    key = math.gcd(n,6)
    answer = (key * n/key * 6/key) / 6 
    return answer