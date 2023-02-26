# def editDistance(s,t):
def editDistance(s1, s2):
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)
    if s1[-1] == s2[-1]:
        cost = 0
    else:
        cost = 1
    return min(editDistance(s1[:-1], s2) + 1,
               editDistance(s1, s2[:-1]) + 1,
               editDistance(s1[:-1], s2[:-1]) + cost)

# def display(s,t):
def display(s1, s2):
    distance = editDistance(s1, s2)
    return "The edit distance between {} and {} is {}".format(s1, s2, distance)