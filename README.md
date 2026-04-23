# README

Este arquivo descreve o funcionamento do código Python presente em `ex1.py`, que implementa uma função para verificar números primos.

## O que o código faz

A função `is_prime(n)` determina se um número inteiro `n` é primo. Ela retorna `True` se `n` for primo e `False` caso contrário.

## Explicação do código em `ex1.py`

1. `# ex1.py`
   - Comentário indicando o nome do arquivo.

2. `def is_prime(n: int) -> bool:`
   - Declaração da função `is_prime`.
   - Recebe um inteiro `n` e retorna um valor booleano.

3. `    """Return True if n is a prime number, otherwise False."""`
   - Docstring explicando o propósito da função.

4. `    if n <= 1:`
   - Verifica se `n` é menor ou igual a 1.

5. `        return False`
   - 0, 1 e números negativos não são primos.

6. `    if n <= 3:`
   - Verifica se `n` é 2 ou 3.

7. `        return True`
   - 2 e 3 são primos.

8. `    if n % 2 == 0:`
   - Verifica se `n` é divisível por 2.

9. `        return False`
   - Números pares maiores que 2 não são primos.

10. `    i = 3`
    - Inicializa o divisor `i` com 3.

11. `    while i * i <= n:`
    - Loop que verifica divisores ímpares até a raiz quadrada de `n`.

12. `        if n % i == 0:`
    - Verifica se `n` é divisível por `i`.

13. `            return False`
    - Se existir um divisor, `n` não é primo.

14. `        i += 2`
    - Avança para o próximo número ímpar.

15. `    return True`
    - Se não foi encontrado divisor, `n` é primo.

## Execução direta do arquivo

No final do arquivo, existe um bloco:

```python
if __name__ == "__main__":
    for value in [1, 2, 3, 4, 17, 18, 19, 20]:
        print(f"{value} is prime: {is_prime(value)}")
```

Isso significa que, ao executar `python ex1.py`, o programa testa alguns valores e imprime se cada um é primo.

## Exemplo de saída

- `1 is prime: False`
- `2 is prime: True`
- `3 is prime: True`
- `4 is prime: False`
- `17 is prime: True`
- `18 is prime: False`
- `19 is prime: True`
- `20 is prime: False`
