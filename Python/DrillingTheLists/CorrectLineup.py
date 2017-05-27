def correctLineup(athletes):
    return sum(zip(athletes[1::2], athletes[::2]), ())
