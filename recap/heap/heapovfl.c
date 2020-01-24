#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>
char global_buf[10] ;

int
main(void) {
    char buf[50] ;
    char* s = malloc(10) ; 
    memset(buf, 0 , sizeof(buf));
    read(0, buf, sizeof(buf));
    strcpy(s, buf) ;
    puts(s);
    return 0 ;
}
