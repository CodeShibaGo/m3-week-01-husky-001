def distinct(input_list):
     none_list = []
     for i in input_list:
        if i not in none_list:
            none_list.append(i)
     return none_list

input_list = input("請輸入任意一串數字")
out = distinct(input_list)
print(out)





