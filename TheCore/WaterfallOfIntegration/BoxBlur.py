def boxBlur(image):
    return [[(sum(sum(x[j:j+3]) for x in image[i:i+3])/9) for j in range(len(image[0])-2)] for i in range(len(image)-2)]
