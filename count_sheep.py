def count_sheep(sheep):

    sleeping_sheep_count = 0
    for is_sleeping in sheep:

        if is_sleeping == 1:
            sleeping_sheep_count += 1

    return sleeping_sheep_count

sheep= [0,1,1,0,1,1]
result = count_sheep(sheep)
print(result)
