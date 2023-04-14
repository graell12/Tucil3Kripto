import hashlib
import RSA
from Crypto.Hash import SHA3_224

def _hash(text, string=True):
    if string:
        return hashlib.new("sha3_224", text.encode()).digest()
    return hashlib.new("sha3_224", text).digest()

def hash(text, string=True):
    if string:
        return SHA3_224.new(text.encode()).digest()
    return SHA3_224.new(text).digest()
# def digitalSign(filename, priv_key):
    