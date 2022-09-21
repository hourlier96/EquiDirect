import bcrypt


def new_salt():
    return bcrypt.gensalt()


def hash_password(plain_text_password, salt):
    return bcrypt.hashpw(plain_text_password, salt).decode("utf-8")


def check_password(plain_text_password, stored_hash):
    return bcrypt.checkpw(plain_text_password.encode("utf-8"), stored_hash)
