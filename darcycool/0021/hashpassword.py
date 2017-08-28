import uuid
from hashlib import sha256


def encrypt_password(password, salt=None):
    if salt is None:
        salt = uuid.uuid4().hex

    return sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == sha256(salt.encode() + user_password.encode()).hexdigest()

print(encrypt_password('123456', '666'))
