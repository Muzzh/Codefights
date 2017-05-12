def eyeRhyme(pairOfLines):
    pattern = r'(?:.*)(.{3}(?=\t))(?:.*)(.{3}(?=$))'
    match = re.match(pattern, pairOfLines)
    return match.group(1) == match.group(2)
