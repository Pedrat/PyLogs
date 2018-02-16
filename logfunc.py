import os,time,sys,datetime
listasites=["netacad","trainingserver","9gag","anime","ccna","jpeg","png","gif"]
lista=[]
listaip=[]
counter=[]
counter2=[]
nome="PfSenseIPLogs"+datetime.datetime.now().strftime("%d-%m-%Y")+".txt"

for x in open("listaurl.txt",'r'):
    listasites.append(x)
def read():
    for x in open("listaurl.txt",'r'):
        listasites.append(x)


def pfanalise():
    try:
        log = r'pfsenselog.txt'
        with open(log) as f:
            f = f.readlines()
        for x in f:
            y = x.split()
            listaip.append(y[2])
        for x in set(listaip):
            counter.append(listaip.count(x))
            counter2.append(x)
        file=open(nome,'w')
        for x in range(len(counter2)):
            file.write("O ip {} acedeu {} vezes a internet.".format(counter2[x],counter[x])+"\n")
        file.close()
        del lista[:]
        del counter[:]
        del counter2[:]
        for y in listasites:
            for x in f:
                if y in x:
                    lista.append(y)
        for x in set(lista):
            counter.append(lista.count(x))
            counter2.append(x)
        for x in range(len(counter2)):
            print("{} {}".format(counter2[x],counter[x])+'\n')
        STOP=input("Press any key to continue...")
    except:
        sys.stdout.write("Algo não correu bem.\n")
        time.sleep(3)
        os.system("clear")
        sys.exit(0)
def update():
    file=open("listaurl.txt",'a')
    while 1:
        url=input("\nQual o url?")
        if url == "exit":
            break
        else:
            file.write(url+'\n')
    file.close()
    read()

#()
