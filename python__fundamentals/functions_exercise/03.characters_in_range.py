first_char = input()
second_char = input()


def get_chars_in_range(first, second):
    result = []
    min_char = min([first_char, second])
    max_char = max([first, second])
    for i in range(ord(min_char) + 1, ord(max_char)):
        character = chr(i)
        result.append(character)
    return result


result = get_chars_in_range(first_char, second_char)
print(" ".join(result))