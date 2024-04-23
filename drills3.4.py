def count_syllables(word):
    vowels = "aeiouy"
    count = 0
    last_was_vowel = False

    for char in word.lower():
        if char in vowels:
            if not last_was_vowel:
                count += 1
            last_was_vowel = True
        else:
            last_was_vowel = False

    if count == 0:
        count = 1

    return count

word = input("Enter a word: ")
syllables = count_syllables(word)
print(f"Word '{word}' has {syllables} syllable(s).")
