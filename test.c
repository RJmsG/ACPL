#include <stdio.h>
void out(char *inp) {
printf("%s",inp);
}
void in(char *var) {
scanf("%s",var);
}
int main() {
int ac = 1;
out("test");
ac = 4;
char input[ac];
in(input);
out(input);
return 0;
}
