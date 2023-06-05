from re import search


def is_num_or_dot(string: str) -> bool:
    return bool(search(r'^[0-9.]$', string))
