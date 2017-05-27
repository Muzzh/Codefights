def wordsRecognition(word1, word2):
    def getIdentifier(w1, w2):
        return ''.join(sorted(set([x for x in w1 if x not in w2])))

    return [getIdentifier(word1, word2), getIdentifier(word2, word1)]
