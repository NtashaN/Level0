def common_letters(string1,string2):
    string1_lowered = string1.lower()
    string2_lowered = string2.lower()
    collected_letters = ""
    for common in string1_lowered:
        if common in string2_lowered  and common not in collected_letters :
            if len(collected_letters) > 0:
                collected_letters = collected_letters + ", " + common
            else:
                collected_letters = collected_letters + common
    print("Common letters:",collected_letters)
