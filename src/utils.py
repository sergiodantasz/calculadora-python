from re import search


def is_num_or_dot(string: str) -> bool:
    return bool(search(r'^[0-9.]$', string))


def is_valid_number(string: str) -> bool:
    try:
        float(string)
        return True
    except ValueError:
        return False
