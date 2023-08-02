from re import search


def is_num_or_dot(string: str) -> bool:
    return bool(search(r'^[0-9.]$', string))


def is_valid_number(string: str) -> bool:
    try:
        float(string)
        return True
    except ValueError:
        return False


def is_empty(string: str) -> bool:
    return len(string) == 0


def convert_to_number(string: str) -> int | float:
    number = float(string)
    if number.is_integer():
        number = int(number)
    return number
