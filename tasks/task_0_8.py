def time_converter(num):
    if (num//60) !=1 and num%60 != 1:
        return str(num//60) + ' hours,' + str(num%60) + ' minutes'

    elif (num//60) !=1 and (num%60) == 1:
        return str(num//60) + ' hours,' + str(num%60) + ' minute'

    elif (num//60) == 1 and (num%60) == 1:
        return str(num//60) + ' hour,' + str(num%60) + ' minute'

    elif (num//60) == 1 and (num%60) != 1:
        return str(num//60) + ' hour,' + str(num%60) + ' minutes'
