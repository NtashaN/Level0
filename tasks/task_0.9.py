def vowel_detector(word):
    word = word.lower()
    detector = ""
    vowels = "aeiou"
    for vowel in word:
        if vowel in vowels and vowel not in detector:
            detector = detector + vowel + ','
    print("Vowels: ", detector)