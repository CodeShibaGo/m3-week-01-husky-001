def change_case(input_string, mode):
    if mode == "upper":
        return input_string.upper()
    elif mode == "lower":
        return input_string.lower()
    else:
        return "Invalid mode. Please use 'upper' or 'lower'."

input_string = input("請輸入英文:")
result = change_case(input_string,"lower")
print(result)  # 輸出: "HELLO WORLD"