def bishopDiagonal(b1, b2):
    b1_ord = ord(b1[0])
    b1_num = int(b1[1])
    diag_a = [chr(b1_ord + x) + str(b1_num + x) for x in range(-7,8) if 97 <= (b1_ord+x) <=104 and 1 <= b1_num + x <= 8]
    diag_b = [chr(b1_ord + x) + str(b1_num - x) for x in range(-7,8) if 97 <= (b1_ord+x) <=104 and 1 <= b1_num - x <= 8]
    if b2 in diag_a:
        return [diag_a[0], diag_a[-1]]
    if b2 in diag_b:
        return [diag_b[0], diag_b[-1]]
    return sorted([b1, b2])
