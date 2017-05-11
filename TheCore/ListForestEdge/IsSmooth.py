def isSmooth(arr):
    if arr[0] != arr[len(arr)-1]:
        return False
    mid = 0
    if len(arr)%2 == 1:
        mid = arr[len(arr)/2]
    else:
        mid = arr[len(arr)/2] + arr[len(arr)/2 -1]
    if arr[0] == mid:
        return True
    return False
