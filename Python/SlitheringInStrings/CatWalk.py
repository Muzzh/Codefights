def catWalk(code):
    return re.sub(r'(^\s*)|(\s*$)', '', re.sub(r'(\s+)', ' ', code))
