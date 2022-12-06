from re import search as check_address_for_valid_pattern

ADDRESS_VALIDATION_REGEXP = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{3,4}$"


def is_address_valid(address) -> bool:
    """Returns true if address follows valid pattern"""
    return check_address_for_valid_pattern(ADDRESS_VALIDATION_REGEXP, address)
