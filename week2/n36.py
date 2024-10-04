#구슬을 나누는 경우의 수

from math import factorial as fac

def solution(balls, share):
    answer = 0
    n = fac(balls)
    m = fac(share)
    bottom = fac(balls-share) * m
    return n/bottom