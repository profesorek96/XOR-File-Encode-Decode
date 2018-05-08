from io import BytesIO
from itertools import cycle

def xore(data, key):
    return bytes(a ^ b for a, b in zip(data, cycle(key)))

def xor_python(in_file,out_file,key):
    try:
        with open(in_file, 'rb') as encry, open(out_file, 'wb') as decry:
            decry.write(xore(encry.read(), key))
    except:
        return False
    return True

