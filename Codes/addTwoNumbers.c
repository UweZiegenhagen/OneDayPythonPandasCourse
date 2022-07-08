    #include<stdio.h>
    long add(long a, long b){
        long result;
        result = a + b;
        return result;}

    int main(){
       int a, b, c;
       printf("Enter two numbers\n");
       scanf("%d%d", &a, &b);
       long myresult = add(a,b);
       printf("Sum of numbers = %d\n", myresult);
       return 0;}
