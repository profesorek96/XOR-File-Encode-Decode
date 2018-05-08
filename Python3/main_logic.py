import xor_dll
import xor_python
import error_xor_file
import error_xor_key
import time_xor
import datetime
def number_to_char_key(key):
    if key>=0 and key<=255:
        s_key = str()
        s_key = bin(key)
        s_key = s_key.lstrip('-0b')
        s_key = '0' * (8 - len(s_key)) + s_key

    else:
        raise error_xor_key.error_xor_key()
    return s_key

def name_file_Python(out):
    out=out.split('.')
    out=out[0]+"_P."+out[1]
    return out

def name_file_C(out):
    out=out.split('.')
    out=out[0]+"_C."+out[1]
    return out

def main_Logic(inF,outF,K):
    in_file = inF
    out_file = outF
    key = number_to_char_key(K)
    out_fileP=name_file_Python(out_file)
    out_fileC=name_file_C(out_file)

    in_file = in_file.encode('ascii')
    out_fileC = out_fileC.encode('ascii')
    key = key.encode('ascii')

    Time_E_D=time_xor.Time_xor()

    Time_E_D.startC=datetime.datetime.now()
    val1 = xor_dll.xor_extern_dll(in_file, out_fileC, key)
    Time_E_D.endC=datetime.datetime.now()


    Time_E_D.startP=datetime.datetime.now()
    val2 = xor_python.xor_python(in_file, out_fileP, key)
    Time_E_D.endP=datetime.datetime.now()

    if val1==False or val2 == False:
        raise error_xor_file.ErrorXorFile()
    return Time_E_D