def stolenLunch(note):
    note = list(note)
    letters = 'abcdefghij'
    for i in range(len(note)):
        if note[i] in letters:
            note[i] = str(letters.index(note[i]))
        elif note[i].isdigit() == True:
            note[i] = int(note[i])
            note[i] = letters[note[i]]
        else:
            pass
    return ''.join(note)
