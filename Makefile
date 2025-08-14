# Nome do executável DLL
DLL_NAME = calculadora.dll
C_SOURCES = calculadora.c
CC = gcc
CFLAGS = -shared -o $(DLL_NAME)

all: $(DLL_NAME)

# Compilação da DLL
$(DLL_NAME): $(C_SOURCES) calculadora.h
	$(CC) $(C_SOURCES) $(CFLAGS)

# Executar o Python
run:
	python calculadora_gui.py

clean:
	del $(DLL_NAME)
