def send_email(
    to_email: str,
    subject: str,
    message: str
):

    print("=" * 50)
    print("EMAIL SERVICE")
    print(f"To      : {to_email}")
    print(f"Subject : {subject}")
    print(f"Message : {message}")
    print("=" * 50)

    return True