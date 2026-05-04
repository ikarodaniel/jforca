def jogar_forca():
    print("---------------------------------------")
    print("----Bem vindo ao jogo da Forca-----")
    print("---------------------------------------")
    
    palavra_secreta = "processador"
    letras_acertadas = ["_","_","_","_","_","_","_","_","_","_","_"]
    perdeu = False
    acertou = False
    
    while(not perdeu and not acertou):
        chute = input("Escreva uma letra: ")
        chute = chute.strip()
        
        #Index define a posição da letra 
        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra 
            index = index + 1
            print(letras_acertadas)
        
        
        
        
        
if(__name__ == "__main__"):
    jogar_forca()