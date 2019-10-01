# XOR-File-Encode-Decode
## Table of contents
* [__General info__](#general-info)
* [__Screenshots__](#screenshots)
* [__Technologies__](#technologies)
* [__Setup__](#setup)
* [__Status__](#status)
* [__License__](#license)

## General info
This program encrypts or decrypts the file using the xor method. The encryption and decryption functions were written in both C and Python. Both functions open the file and process it. The result is an output file.

The GUI was created using the Tkinter library. The code written in C was compiled as a dynamic library and python calls functions from this file using the Cytpes package.

The second goal of this project is to compare python and C speed.

As you can see, encryption/decryption in python is 3 times slower than in C

## Screenshots
![Example screenshot 1](https://github.com/profesorek96/XOR-File-Encode-Decode/blob/master/screenshot/screenshot-1.jpg)

![Example screenshot 1](https://github.com/profesorek96/XOR-File-Encode-Decode/blob/master/screenshot/screenshot-2.jpg)


## Technologies
* __C++__
* __Python 3__

## Setup
1. Pull repository
2. Open file ./XOR_dll/xor_file.sln in Visual Studio 2017
3. Compile this project to 64 bit relase
4. Copy compile dll to ./Python3
5. Run ./Python3/GUI.py
6. Finished. Use this program :)

## Status
Project is: _finished_

## License
See `LICENSE.md`.
