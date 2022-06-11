def cancel(agenda, numero):
    for c in range(0, len(agenda)):
        if agenda[c][1] == numero:
            agenda.remove(agenda[c])
            break

def confirmation(agenda, numero, situacao):
    for c in range(0, len(agenda)):
        if agenda[c][1] == numero:
            agenda[c].append(situacao)