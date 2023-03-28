#!/usr/bin/env python3

import sys

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]

#TR: ASCII kodlarını içeren bir liste veriliyor. "ords" listesi.
#EN: There is a ASCII numbers list with the name "ords".

print("Here is your flag:")

print("".join(chr(o ^ 0x32) for o in ords))
