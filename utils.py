import re

email_pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"


def validate_email(email: str):
    if (re.match(email_pattern, email)):
        return True
    return False
