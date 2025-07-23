# https://leetcode.com/problems/fraction-to-recurring-decimal/?envType=problem-list-v2&envId=hash-table


def fractionToDecimal(numerator: int, denominator: int) -> str:
    while True:
        if numerator < denominator:
            numerator *= 10
        else:
            quot = numerator // denominator


            


if __name__ == '__main__':
    case = 1, 2
    print(fractionToDecimal(*case))
    case = 2, 1
    print(fractionToDecimal(*case))
    case = 4, 333    
    print(fractionToDecimal(*case))
