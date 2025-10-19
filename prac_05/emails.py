def extract_name_from_email(email):
    """Extracts a name from an email address."""
    # Take the part before the @
    local_part = email.split('@')[0]
    # Replace dots with spaces and title-case each word
    name_guess = " ".join(part.title() for part in local_part.split('.'))
    return name_guess


def main():
    key_to_value = {}  # Dictionary to store emails (keys) and names (values)

    while True:
        email = input("Email: ").strip()
        if email == "":
            break

        name_guess = extract_name_from_email(email)
        confirm = input(f"Is your name {name_guess}? (Y/n) ").strip().lower()

        if confirm not in ("", "y", "yes"):
            # User didn't confirm, ask for the correct name
            name_guess = input("Name: ").strip()

        key_to_value[email] = name_guess

    print("\nStored emails and names:")
    for email, name in key_to_value.items():
        print(f"{name} ({email})")

main()
