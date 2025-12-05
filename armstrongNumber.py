def armstrongSum(number):
    digitSum = 0
    digitCount = 0

    temporaryVariable = number
    while temporaryVariable > 0:
        digitCount = digitCount + 1
        temporaryVariable = temporaryVariable // 10

    temporaryVariable = number
    for index in range(1, temporaryVariable + 1):
        digit = temporaryVariable % 10
        digitSum = digitSum + (digit ** digitCount)
        temporaryVariable //= 10
    return digitSum


userNumber = int(input("\nPlease Enter the Number to Check for Armstrong: "))

if userNumber == armstrongSum(userNumber):
    print("\n %d is an Armstrong Number.\n" % userNumber)
else:
    print("\n %d is Not an Armstrong Number.\n" % userNumber)
