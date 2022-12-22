# pylint: disable=redefined-outer-name
def getMinMax(a):
    min_val = a[0]  # assuming the min and max to be at first index
    max_val = a[0]
    for i in range(len(a)):
        if a[i] < min_val:
            min_val = a[i]
        elif a[i] > max_val:
            max_val = a[i]
    return min_val, max_val


a = [1, 2, -42, 5, 10, -100, 430]
print(getMinMax(a))
