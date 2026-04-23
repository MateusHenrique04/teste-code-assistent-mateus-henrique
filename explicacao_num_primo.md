# Explicação da Função `is_prime`

Esta função verifica se um número é primo usando Python. Um número primo é um inteiro maior que 1 que não tem divisores positivos além de 1 e ele mesmo.

## Código da Função

```python
def is_prime(number: int) -> bool:
    """Check if a number is prime.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

    Args:
        number: The integer to check for primality.

    Returns:
        True if the number is prime, False otherwise.

    Raises:
        TypeError: If number is not an integer.
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")

    if number < 2:
        return False

    if number in (2, 3):
        return True

    if number % 2 == 0 or number % 3 == 0:
        return False

    # Check for factors from 5 onwards, skipping even numbers and multiples of 3
    factor = 5
    while factor * factor <= number:
        if number % factor == 0 or number % (factor + 2) == 0:
            return False
        factor += 6

    return True
```

## Explicação Linha a Linha

1. **`def is_prime(number: int) -> bool:`**  
   Define a função chamada `is_prime` que recebe um parâmetro `number` do tipo inteiro e retorna um booleano. O uso de type hints melhora a legibilidade e permite verificações estáticas.

2-12. **Docstring (linhas 2-12):**  
   Uma docstring detalhada em estilo Google, explicando o propósito da função, argumentos, retorno e possíveis exceções. Isso segue princípios de clean code para documentação clara.

13. **`if not isinstance(number, int):`**  
   Verifica se o input é um inteiro. Se não for, lança uma exceção para garantir entrada válida.

14. **`raise TypeError("Input must be an integer")`**  
   Lança uma TypeError se o input não for inteiro, promovendo robustez.

15. **`if number < 2:`**  
   Verifica se `number` é menor que 2. Números primos são maiores que 1.

16. **`return False`**  
   Retorna `False` para números menores que 2.

17. **`if number in (2, 3):`**  
   Verifica se `number` é 2 ou 3, que são primos.

18. **`return True`**  
   Retorna `True` para 2 e 3.

19. **`if number % 2 == 0 or number % 3 == 0:`**  
   Elimina números pares e múltiplos de 3 rapidamente.

20. **`return False`**  
   Retorna `False` se for par ou múltiplo de 3.

21. **`# Check for factors from 5 onwards, skipping even numbers and multiples of 3`**  
   Comentário explicativo para o loop, seguindo clean code.

22. **`factor = 5`**  
   Inicializa `factor` com 5, usando um nome descritivo.

23. **`while factor * factor <= number:`**  
   Loop otimizado até a raiz quadrada de `number`.

24. **`if number % factor == 0 or number % (factor + 2) == 0:`**  
   Verifica divisibilidade por `factor` ou `factor + 2`.

25. **`return False`**  
   Retorna `False` se encontrar divisor.

26. **`factor += 6`**  
   Incrementa `factor` em 6 para pular candidatos desnecessários.

27. **`return True`**  
   Retorna `True` se nenhum divisor for encontrado.

## Princípios de Clean Code Aplicados

- **Nomes descritivos:** `number` em vez de `n`, `factor` em vez de `i`.
- **Type hints:** Indicam tipos para melhor legibilidade e ferramentas de análise.
- **Docstring completa:** Documentação clara e padronizada.
- **Validação de entrada:** Verifica tipo do input para robustez.
- **Comentários explicativos:** Explicam lógica complexa sem ser verbosa.
- **Estrutura clara:** Uso de early returns e separação de responsabilidades.

## Como Usar

Para usar a função, importe-a e chame-a com um número inteiro:

```python
from exercicio1 import is_prime

print(is_prime(17))  # True
print(is_prime(18))  # False

# Exemplo com erro de tipo
try:
    is_prime(3.5)
except TypeError as e:
    print(e)  # Input must be an integer
```

## Otimizações

Esta implementação é eficiente para números grandes, pois:
- Elimina rapidamente números pares e múltiplos de 3.
- Verifica apenas até a raiz quadrada de `number`.
- Pula candidatos desnecessários incrementando `factor` em 6.
- Usa early returns para sair cedo em casos óbvios.