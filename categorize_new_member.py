def categorize_new_member(data):
    emptyList = []

    for x in data:
        if x[0] >= 55 and x[1] > 7:
            emptyList.append("Senior")
        else:
            emptyList.append("Open")
    return emptyList

data = [(60 , 7)]
print(categorize_new_member(data))

