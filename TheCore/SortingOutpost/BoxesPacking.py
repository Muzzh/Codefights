def boxesPacking(length, width, height):
    boxes = sorted([sorted([length[i], width[i], height[i]]) for i in range(len(length))])
    for i in range(len(boxes)-1):
        for j in range(len(boxes[i])):
            if boxes[i+1][j] > boxes[i][j]:
                pass
            else:
                return False
    return True

    
