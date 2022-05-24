def common_letters(string1,string2):
    for common in string1:
        if common in string2:
            print("Common Letters: ", common, end=', ')
    return common
 