def is_pangram(sentence: str):
    sentence = set(sentence.lower())
    alphabet = [chr(x) for x in range(97, 123)]
    for ch in alphabet:
        if ch not in sentence:
            return False
    return True
