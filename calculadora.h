#ifndef CALCULADORA_H
#define CALCULADORA_H

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

// Declarações das funções exportadas
EXPORT unsigned long long fatorial(int n);
EXPORT double potencia(double base, double exp);
EXPORT long long mmc(int a, int b);
EXPORT int ehPrimo(int n);

#endif