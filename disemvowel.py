def disemvowel(s):
    y = "aeiouAEIOU"
    b = ""
    for x in s:
        if x not in y:
            b += x
    return b

test = "This is a sample text."
disemvowel(test)
print(disemvowel(test))