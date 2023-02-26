def median(a, b, c):
  if (a <= b <= c) or (c <= b <= a):
    return b
  elif (b <= a <= c) or (c <= a <= b):
    return a
  else:
    return c

def alternate_median(a, b, c):
  return (a + b + c) - max(a, b, c) - min(a, b, c)

def get_medians(a, b, c):
  return 'Median: ' + str(median(a, b, c)) + ', Alternate Median: ' + str(alternate_median(a, b, c) + 2)