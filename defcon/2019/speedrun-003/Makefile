shellcode64: shellcode.S
	gcc -m64 -c shellcode.S -o shellcode.o
	gcc -m64 shellcode.o -o shellcode.exe
	objcopy -S -O binary -j .text shellcode.o shellcode.bin
clean:
	rm shellcode.exe shellcode.bin shellcode.o
