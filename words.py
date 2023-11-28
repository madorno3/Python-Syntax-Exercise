def print_upper_words(words):
    """will print words in capital letters. enter words in array"""
    for word in words:
        print(word.upper())

def starts_with(words):
    """will print words in capital letters. enter words in array"""
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word)

def print_upper_words3(words, start):
    for word in words:
        for letter in start:
            if word.startswith(letter):
                print(word.upper())
                break


