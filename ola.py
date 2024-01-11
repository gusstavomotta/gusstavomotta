import random
ja_sorteados = [11]

def sorteia():
    while True:
        sorteio = random.randrange(1,11)
        if sorteio not in ja_sorteados:
            print(sorteio)
            ja_sorteados.append(sorteio)
            

        else:
            continue
        
    if ja_sorteados.lenght() == 11:
        return
        
sorteia()