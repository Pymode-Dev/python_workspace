def collatz(number):
    while number != 1:
        if number% 2 == 0:   # if the number is even
            result = number // 2
            return result
        else:   # if the number is odd
            result = 3 * number + 1   
            return result


print('enter a number: ')
n = int(input())
while n != 1:  # it exercises a recursive call 
    # once n reaches 1 it stops
    n = collatz(n)
    print(n)
