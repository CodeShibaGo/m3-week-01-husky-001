def is_square(n):
    a = n ** 0.5
    if a * a == n:
        return True
    else:
        return False



n = int(input(""))
print(is_square(n))