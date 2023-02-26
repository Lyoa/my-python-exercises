def leftPad(s, n, c):
    if len(s) >= n:
        return s
    else:
        return leftPad(c + s, n, c)