import sys

b = "zhwan"
b= b.encode("utf-8")
grade = "A+"
grade = grade.encode()
sys.stdout.buffer.write(b+b"\x00\x00\x00\x00\x00" + grade + b"\x00")