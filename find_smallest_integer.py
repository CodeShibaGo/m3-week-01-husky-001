def find_smallest_int(arr):
    arr.sort()
    return(arr[0])


arr = [int(input(f"請輸入第{x + 1}個數字:")) for x in range(5)]
find_smallest_int(arr)
print(arr[0])







