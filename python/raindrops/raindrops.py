def convert(number: int) -> str:
    """
        Similar to FizzBuzz, create the string based on factors of the given number
        :param number: Given number
        :return: Created string
    """
    res = ""
    sounds = {
        3: 'Pling',
        5: 'Plang',
        7: 'Plong'
    }
    for num, sound in sounds.items():
        if number % num == 0:
            res += sound

    return res or str(number)
