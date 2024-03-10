def CountDigit(number, digit):
    count = 0
    if number < 0:
        number=-number
    while number > 0:
        if number % 10 == digit:
            count += 1
        number //= 10
    return count

number,digit=input().split()
number=int(number)
digit=int(digit)
count=CountDigit(number,digit )
print("Number of digit 2 in "+str(number)+":",count)
