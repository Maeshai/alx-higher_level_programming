def introduce_myself(name, surname=""):
    """Print a full name.

    Args:
        name (str): The first name to print.
        surname (str): The last name to print.
    Raises:
        TypeError: If either of name or surname are not strings.
    """
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    if not isinstance(surname, str):
        raise TypeError("surname must be a string")
    print("Hello, I am {} {}".format(name, surname))
