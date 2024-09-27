from fractions import Fraction

def solution(numer1, denom1, numer2, denom2):
    
    bunsu1 = Fraction(numer1/denom1).limit_denominator(1000)
    bunsu2 = Fraction(numer2/denom2).limit_denominator(1000)
    
    bunsu =  bunsu1 + bunsu2
    numer = bunsu.numerator
    denom = bunsu.denominator

    answer=[numer,denom]
    
    
    return answer