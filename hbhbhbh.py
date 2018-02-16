listaip=[]
log = r'pfsenselog.txt'
with open(log) as f:
    f = f.readlines()
for x in f:
    x = x.split()
    listaip.append(x[2])
print(listaip)
