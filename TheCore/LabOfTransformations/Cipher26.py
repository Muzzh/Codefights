def cipher26(message):

    letters = string.ascii_lowercase
    answer = [message[0]]
    tot = letters.index(message[0])

    for i in range(1,len(message)):
        target = letters.index(message[i])
        index_new_l = 26 + target - tot
        if index_new_l > 25:
            index_new_l = index_new_l%26
        answer.append(letters[index_new_l])
        tot += index_new_l

    return ''.join(answer)
