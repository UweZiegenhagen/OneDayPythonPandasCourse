    #include<stdio.h>
    long add(long a, long b){
        long ergebnis;
        ergebnis = a + b;
        return ergebnis;}

    int main(){
       int a, b, c;
       printf("Geben Sie zwei Zahlen ein\n");
       scanf("%d%d", &a, &b);
       long meinergebnis = add(a,b);
       printf("Summe der Zahlen = %d\n", meinergebnis);
       return 0;}
