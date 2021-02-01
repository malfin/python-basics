import re

RE_REAL_NUMBER_VALIDATOR = re.compile(r'^[0-9]+[.,]?([0-9]+)?$')


def real_number_is_valid(data):
    return RE_REAL_NUMBER_VALIDATOR.match(data)


assert real_number_is_valid('132')
assert real_number_is_valid('1,32')

