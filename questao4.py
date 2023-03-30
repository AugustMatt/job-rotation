# Função para calcular o percentual de representação de cada estado no faturamento total da empresa
def percentualDeRepresentacao(faturamento):

    # Calcula o faturamento total
    faturamentoTotal = 0
    for dict in faturamento:
        faturamentoTotal += dict['valor']
    
    # Calcula o percentual de representação de cada estado E adiciona o percentual ao dicionario
    for dict in faturamento:
        dict['percentual'] = dict['valor']/faturamentoTotal
    
    # Como a questão não informa se eu devo retornar algum valor, vou apenas exibir o resultado
    # Exibe o resultado em porcentagem com 2 casas decimais
    for dict in faturamento:
        print(f'{dict["estado"]}: {dict["percentual"]*100:.2f}%')
        

if __name__ == "__main__":
    
    # Como a questão não informa um formado de entrada, vou assumir que seja um array de dicionarios
    # na seguinte forma: [{'estado': X, 'valor': V1}, {'estado': Y, 'valor': V2}, ...]

    # Tambem não foi informado o numero de casas decimais que devem ser exibidas, vou assumir que seja 2

    # Exemplo de entrada
    faturamento = [
        {
            'estado': 'SP', 
            'valor': 67836.43
        }, 
        {
            'estado': 'RJ', 
            'valor': 36678.66
        }, 
        {
            'estado': 'MG', 
            'valor': 29229.88
        }, 
        {
            'estado': 'ES', 
            'valor': 27165.48
        }, 
        {
            'estado': 'OUTROS', 
            'valor': 19849.53
        }
    ]

    percentualDeRepresentacao(faturamento)