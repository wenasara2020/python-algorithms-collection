 
def search(arr, n, f):
 
    for i in range(0, n):
        if (arr[i] == f):
            return i
    return -1
 

arr = [5, 32, 24, 150, 240 , 48 , 89 , 8, 464]
f = 8
n = len(arr)
 

result = search(arr, n, f)
if(result == -1):
    print("number is not present in array")
else:
    print("number is present at index", result)
