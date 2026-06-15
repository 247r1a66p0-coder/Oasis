import string
import secrets

def generate_password(
    length,
    use_upper,
    use_lower,
    use_digits,
    use_symbols,
    exclude_similar
):

    characters = ""

    if use_upper:
        characters += string.ascii_uppercase

    if use_lower:
        characters += string.ascii_lowercase

    if use_digits:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    if exclude_similar:

        similar_chars = "O0l1I"

        for char in similar_chars:
            characters = characters.replace(char, "")

    if not characters:
        return None

    password = ''.join(
        secrets.choice(characters)
        for _ in range(length)
    )

    return password