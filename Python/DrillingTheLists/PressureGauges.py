def pressureGauges(morning, evening):
    return [[min(morning[i], evening[i]) for i in range(len(evening))], [max(morning[i],evening[i]) for i in range(len(evening))]]
