def permutationCipher(password, key):
    table = string.maketrans(string.ascii_lowercase, key)
    return str(password).translate(table)
