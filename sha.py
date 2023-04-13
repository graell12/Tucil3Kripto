import hashlib
import RSA

def hash(text):
    hash = hashlib.new("sha3_224", text.encode())
    return hash.hexdigest()

# def digitalSign(filename, priv_key):
    