def verificarnum(numero):
    while not numero.isnumeric():
        numero = input('Diga um numero valido: ')
    return int(numero)

def verificarsimounao(res):
    while not (res == 'sim' or res == 'não'):
        res = input('Diga "sim" ou "não": ')
    return res

def verificaragua(ph,temp,sal):
    nivelph = ''
    niveltemp = ''
    nivelsal = ''
    if ph >= 7 and ph <= 9:
        nivelph = 'bom'
    elif ph < 7:
        nivelph = 'baixo'
    else:
        nivelph = 'alto'

    if temp >= 5 and temp <= 15:
        niveltemp = 'bom'
    elif temp < 5:
        niveltemp = 'baixo'
    else:
        niveltemp = 'alto'

    if sal >= 30 and sal <= 40:
        nivelsal = 'bom'
    elif sal < 30:
        nivelsal = 'baixo'
    else:
        nivelsal = 'alto'

    print(f'Detalhes da água:\n - PH: {ph}, nivel: {nivelph}\n - Temperatura: {temp}°C, nivel: {niveltemp}\n - Salinidade: {sal} gramas/litro, nivel: {nivelsal}')

    return [nivelph, niveltemp, nivelsal]

infos = ['ph', 'temp', 'sal']
tratbaixo = ['utilize um elevador de ph na área', 'Retirar a vida marinha da área enquanto limpa os residuos de lixo na superficie da água', 'Adicione uma solução salina na água']
tratalto = ['use a adição de um ácido fraco ou de um ácido forte diluído na água','Analise as correntes de água da área de acordo com a época do ano','adicione água salina magnetizada na área analisada']
def tratamento (lista):
    for i in range(len(lista)):
        if lista[i] == 'baixo':
            print(f'tratamento de {infos[i]} ({lista[i]}) \n - Orientação: {tratbaixo[i]} ')
        elif lista[i] == 'alto':
            print(f'tratamento de {infos[i]} ({lista[i]}) \n - Orientação: {tratalto[i]} ')
    return

def analisaragua ():
    ph = input('Digite o ph da água: ')
    novoph = verificarnum(ph)
    temp = input('Digite a temperatura da água(Celcius): ')
    novotemp = verificarnum(temp)
    sal = input('Digite a salinidade da água(grama/litro): ')
    novosal = verificarnum(sal)

    aguaverificada = verificaragua(novoph, novotemp, novosal)

    orientacoes = input('Você quer ver as orientações sobre como tratar a água?(Diga "sim" ou "não"): ')
    resposta = verificarsimounao(orientacoes)

    if resposta == 'sim':
        tratamento(aguaverificada)

    repetir = input('Você quer analisar outra água?(Diga "sim" ou "não"): ')
    repeticao = verificarsimounao(repetir)

    if repeticao == 'sim':
        analisaragua()


print('Bem-vindo ao   água!')
analisaragua()

print('Até mais')