def authenticate(username, password, users):
    """Compare test credentials in this educational fixture only."""
    return username in users and users[username] == password
