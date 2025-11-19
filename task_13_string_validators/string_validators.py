def alphanumeric_validator(string):
    has_alphanumeric_characters = False

    for char in string:
        if char.isalnum():
            has_alphanumeric_characters = True
            break

    return has_alphanumeric_characters


def alphabetical_validator(string):
    has_alphabetical_characters = False

    for letter in string:
        if letter.isalpha():
            has_alphabetical_characters = True
            break

    return has_alphabetical_characters


def digits_validator(string):
    has_digit_characters = False

    for digit in string:
        if digit.isdigit():
            has_digit_characters = True
            break

    return has_digit_characters


def lowercase_validator(string):
    has_lowercase_characters = False

    for char in string:
        if char.islower():
            has_lowercase_characters = True
            break

    return has_lowercase_characters


def uppercase_validator(string):
    has_uppercase_characters = False

    for char in string:
        if char.isupper():
            has_uppercase_characters = True
            break

    return has_uppercase_characters


def string_validator(string):
    validators_result = [
        alphanumeric_validator(string),
        alphabetical_validator(string),
        digits_validator(string),
        lowercase_validator(string),
        uppercase_validator(string),
    ]

    return "\n".join(str(x) for x in validators_result)


if __name__ == '__main__':
    s = input()
    result = string_validator(s)
    print(result)



