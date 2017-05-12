def chessBishopDream(size, P, direction, k):
    ans = [0, 0]

    for i in range(2):
        pos = P[i]
        di = direction[i]

        new_pos = pos + k*di

        modulus = size[i] * 2

        new_pos = new_pos%modulus

        mid = (float(modulus-1)) / 2
        ans[i] = int(mid - abs(mid - new_pos))

    return ans
        
