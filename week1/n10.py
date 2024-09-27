#중앙값 구하기
import pandas as pd

def solution(array):
    
    arrays = pd.Series(array)

    return arrays.median()