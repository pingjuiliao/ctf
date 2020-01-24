#include<stdio.h>
#include<unistd.h>

void
pop_shell(void) {
    execve("/bin/sh", 0, 0) ;
}




int
main(int argc, char** argv) {
    char buf[100] ;
    read(0, buf, sizeof(buf));
    printf(buf);
    puts("bye, bye !");
    return 0;
}
