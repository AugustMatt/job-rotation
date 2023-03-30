# Função para inverter string
def inverterString(string):

    # Adquire o array de caracteres da string
    array = list(string)

    # percorre o array de trás para frente colocando o resultado em outro array
    array_invertido = []
    for i in range(len(array)-1, -1, -1):
        array_invertido.append(array[i])

    # Transforma o array invertido em string
    string_invertida = ''.join(array_invertido)

    return string_invertida
    


if __name__ == "__main__":
    string = input('Digite uma string: ')
    print(inverterString(string))