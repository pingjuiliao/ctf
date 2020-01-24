#include <stdio.h>
#include <string.h>
typedef struct _name {
    char first[32] ;
    char last[32] ;
} name_t ;

int
main(void) {
    name_t n ;
    memset(&n, 0, sizeof(name_t)) ;
    strcpy(n.first,"hello") ;
    strcpy(n.last, "world") ;
    printf("first name : %s\n", n.first) ;
    printf(" last name : %s\n", n.last) ;
    return 0 ;
}
