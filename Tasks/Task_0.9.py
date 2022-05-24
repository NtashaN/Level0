def vowel_detector(word):
    vowels = "aeiouAEIOU"
    for vowel in word:
        if vowel in vowels:
            print(vowel, end=', ')
    return vowel
