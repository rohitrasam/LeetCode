
def sqrt(x: int):
    sr = 1
    while sr * sr <= x:
        sr += 1
    
    return sr-1



print(sqrt(8))
