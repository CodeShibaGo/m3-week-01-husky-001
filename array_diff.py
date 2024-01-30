def array_diff(a,b):
    none_list = []
    result = [x for x in  a  if x not in  b]
    return result

a=str(input("請輸入列表1"))
b=str(input("請輸入列表2"))
print(array_diff(a, b))