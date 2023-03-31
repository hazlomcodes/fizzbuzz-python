#Define a function called anti_vowel that takes one string, text, as input and returns the text with all of the vowels removed.
#For example: anti_vowel("Hey You!") should return "Hy Y!". Don’t count Y as a vowel. Make sure to remove lowercase and uppercase vowels.

def anti_vowel(text) :
    removed = text
    vowel = ['a','e','i','o','u','A','E','I','O','U']
    for char1 in text :
        for char2 in vowel:
            if char1 == char2:
                removed = removed.replace(char1,"")
    return removed
print anti_vowel("la roompa")