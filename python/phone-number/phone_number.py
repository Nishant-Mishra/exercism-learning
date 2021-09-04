"""
Clean up user-entered phone numbers so that they can be sent SMS messages.

The North American Numbering Plan (NANP) is a telephone numbering system used by many countries in North America
like the United States, Canada or Bermuda. All NANP-countries share the same international country code: 1.

NANP numbers are ten-digit numbers consisting of a three-digit Numbering Plan Area code, commonly known as area code,
followed by a seven-digit local number.
The first three digits of the local number represent the exchange code,
followed by the unique four-digit number which is the subscriber number.

The format is usually represented as

    (NXX)-NXX-XXXX
where N is any digit from 2 through 9 and X is any digit from 0 through 9.

Your task is to clean up differently formatted telephone numbers by removing punctuation and
the country code (1) if present.

For example, the inputs

    +1 (613)-995-0253
    613-995-0253
    1 613 995 0253
    613.995.0253
should all produce the output

    6139950253

Note: As this exercise only deals with telephone numbers used in NANP-countries,
only 1 is considered a valid country code.
"""
import re


class PhoneNumber:
    """
    This class accepts a human readable (pretty-formatted) phone number, as explained in module docstring
    and converts it into a 10-digit number string (w/o intl. code).
    """
    def __init__(self, number: str):
        self._validate(number)
        self._phn_str = number
        self._sms_num = None
        self._convert()

    @staticmethod
    def _validate(number: str):
        patt_intl_code = r"(?:(?:\+)?1)"
        patt_area_n_exch_code = r"(?:[2-9][0-9]{2})"
        patt_area_n_exch_code_in_paran = fr"(\()?{patt_area_n_exch_code}(?(1)\))"
        patt_num = r"[0-9]{4}"
        patt_wspace = r"[ ]*"
        patt_sep = fr"{patt_wspace}(?:-|\.)?{patt_wspace}"
        patt_full = fr"{patt_wspace}{patt_intl_code}?{patt_wspace}" + \
                    fr"{patt_area_n_exch_code_in_paran}{patt_sep}" + \
                    fr"{patt_area_n_exch_code}{patt_sep}" + \
                    fr"{patt_num}{patt_wspace}"

        if not re.fullmatch(patt_full, number):
            raise ValueError("Invalid phone number format")

    @property
    def number(self):
        """

        :return: The converted 10-digit SMS number
        """
        return self._sms_num

    @property
    def area_code(self):
        """

        :return: The 3-digit area code extracted from the input phone string
        """
        return self._sms_num[:3]

    @property
    def exchange_code(self):
        """

        :return: The 3-digit exchange code extracted from the input phone string
        """
        return self._sms_num[3:6]

    @property
    def subscriber_number(self):
        """

        :return: The 4-digit subscriber number extracted from the input phone string
        """
        return self._sms_num[6:]

    def _convert(self):
        phn_str = "".join([ch for ch in self._phn_str if ch.isdigit()])
        if len(phn_str) == 11:
            phn_str = phn_str[1:]
        self._sms_num = phn_str

    def pretty(self):
        """

        :return: A prettified phone number string:
            - No International code
            - Area Code inside parantheses
            - Area Code, Exchange Code and Subscriber number separated by '-'
        """
        return f"({self.area_code})-{self.exchange_code}-{self.subscriber_number}"
