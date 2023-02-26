import decimal

def gregoryLeibnitz(n_terms: int) -> str:
    decimal.getcontext().prec = 8
    pi = decimal.Decimal(0)
    for i in range(n_terms):
        pi += decimal.Decimal((4/(i*2+1)) * ((-1)**i))
    return str(round(pi, 5))