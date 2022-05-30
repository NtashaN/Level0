def vowel_detector(word):
    word = word.lower()
    detector = ""
    vowels = "aeiou"
    for vowel in word:
        if vowel in vowels and vowel not in detector:
            if len(detector) > 0:
                detector = detector + ", "+ vowel  
            else:
                detector = detector + vowel 
    print("Common Letters:", detector)