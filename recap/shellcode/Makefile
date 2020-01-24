32: shellcode.S
	gcc -m32 -c shellcode.S -o shellcode.o
	gcc -m32 shellcode.o -o shellcode.exe
	objcopy -S -O binary -j .text shellcode.o shellcode.bin
