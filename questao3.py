import json

# Função que recebe um dicionario com os valores do faturamento por dia de uma empresa e retorna
# o dia com maior faturamento, o dia com o menor faturamento e o numero de dias com em que o faturamento
# foi superior a media
def analiseFaturamento(faturamento):
    maximoFaturamento = maxValue(faturamento, 'valor')
    minimoFaturamento = minValue(faturamento, 'valor')
    diasAcimaDaMedia = faturamentosAcimaDaMedia(faturamento, 'valor')
    return maximoFaturamento['valor'], minimoFaturamento['valor'], diasAcimaDaMedia

# Retorna o dicionario com o maior valor de uma chave
def maxValue(listOfDicts, key)->dict:
    max = 0
    max_dict = {}
    for dict in listOfDicts:
        if dict[key] > max:
            max = dict[key]
            max_dict = dict
    return max_dict

# Retorna o dicionario com o menor valor de uma chave
def minValue(listOfDicts, key)->dict:
    min = float('inf')
    min_dict = {}
    for dict in listOfDicts:
        if dict[key] < min:
            min = dict[key]
            min_dict = dict
    return min_dict

# Retorna o numero de dias com faturamento acima da media
def faturamentosAcimaDaMedia(listOfDicts, key)->int:

    # calcula a media dos faturamentos 
    # ignorando os dias cujo fatuamento é 0
    soma = 0
    dias = 0
    for dict in listOfDicts:
        if dict[key] != 0:
            soma += dict[key]
            dias += 1

    media = soma/dias

    # conta quantos dias tem faturamento acima da media
    count = 0
    for dict in listOfDicts:
        if dict[key] > media:
            count += 1

    return count
    
if __name__ == "__main__":
    faturamento = json.load(open('dados.json'))
    faturamentoMaximo, faturamentoMinimo, diasAcimaDaMedia = analiseFaturamento(faturamento)
    print(f'Faturamento maximo: {faturamentoMaximo}')
    print(f'Faturamento minimo: {faturamentoMinimo}')
    print(f'Dias com faturamento acima da media: {diasAcimaDaMedia}')