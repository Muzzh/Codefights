def arrayConversion(inputArray):
    def add(A):
        new = []
        for i in range(0, len(A)-1, 2):
            new.append(A[i] + A[i+1])
        return new

    def mult(A):
        new = []
        for i in range(0, len(A)-1, 2):
            new.append(A[i] * A[i+1])
        return new

    while len(inputArray) > 1:
        inputArray = add(inputArray)
        if len(inputArray) > 1:
            inputArray = mult(inputArray)

    return int(inputArray[0])
