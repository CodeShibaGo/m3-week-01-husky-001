def even_or_odd(number):
    if number % 2 != 0:
        return  "Odd"
    elif number % 2 == 0:
        return  "Even"

num=int(input("請輸入數字"))
result = even_or_odd(num)
print(result)