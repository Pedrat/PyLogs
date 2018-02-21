import os,sys,time
import logfunc


os.system("clear")
sys.stdout.write("Este Programa ira demonstrar(em um ficheiro) quantos IP's ficaram em logs\n e o URL's que foram acedidos.\n")
if __name__ =="__main__":
    while 1:
        opc=input("1-IP's e Mostrar os URL's\n2-Adicionar URL's ao ficheiro\n")
        #print(logfunc.listasites)
        if opc=="1":
            os.system("clear")
            logfunc.pfanalise()
        elif opc == "2":
            logfunc.update()
        else:
            continue
