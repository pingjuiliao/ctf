#include<stdio.h>
#include<string.h>

int
main(void) {
    char buf[20];
    int i;
    memset(buf, 0x90, sizeof(buf));
    fgets(buf, 20, stdin) ;
    for ( i = 0 ; i < 20 ; ++i ) {
        printf("%c", buf[i]);
    }
    puts("");
    return 0;
}
