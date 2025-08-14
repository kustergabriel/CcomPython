#include "calculadora.h"
#include <stdio.h>
#include <math.h>

// Fatorial
EXPORT unsigned long long fatorial(int n) {
    if (n < 0) return 0;
    unsigned long long result = 1;
    for (int i = 2; i <= n; i++)
        result *= i;
    return result;
}

// Potência
EXPORT double potencia(double base, double exp) {
    return pow(base, exp);
}

// Menor Múltiplo Comum (MMC)
EXPORT long long mmc(int a, int b) {
    if (a <= 0 || b <= 0) return 0;

    int maior = (a > b) ? a : b;
    long long m = maior;

    while (m % a != 0 || m % b != 0) {
        m++;
    }

    return m;
}

// Verificação de primo
EXPORT int ehPrimo(int n) {
    if (n < 2) return 0;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0)
            return 0;
    }
    return 1;
}
