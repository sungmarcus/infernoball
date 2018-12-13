import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
import sys

# modified from https://www.quickprogrammingtips.com/python/aes-256-encryption-and-decryption-in-python.html
BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

def encrypt(raw, key):
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw))

def decrypt(enc, key):
     enc = base64.b64decode(enc)	
     iv = enc[:16]
     cipher = AES.new(key, AES.MODE_CBC, iv)
     return unpad(cipher.decrypt(enc[16:]))
input_cipher = sys.argv[1]
input_secret = sys.argv[2]

with open(input_cipher,"r") as cipher_file:
    cipher = cipher_file.read()
with open(input_secret, "r") as secret_file:
    secret = secret_file.read()
secret = secret.strip()
next_level = decrypt(cipher,secret.zfill(32).decode('hex'))

with open("next_layer","w") as next_layer:
    next_layer.write(next_level)
