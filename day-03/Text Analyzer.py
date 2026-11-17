
def count_characters(text):
    return len(text)

def count_words(text):
    return len(text.split())

def count_vowels(text):
    v = 0
    for i in text.lower():
        if i in "aeiou":
            v += 1
    return v

def count_consonants(text):
    x = 0
    for i in text.lower():
        if i.isalpha() and i not in "aeiou":
            x += 1
    return x

def find_longest_word(text):
    words = text.split()

    if not words:
        return ""
    longest = max(words, key=len)
    return longest

def lowercase(text):
    return text.lower()

def uppercase(text):
    return text.upper()

def main():
    text = input("Enter your text: ")
    print("Characters:", count_characters(text))
    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Longest word:", find_longest_word(text))
    print("Lowercase:", lowercase(text))
    print("Uppercase:", uppercase(text))
main()