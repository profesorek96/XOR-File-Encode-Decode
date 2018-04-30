#pragma once  

#ifdef TESTLIB_EXPORTS  
#define LIB_API __declspec(dllexport)   
#else  
#define LIB_API __declspec(dllimport)   
#endif  

extern "C"
{
	bool LIB_API xor_crypt_encrypt(char * plikXorowany, char *plikWyjsciowy, char *klucz);
}

