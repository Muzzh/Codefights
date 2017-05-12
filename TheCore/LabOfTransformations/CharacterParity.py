def characterParity(symbol):
    if symbol.isdigit() == True:
        symbol = int(symbol)
        if symbol%2 == 0:
            return 'even'
        else:
            return 'odd'
    return "not a digit"
