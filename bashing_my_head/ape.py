from pwn import *

context.log_level = "Critical"
connect = remote('cyberyoddha.baycyber.net', 10006)

print(connect.recvuntil('decrypt this').encode("utf-8"))

connect.close()
