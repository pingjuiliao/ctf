#include <stdio.h>
#include <stdlib.h>

int safe() {
    int count = 1;
    int size = 8;
    int* count_ptr = &count;
    int* size_ptr = &size;

    char msg[100];

    puts("My mistake was letting you have too many characters.");
    puts("Don't worry, I fixed that now.");
    puts("You get 7 characters. Just enough to say 'no flag'.");
    puts("I'll say it with you...");
    fflush(stdout);

    while (count > 0) {
        fgets(msg, size, stdin);
        printf(msg);
        fflush(stdout);
        --count;

    }
    return 0;

}

int main() {
    safe();
    return 0;

}
