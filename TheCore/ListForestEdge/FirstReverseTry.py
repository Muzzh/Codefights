def firstReverseTry(arr):
    if len(arr) <= 1:
        return arr
    temp1 = arr[0]
    temp2 = arr[len(arr)-1]
    arr[0] = temp2
    arr[len(arr)-1] = temp1
    return arr
