def century(year):
    year_str = str(year)
    if year_str[-2] != "0":
        return int(year_str[0:2])+1
    elif year_str[-1] != "0":
        return int(year_str[0:2])+1
    elif year_str[-2:-1] == "0":
        return int(year_str[0:2])


result = century(1710)
print(result)





