### Trabalho desenvolvido por: Charllynson Carvalho, Gabriel Kuster e Luana Montilha

### Calculadora com integração C + Python

O programa principal, em Python, fornece a interface do usuário, enquanto as funções de cálculo mais intensivas (fatorial, potência, MMC e verificação de número primo) são implementadas em uma biblioteca C e chamadas dinamicamente.

-----

#### Requisitos

Para executar este projeto, você precisará ter:

  * **Python 3.x**
  * **Um compilador C**.
  * A biblioteca padrão do Python `tkinter` para a interface gráfica.
  * A biblioteca padrão do Python `ctypes` para a integração.

-----

#### Estrutura do Projeto

O projeto é composto por dois arquivos principais:

  * `calculadora.c`: O código-fonte em C que contém as funções matemáticas.
  * `calculadora.py`: O script em Python que cria a interface gráfica e chama as funções C.

-----

#### 1\. Compilando o Código C

Primeiro, o código C precisa ser compilado em uma biblioteca dinâmica (DLL no Windows, SO no Linux/macOS) para que o Python possa acessá-lo.

Abra o terminal na pasta do projeto e execute o comando:

**No Windows (com MinGW):**

```bash
mingw32-make
```

Após a compilação, um arquivo chamado `calculadora.dll` (Windows) será criado na mesma pasta.

-----

#### 2\. Executando a Calculadora

Com a biblioteca compilada, basta executar o script Python.

```bash
mingw32-make run
```

Isso abrirá uma janela da calculadora onde você pode inserir números e usar os botões para chamar as funções.
