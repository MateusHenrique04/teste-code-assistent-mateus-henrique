# README

Este repositório contém uma função simples em Python para verificar se um número é primo.

## Arquivo principal

- `ex1.py`: implementação de `is_prime(number)`.
- A função retorna `True` quando o valor informado é primo e `False` quando não é.

## Como a função funciona

1. Números menores ou iguais a 1 não são primos.
2. O número 2 é o único número primo par.
3. Números pares maiores que 2 não são primos.
4. Para números ímpares maiores que 2, o código testa divisores ímpares a partir de 3.
5. A verificação vai apenas até a raiz inteira de `number` com `math.isqrt(number)`.

## Por que essa implementação é eficiente

- Elimina divisões por números pares.
- Verifica apenas até a raiz quadrada do número.
- Usa `range(3, limit + 1, 2)` para testar apenas divisores ímpares.

## Execução

Execute o arquivo diretamente:

```bash
python ex1.py
```

Isso imprime se cada número da lista de exemplo é primo.

## Saída esperada

- `1 is prime: False`
- `2 is prime: True`
- `3 is prime: True`
- `4 is prime: False`
- `17 is prime: True`
- `18 is prime: False`
- `19 is prime: True`
- `20 is prime: False`
