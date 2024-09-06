def is_fibonacci(n):
    a, b = 0, 1
    while b <= n:
        if b == n:
            return True
        a, b = b, a + b
    return False

numero = int(input("Informe um numero: "))

if is_fibonacci(numero):
    print(f"O numero {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O numero {numero} não pertence à sequência de Fibonacci.")

