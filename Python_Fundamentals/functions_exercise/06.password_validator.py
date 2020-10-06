password = input()


def validate_passwrod(password):
    mesages = []
    valid_length = len(password) >= 6 and len(password) <= 10
    are_letters_and_digits = password.isalnum()
    has_atleat_two_digits = len([x for x in password if x.isdigit()]) >= 2

    if valid_length and are_letters_and_digits and has_atleat_two_digits:
        mesages.append("Password is valid")
    if not valid_length:
        mesages.append("Password must be between 6 and 10 characters")
    if not are_letters_and_digits:
        mesages.append("Password must consist only of letters and digits")
    if not has_atleat_two_digits:
        mesages.append("Password must have at least 2 digits")

    return mesages


print("\n".join(validate_passwrod(password)))
