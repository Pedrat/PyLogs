import os,time,sys,datetime
lista=[]
listaip=[]
counter=[]
counter2=[]
os.system("clear")
sys.stdout.write("Este Programa ira demonstrar quantos IP's ficaram em logs, e o URL's que foram acedidos.\n")
nome="PfSenseLogs"+datetime.datetime.now().strftime("%d-%m-%Y")+".txt"
time.sleep(2)

if __name__ =="__main__":
    try:
        log = r'pfsenselog.txt'
        with open(log) as f:
            f = f.readlines()
        for x in f:
            y = x.split()
            listaip.append(y[2])
    #print(listaip)
        for x in set(listaip):
            counter.append(listaip.count(x))
            counter2.append(x)
        for x in range(len(counter2)):
            print("O ip {} acedeu {} vezes a internet.".format(counter2[x],counter[x]))
            lista.append("O ip {} acedeu {} vezes a internet.".format(counter2[x],counter[x]))
        file=open(nome,'w') #Cria o ficheiro se não existir
        for x in lista:
            file.write(x+"\n")
        file.close()
        del lista[:]

    except:
        sys.stdout.write("Algo não correu bem.\n")
        time.sleep(3)
        os.system("clear")
        sys.exit(0)
