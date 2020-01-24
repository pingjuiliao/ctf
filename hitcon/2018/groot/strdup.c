#include<stdio.h>
#include<string.h>

int main() {
    char buf[] = "hello world!\n";
    char* s = strdup(buf);
    printf("%s", s);
    printf("%p", s);
    return 0;
}
