"""
    Output the lyrics to 'The Twelve Days of Christmas':

        On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.

        On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.

        On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves,
        and a Partridge in a Pear Tree.

        On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens,
        two Turtle Doves, and a Partridge in a Pear Tree.

        On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds,
        three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

        On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings,
        four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

        On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying,
        five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

        On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming,
        six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves,
        and a Partridge in a Pear Tree.

        On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking,
        seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens,
        two Turtle Doves, and a Partridge in a Pear Tree.

        On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing,
        eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds,
        three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

        On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping,
        nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings,
        four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

        On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping,
        ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying,
        five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
"""
from typing import List

gifts = (
    '',
    'a Partridge in a Pear Tree.',
    'two Turtle Doves,',
    'three French Hens,',
    'four Calling Birds,',
    'five Gold Rings,',
    'six Geese-a-Laying,',
    'seven Swans-a-Swimming,',
    'eight Maids-a-Milking,',
    'nine Ladies Dancing,',
    'ten Lords-a-Leaping,',
    'eleven Pipers Piping,',
    'twelve Drummers Drumming,',
)

PRAYER_START = "On the {nth} day of Christmas my true love gave to me:"

nth = (
    '',
    'first',
    'second',
    'third',
    'fourth',
    'fifth',
    'sixth',
    'seventh',
    'eighth',
    'ninth',
    'tenth',
    'eleventh',
    'twelfth'
)


def _nth_verse(n: int) -> str:
    verse = f"{PRAYER_START.format(nth=nth[n])} "
    all_gifts = ""
    for i in range(n, 1, -1):
        all_gifts += f"{gifts[i]} "

    if all_gifts:
        all_gifts += "and "
    all_gifts += f"{gifts[1]}"

    return verse + all_gifts


def recite(start_verse: int, end_verse: int) -> List[str]:
    """

    :param start_verse: Start Verse ID
    :param end_verse: End Verse ID
    :return: A list of prayer verses as queried.
    """
    return [_nth_verse(n) for n in range(start_verse, end_verse + 1)]
