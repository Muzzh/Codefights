def drawRectangle(canvas, rectangle):
    top_left = [rectangle[1], rectangle[0]]
    top_right = [rectangle[1], rectangle[2]]
    bot_left = [rectangle[3], rectangle[0]]
    bot_right = [rectangle[3], rectangle[2]]

    corners = [top_left, top_right, bot_left, bot_right]
    print corners
    for i in range(len(corners)):
        canvas[corners[i][0]][corners[i][1]] = '*'
    for i in range(rectangle[0]+1, rectangle[2]):
        canvas[top_left[0]][i] = '-'
        canvas[bot_left[0]][i] = '-'
    for i in range(rectangle[1]+1, rectangle[3]):
        canvas[i][top_left[1]] = '|'
        canvas[i][top_right[1]] = "|"
    return canvas

    
