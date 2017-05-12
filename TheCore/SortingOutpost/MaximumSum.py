def maximumSum(arr, queries):
    arr += arr
    print arr
    for i in range(len(queries)):
        queries[i][1] += 1

    for i in range(len(queries)):
        tot = 0
        for ii in range(len(arr)/2):
            low_end = ii + queries[i][0]
            hi_end = ii + queries[i][1]
            print low_end, hi_end


    
