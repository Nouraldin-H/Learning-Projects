class LetterFilter:

    def __init__(self):
        self.s = s

    def filter_vowels(self):
        vowels = "aeiou"
        result = ""
        for char in self.s:
            if char not in vowels:
                result += char
        return result
    
    def filter_consonants(self):
        consonants = "bcdfghjklmnpqrstvwxyz"
        result = ""
        for char in self.s:
            if char not in consonants:
                result += char
        return result
    
s = input()
f = LetterFilter(s)
print(f.filter_vowels())
print(f.filter_consonants())