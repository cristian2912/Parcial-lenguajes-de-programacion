#include <stdio.h>
#include <time.h>

long long fib(int n) {
    if (n <= 1) return n;
    return fib(n-1) + fib(n-2);
}

int main() {
    int n = 40;
    clock_t start = clock();
    long long result = fib(n);
    clock_t end = clock();

    double time_taken = (double)(end - start) / CLOCKS_PER_SEC;

    printf("Fibonacci(%d) = %lld\n", n, result);
    printf("Tiempo en C: %f segundos\n", time_taken);

    return 0;
}
