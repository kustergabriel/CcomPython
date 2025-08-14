import ctypes
import os
import tkinter as tk
from tkinter import messagebox

# Carrega a DLL
library_name = 'calculadora.dll' if os.name == 'nt' else 'calculadora.so'
calc = ctypes.CDLL(f'./{library_name}')

# Define tipos de argumentos e retorno
calc.fatorial.argtypes = [ctypes.c_int]
calc.fatorial.restype = ctypes.c_ulonglong

calc.potencia.argtypes = [ctypes.c_double, ctypes.c_double]
calc.potencia.restype = ctypes.c_double

calc.mmc.argtypes = [ctypes.c_int, ctypes.c_int]
calc.mmc.restype = ctypes.c_longlong

calc.ehPrimo.argtypes = [ctypes.c_int]
calc.ehPrimo.restype = ctypes.c_int

# Pega a entrada do usuario
def getEntrada(entry_widget, tipo=int, default=0):
    try:
        return tipo(entry_widget.get())
    except ValueError:
        if tipo == int:
            messagebox.showerror("Erro", "Número 1 inválido!")
            return None
        else:
            return default

def calcFatorial(entrada1, resultado):
    n = getEntrada(entrada1, int)
    if n is not None:
        res = calc.fatorial(n)
        resultado.config(text=f"Resultado: {res}")

def calcPotencia(entrada1, entrada2, resultado):
    base = getEntrada(entrada1, float)
    exp = getEntrada(entrada2, float)
    if base is not None:
        res = calc.potencia(base, exp)
        resultado.config(text=f"Resultado: {res}")

def calcMmc(entrada1, entrada2, result_label):
    a = getEntrada(entrada1, int)
    b = getEntrada(entrada2, int)
    if a is not None and b is not None:
        res = calc.mmc(a, b)
        result_label.config(text=f"MMC({a}, {b}) = {res}")

def calcEhPrimo(entrada1, resultado):
    n = getEntrada(entrada1, int)
    if n is not None:
        res = calc.ehPrimo(n)
        resultado.config(text=f"{n} é primo? {'Sim' if res else 'Não'}")

def main():
    root = tk.Tk()
    root.title("Calculadora C + Python")

    tk.Label(root, text="Número 1:").grid(row=0, column=0, padx=5, pady=5)
    entrada1 = tk.Entry(root)
    entrada1.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(root, text="Número 2 (se necessário):").grid(row=1, column=0, padx=5, pady=5)
    entrada2 = tk.Entry(root)
    entrada2.grid(row=1, column=1, padx=5, pady=5)

    resultadoConta = tk.Label(root, text="Resultado: ", font=("Helvetica", 14))
    resultadoConta.grid(row=4, column=0, columnspan=2, pady=10)

    tk.Button(root, text="Fatorial", command=lambda: calcFatorial(entrada1, resultadoConta)).grid(row=2, column=0, pady=5)
    tk.Button(root, text="Potência", command=lambda: calcPotencia(entrada1, entrada2, resultadoConta)).grid(row=2, column=1, pady=5)
    tk.Button(root, text="MMC", command=lambda: calcMmc(entrada1, entrada2, resultadoConta)).grid(row=3, column=0, pady=5)
    tk.Button(root, text="É primo?", command=lambda: calcEhPrimo(entrada1, resultadoConta)).grid(row=3, column=1, pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    main()
