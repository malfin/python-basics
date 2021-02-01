real_number = {chr(el) for el in range(ord('0'), ord('9') + 1)}
real_number.update(['.'], [','])

required_real_number = {'.'}


def real_number_is_valid(number):
    real_number_as_set = set(number)
    if not number or real_number_as_set - real_number or required_real_number - real_number_as_set:
        return False

    number_chunks = number.split('.')
    if len(number_chunks) < 1 or len(number_chunks[-1]) < 1:
        return False

    return True


assert real_number_is_valid('1.32')
assert not real_number_is_valid('1,32')
