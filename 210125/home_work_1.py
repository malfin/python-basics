date_n = {chr(el) for el in range(ord('0'), ord('9') + 1)}
date_n.update(['/'])

required_date = {'/'}


def date_is_valid(date):
    date_as_set = set(date)

    if not date or date_as_set - date_n or required_date - date_as_set:
        return False

    for cct in required_date:
        count = date.count(cct)
        if count != 2:
            return False

    den, mes, got = date.split('/')
    if len(den) != 2 or len(mes) != 2 or len(got) != 4:
        return False
    return True


assert date_is_valid('01/02/2021')
assert not date_is_valid('01/020/2021')
