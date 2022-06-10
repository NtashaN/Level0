def time_converter(num):
    hours = num//60
    minutes = num%60
    if (hours) !=1 and minutes != 1:
        return str(hours) + ' hours, ' + str(minutes) + ' minutes'

    elif (hours) !=1 and (minutes) == 1:
        return str(hours) + ' hours, ' + str(minutes) + ' minute'

    elif (hours) == 1 and (minutes) == 1:
        return str(hours) + ' hour, ' + str(minutes) + ' minute'

    elif (hours) == 1 and (minutes) != 1:
        return str(hours) + ' hour, ' + str(minutes) + ' minutes'