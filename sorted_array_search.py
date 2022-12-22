def search(arr, target):
    for i in range(len(arr)):
        if (target == arr[i]):
            return i
            break
    else:
        return -1


arr = [1, 2, 3, 4, 6, 7, 4] #prints only the first occurance of the element
target = 7
print(search(arr, target))
