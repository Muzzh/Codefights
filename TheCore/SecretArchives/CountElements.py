def countElements(inputString):
    m = re.findall('\d+|(?:\".*?\")|true|false', inputString)
    return len(m)

    
