def max_finder(num1, num2,num3):
    max_num = num1
    for num in num1, num2,num3:
        if num > max_num:
            max_num = num
    return max_num
