def rectangleRotation(a, b):
    s = math.sqrt(2)
    x1 = a / 2 // s * 2 + 1
    y1 = b / 2 // s * 2 + 1
    x2 = (a + s) / 2 // s * 2
    y2 = (b + s) / 2 // s * 2
    return x1*y1 + x2*y2
