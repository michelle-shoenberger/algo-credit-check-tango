def credit_check(s):
    total = 0
    for index, number in enumerate(s):
        num = int(number)
        if index%2 == 0:
            num *= 2
        if num >= 10:
            temp = 0
            for char in str(num):
                temp += int(char)
            num = temp
        total += num
    if  total % 10 == 0:
        return "The number is valid!"
    else:
        return "The number is invalid!"
