import sys
import hmac
import hashlib

s = "Hello, world!"
dataLen = len(s)

sys.stdout.buffer.write(int.to_bytes(dataLen, 4, 'little'))


sys.stdout.buffer.write(s.encode())

key = bytearray.fromhex("63bd8135")

h = hmac.new(key, s.encode(), hashlib.sha256).digest()

sys.stdout.buffer.write(h)