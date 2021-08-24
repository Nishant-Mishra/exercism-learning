def score(x, y):
    score_map = {
        range(5, 10): 1,
        range(1, 5): 5,
        range(-1, 1): 10,
    }
    dist = (x ** 2 + y ** 2) ** 0.5
    for rangge, scorre in score_map.items():
        if rangge.start < dist <= rangge.stop:
            return scorre
    return 0
