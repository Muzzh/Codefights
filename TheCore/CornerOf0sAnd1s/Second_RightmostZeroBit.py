def secondRightmostZeroBit(n):
    return 2**(len(bin(n)[2:]) -((((str('{0:b}'.format(n))).rstrip('1'))[:len((str('{0:b}'.format(n))).rstrip('1'))-1]).rfind('0'))-1)
