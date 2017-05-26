def wordPower(word):
    num = {v:i+1 for i,v in enumerate(string.ascii_lowercase)}
    return sum([num[ch] for ch in word])
