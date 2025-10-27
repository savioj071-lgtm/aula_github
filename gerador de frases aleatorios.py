import random

sujeitos = ["O gato", "Minha avó", "Um robô", "A professora", "O dragão"]
verbos = ["comeu", "quebrou", "descobriu", "construiu", "pintou"]
objetos = ["um carro", "a lua", "um sanduíche", "um castelo", "o computador"]

def gerar_frase():
    sujeito = random.choice(sujeitos)
    verbo = random.choice(verbos)
    objeto = random.choice(objetos)
    return f"{sujeito} {verbo} {objeto}."

# Gera 5 frases aleatórias
for _ in range(5):
    print(gerar_frase())

print("essa é a frase final")
