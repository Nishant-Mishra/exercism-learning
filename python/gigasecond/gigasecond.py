from datetime import datetime as dt
from datetime import timedelta as tdel


def add(moment):
    if isinstance(moment, dt):
        return moment + tdel(seconds=10**9)
