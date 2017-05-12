def addBorder(picture):
    new = []
    for i in range(len(picture)):
        picture[i] = '*' + picture[i] + '*'
    picture.append('*' * len(picture[0]))
    picture.insert(0, ('*' * len(picture[0])))

    return picture
