def solve():
    result = 0
    values = [1, 2]
    while(values[1] < 4e6):
        if(values[1] % 2 == 0):
            result += values[1]
        hold = values[0]
        values[0] = values[1]
        values[1] = hold + values[0]
    return result

print(solve())