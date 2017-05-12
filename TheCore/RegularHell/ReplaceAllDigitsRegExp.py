def replaceAllDigitsRegExp(inpgutString):
    return  ''.join(['#' for x in inputString if x.isdigit()==True else x])
