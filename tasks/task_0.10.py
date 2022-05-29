def common_letters(string1,string2):
    s1 = string1.lower()
    s2 = string2.lower()
    c = ""
    for common in s1:
        if common in s2  and common not in c :
            c = c + common + ','
    return "Common letters: " + c