def killKthBit(n, k):
    return (n^(1<<(k-1))) & n
