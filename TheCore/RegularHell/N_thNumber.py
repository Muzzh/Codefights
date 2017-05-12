def nthNumber(s, n):
    pattern = r'(?:\D*\d+\D*){%r}\D*0*(\d+).*' % (n-1)
    return re.match(pattern, s).group(1)
