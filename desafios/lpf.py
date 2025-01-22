def solve():
    result = 3
    number = 600851475143
    number2 = 2
    while(number2 <= number):
        while(number % number2 == 0):
            number = number / number2
            result = number2
        number2 += 1
    return result

print(solve())
    