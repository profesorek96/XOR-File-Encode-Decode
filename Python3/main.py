import xor_dll
def testCallTest():
    in_file = "ala.txt"
    out_file = "ola.txt"
    key = "10101010"
    in_file = in_file.encode('ascii')
    out_file = out_file.encode('ascii')
    key = key.encode('ascii')
    val = xor_dll.xor_extern_dll(in_file, out_file, key)
    print(val)


testCallTest()