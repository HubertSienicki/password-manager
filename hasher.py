from hashlib import sha256
import random
from secret_key import get_secret_key

SECRET_KEY = get_secret_key()
ALPHABET = ('abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTYVWXYZ', '0123456789', '(,._-*~"<>/|!@#$%^&)+=')
