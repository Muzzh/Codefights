def houseOfCats(legs):
    ans = []
    for i in range((legs/4) +1):
        ans.append((legs - 4*i)/2)
    return ans[::-1]
