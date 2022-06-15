def cancel(agenda, numero):
    for c in range(0, len(agenda)):
        if agenda[c][1] == numero:
            agenda.remove(agenda[c])
            break

def confirmation(agenda, numero, situacao):
    for c in range(0, len(agenda)):
        if agenda[c][1] == numero:
            agenda[c].append(situacao)
            break

def show_register(agenda, numero):
    for c in range(0, len(agenda)):
        if agenda[c][1] == numero:
            return f'Nome: {agenda[c][0]}, Numero: {agenda[c][1]}'

def NestedIndex(termo, agenda):
    for c in range(0, len(agenda)): #Run each list
        for k in range(0, len(agenda[c])): #Run each term in the lisk 'c'
            if agenda[c][k] == termo: #Check if the term is the specified term
                ListPos, TermPos = c, k
                return ListPos, TermPos

            #Utilization example, is this the most efficient way to do this? Offcourse no, but it will help
            #nums = NestedIndex(teste(termo, agenda))
            #print(lista[nums[0]][nums[1]])