def knapsackLight(value1, weight1, value2, weight2, maxW):
    if weight1 + weight2 <= maxW:
        return value1+value2
    if min(weight1,weight2) > maxW:
        return 0
    if max(weight1, weight2) <= maxW:
        return max(value1,value2)
    if weight1 <= maxW:
        return value1
    return value2
