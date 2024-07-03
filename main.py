import os
mensagens= []
nome= input("Nome:")

while True:

    os.system ('cls')

if len(mensagens)>0:
    for m in mensagens:
        print(m['nome'],"-",m['texto'])
        print("_______")
    texto = input ("mensagem:")
elif "fim":
    print("Fim :)")

    mensagens.append ({"nome":nome,
                      "texto":texto
                      })