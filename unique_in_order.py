def unique_in_order(iterable):
    if  not iterable :
       return[]
    result = []
    i = 0
    while i < len(iterable)-1:
        if iterable[i] != iterable[i+1]:
            result.append(iterable[i])
        i += 1
    result.append(iterable[-1])
    return result
a = ("ABBCCDDEEEEEE")
result = unique_in_order(a)
print(result)

