import os
import time
from itertools import chain
from glob import glob
 
#linhas=str(0)
location = "/home/mint/Desktop/Logs"
 
while (True):
    print("1-Logins falhados")
    print("2-Mostrar logs por mês\n")
    escolha=int(input())
    c=0
    if escolha == 1:
            for linha in open("auth.log"):
                linha = linha.lower()
                letr="authentication failure"
                if letr in linha or "Authentication failure" in linha:
                    file = open("login.txt","a")
                    c=1
                    file.write(linha)
                    file.close()
            if c==1:
                print("Ficheiro criado com sucesso!")  
    if escolha == 2:
        palavra=input('Que mês deseja procurar?\n')
        for linha in open("auth.log"):
            if palavra in linha:
                if palavra == "Dec":
                    file = open("guarda_dezembro.txt","a")
                    file.write(linha)
                    file.close()
               
                if palavra == "Nov":
                    file2 = open("guarda_nov.txt","a")
                    file2.write(linha)
                    file2.close()
 
                if palavra == "Jan":
                    file3 = open("guarda_jan.txt","a")
                    file3.write(linha)

                    file3.close()
