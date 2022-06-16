import funcs

perguntas = {
    1:'Agendar',
    2:'Cancelar',
    3:'Confirmar',
    4:'Mostrar Registrados'
}
agendados = []
esl = ''

for c in perguntas.keys(): #Mostra as opções
    print(f'{c}: {perguntas[c]}')

while esl != 5:
    esl = int(input('Escolha uma das opções: '))
    if esl == 1:
        agendados.append(str(input('Precisaremos de alguns dados seus, digite seu nome e numero separadamente: ')).split())

    elif esl == 2:
        funcs.cancel(agendados, numero=str(input('Digite seu numero: ')))
###dwadwa
    elif esl == 3:
        num = str(input('Digite seu numero: '))
        sit = str(input('Qual sua situação?:  '))
        funcs.confirmation(agendados, num, sit)

    elif esl == 4:
        num = str(input('Digite seu numero para verificar o registro: ')).strip()
        print(funcs.show_register(agendados, num))