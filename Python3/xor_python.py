from io import BytesIO
from itertools import cycle

def xore(data, key):
    return bytes(a ^ b for a, b in zip(data, cycle(key)))
b = b'This is a test'
with BytesIO(b) as f:
    enc = xore(f.read(), b'anykey')
print(enc)
with BytesIO(enc) as f:
    dec = xore(f.read(), b'anykey')
    print(dec)
