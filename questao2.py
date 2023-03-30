# Função para verificar se o numero n está na sequencia de Fibonacci
def verifyIfInFibonacci(n)->bool:

    # Se o nuemro for 0 ou 1, ele está na sequencia
    if n == 0:
        return True
    elif n == 1:
        return True
    
    # Caso contrario calcula a sequencia de Fibonacci até que o numero seja maior que n
    # Se for igual, retorna True, caso contrario, retorna False
    else:
        a = 0
        b = 1
        c = 0
        while c < n:
            c = a + b
            a = b
            b = c
            if c == n:
                return True
        return False

if __name__ == "__main__":
    n = int(input('Digite um numero: '))
    if verifyIfInFibonacci(n):
        print('O numero %d está na sequencia de Fibonacci' % n)
    else:
        print('O numero %d não está na sequencia de Fibonacci' % n)