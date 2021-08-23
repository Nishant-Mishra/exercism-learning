def convert(number):
    res = ""
    if not number % 3:
        res += 'Pling'
    if not number % 5:
        res += 'Plang'
    if not number % 7:
        res += 'Plong'
    if not res:
        res = str(number)

    return res
