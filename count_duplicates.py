def count_duplicates(text):
    text = text.lower()
    duplicate_chars = set()
    for char in text:
        if char not in duplicate_chars:
            duplicate_chars.add(char)



    return len(duplicate_chars)


result = count_duplicates("AaBbCdeeeeeee")
print(result)