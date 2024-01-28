def greet(name):
    if name == "Johnny" :
        return("Hello, my love!")
    else :
        return(f"Hello, {name}!")

a = input("請輸入名字")
result = greet(a)
print(result)


