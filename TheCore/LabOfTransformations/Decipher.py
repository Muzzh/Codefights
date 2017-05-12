def decipher(cipher):
    poss = list(range(97,123))
    poss = [str(x) for x in poss]

    chars = []
    cipher = str(cipher)
    print cipher, type(cipher)
    index = 0
    while index < len(cipher):
        print cipher[index]
        if cipher[index] == '1':
            chars.append(int(cipher[index: index + 3]))
            index += 3
        else:
            chars.append(int(cipher[index: index + 2]))
            index += 2

    return ''.join([chr(x) for x in chars])
