def integerToStringOfFixedWidth(number, width):
    diff = len(str(number)) - width
    if diff > 0:
        return str(number)[diff:]
    if diff == 0:
        return str(number)
    if diff < 0:
        return '0' * abs(diff) + str(number)
