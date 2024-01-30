def find_capitals(word):
    word_capitals = word.upper()
    result = ""
    for x in word:
        if x in word_capitals:
            result += x
    return result.replace(" ", "")

word = "i am  You  fatHer"
a = find_capitals(word)
print(a)