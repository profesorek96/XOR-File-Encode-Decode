from ctypes import CDLL, c_char, POINTER, c_bool, cast, byref

lib = CDLL('xor_file')
lib.xor_crypt_encrypt.argtypes = (POINTER(c_char), POINTER(c_char), POINTER(c_char))

lib.xor_crypt_encrypt.restype = c_bool


def xor_extern_dll(nazwa1, nazwa2, klucz):
    l1 = len(nazwa1)
    l2 = len(nazwa2)
    l3 = len(klucz)

    l1_c = cast((c_char * l1)(), POINTER(c_char))
    l2_c = cast((c_char * l2)(), POINTER(c_char))
    l3_c = cast((c_char * l3)(), POINTER(c_char))

    for i in range(l1):
        l1_c[i] = nazwa1[i]

    for i in range(l2):
        l2_c[i] = nazwa2[i]
    for i in range(l3):
        l3_c[i] = klucz[i]

    return lib.xor_crypt_encrypt(l1_c, l2_c, l3_c)
