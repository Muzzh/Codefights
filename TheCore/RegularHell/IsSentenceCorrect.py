def isSentenceCorrect(sentence):
    pattern = re.compile('\A[A-Z][^!.?]*[!.?]\Z')
    return re.match(pattern, sentence) is not None
