def abbrev_name(name):
    name1_capitalize = name[0].capitalize()
    name2_capitalize = name[1].capitalize()
    result = name1_capitalize[0] + "." + name2_capitalize[0]
    return result


name = ["John","Smith"]
print(abbrev_name(name))

#解不出來了 不知道如何把1輸入 拆分為2
#如果把輸入強制設定成2個   返回值會變2個   不是一個  跟測試檔需要指返回一個不相符

