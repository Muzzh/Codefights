def timedReading(maxLength, text):
    import re
    words = re.findall('[a-zA-Z]+', text)
    return len([x for x in words if len(x) <= maxLength])
