def positive_sum(arr):
    total = sum( i for i in arr if i > 0 )
    return total

arr=[1,2,3,3,-4,-4]
a=positive_sum(arr)
print(a)