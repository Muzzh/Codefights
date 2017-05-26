def getCommit(commit):
    return re.sub(r'([0?+!]+)', '', commit)
