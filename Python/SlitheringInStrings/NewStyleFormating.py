def newStyleFormatting(s):
    s = re.sub(r'%%', '{temp}', s)
    s = re.sub(r'%\w', '{}', s)
    s = re.sub(r'{temp}', '%', s)
    return s
