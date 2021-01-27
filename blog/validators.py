import re
from django.core.exceptions import ValidationError


def check_phone(value):
    pattern = r'09[01239][0-9][0-9]{7}'
    f = re.match(pattern, value)
    if not f:
        raise ValidationError('شماره اشتباه میباشد.')

