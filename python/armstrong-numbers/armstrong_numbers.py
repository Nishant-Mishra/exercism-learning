def is_armstrong_number(number):
    digs = list(map(int, str(number)))
    n_digs = len(digs)
    ans = sum(map(lambda base: base ** n_digs, digs))
    return ans == number
