import funcs

perguntas = {
    1:'Agendar',
    2:'Cancelar',
    3:'Confirmar'
}
agendados = []
esl = ''

for c in perguntas.keys(): #Mostra as opções
    print(f'{c}: {perguntas[c]}')

while esl != 4:
    esl = int(input('Escolha uma das opções: '))
    if esl == 1:
        agendados.append(str(input('Precisaremos de alguns dados seus, digite seu nome e numero separadamente: ')).split())
        agendados.append('Des')

    elif esl == 2:
        funcs.cancel(agendados, numero=str(input('Digite seu numero: ')))

    elif esl == 3:
        num = str(input('Digite seu numero: '))
        sit = str(input('Qual sua situação?:  '))
        funcs.confirmation(agendados, num, sit)
