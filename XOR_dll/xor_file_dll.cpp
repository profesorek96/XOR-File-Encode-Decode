#include "xor_file_dll.h"
#include <cstdio>
#include <cstring>
bool xor_crypt_encrypt(char * in_file,char *out_file,char *key)
{
	FILE *file = fopen(in_file, "rb");

	if (file != NULL)
	{
		FILE *encrypt_file = fopen(out_file, "wb");
		if (encrypt_file != NULL)
		{
			int sign, xor_sign, k = 0,len = strlen(key);
			do
			{
				if (k >= len)k = 0;
				sign = fgetc(file);
				xor_sign = key[k]^sign;
				k++;
				if (sign != EOF)fputc(xor_sign, encrypt_file);
			} while (sign != EOF);
			if (!(fclose(file))&&!(fclose(encrypt_file)))
				return true;
			else
				return false;
		}

		else
			return false;
	}
	else
		return false;
}