# Explicação linha por linha do código em `ex2.py`

1. `from typing import Iterable, Tuple`  
   Importa tipos `Iterable` e `Tuple` do módulo `typing` para anotações de tipo.

2. `def calculate_statistics(values: Iterable[float]) -> Tuple[float, float, float, float]:`  
   Define uma função que recebe um iterável de floats e retorna uma tupla de quatro floats (total, média, máximo, mínimo).

3. `"""Return total, average, maximum, and minimum for the given values."""`  
   Docstring explicando o propósito da função.

4. `values_list = list(values)`  
   Converte o iterável `values` em uma lista para permitir operações como `sum`, `max`, etc.

5. `if not values_list:`  
   Verifica se a lista está vazia.

6. `raise ValueError("The input list must contain at least one value.")`  
   Lança um erro se a lista estiver vazia, exigindo pelo menos um valor.

7. `total = sum(values_list)`  
   Calcula a soma de todos os valores na lista.

8. `average = total / len(values_list)`  
   Calcula a média dividindo a soma pelo número de elementos.

9. `maximum = max(values_list)`  
   Encontra o valor máximo na lista.

10. `minimum = min(values_list)`  
    Encontra o valor mínimo na lista.

11. `return total, average, maximum, minimum`  
    Retorna os quatro valores calculados como uma tupla.

12. `def main() -> None:`  
    Define a função principal que executa o programa.

13. `numbers = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]`  
    Cria uma lista de números inteiros para teste.

14. `total, average, maximum, minimum = calculate_statistics(numbers)`  
    Chama a função `calculate_statistics` com a lista e desempacota os resultados.

15. `print("total:", total)`  
    Imprime o total.

16. `print("media:", average)`  
    Imprime a média (em português, "média").

17. `print("maior:", maximum)`  
    Imprime o maior valor.

18. `print("menor:", minimum)`  
    Imprime o menor valor.

19. `if __name__ == "__main__":`  
    Verifica se o script está sendo executado diretamente (não importado).

20. `main()`  
    Chama a função `main` para iniciar o programa.