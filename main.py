import os
from time import sleep


ultima = False
while True:
    while True:
        os.system("clear")
        questao1 = str(input("1-A que tipo de heroi o Capitao vitorino e associado?\n\nA)Batman\nB)Don Quixote\nC)Demolidor\nDigite a alternativa correta:")).lower()
        if questao1 == 'b':
            print("Voce acertou!!!")
            
        else:
            print("Voce errou, tente novamente!")
            sleep(3)
            break
        



        os.system("clear")
        questao1 = str(input("2-Quem tira o Capitao Vitorino da prisao?\n\nA)Tenente Mauricio\nB)Antonio Silvino\nC)Coronel Jose Paulino\nDigite a alternativa correta:")).lower()
        if questao1 == 'c':
            print("Voce acertou!!!")
            
        else:
            print("Voce errou, tente novamente!")
            sleep(3)
            break




        os.system("clear")
        questao1 = str(input("3-Quem se mata no final?\n\nA)Mestre Jose Amaro\nB)Capitao Vitorino\nC)Capitao Lula\nDigite a alternativa correta:")).lower()
        if questao1 == 'a':
            print("Voce acertou!!!")
            
        else:
            print("Voce errou, tente novamente!")
            sleep(3)
            break




        os.system("clear")
        questao1 = str(input("4-Quem tinha a fama de lobisomem?\n\nA)Jose Amaro\nB)Antonio Silvino\nC)Tenente Mauricio\nDigite a alternativa correta:")).lower()
        if questao1 == 'a':
            print("Voce acertou!!!")
            
        else:
            print("Voce errou, tente novamente!")
            sleep(3)
            break





        os.system("clear")
        questao1 = str(input("5-Quem era lider do cangaco?\n\nA)Antonio Silvino\nB)Jose Amaro\nC)Capitao Vitorino\nDigite a alternativa correta:")).lower()
        if questao1 == 'a':
            print("Voce acertou!!!")
            ultima = True
        else:
            print("Voce errou, tente novamente!")
            sleep(3)
            break
    
        if ultima == True:
            os.system("clear") 
            print("Voce Acertou todas!!!")
            print("FIM")
            sleep(3)
            exit()




