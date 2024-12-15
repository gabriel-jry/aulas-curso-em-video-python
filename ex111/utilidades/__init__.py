def dobro(n=0,f=False):
    if f:
        return converter(n+n)
    else:
        return n + n

def metade(n=0,f=False):
    if f:
        return converter(n/2)
    else:
        return n / 2

def aumentar(n=0,p=0,f=False):
    if f:
        return converter(n+(n*p)/100)
    else:
        return n + (n * p) / 100

def diminuir(n=0,p=0,f=False):
    if f:
        return converter(n-(n*p)/100)
    else:
        return n - (n * p) / 100

def converter(n=0, s='R$'):
    return f'{s}{n:.2f}'.replace('.',',')

w = False
p = float(input('\npreço: '))
d = float(input("desconto: "))
while True:
    f = str(input("deseja ver formatado? ")).lower()[0]
    if f in "sn":
        if f == "s":
            w = True
            break
        else:
            w = False
            break
    else:
        print("responda apenas com, sim ou não.\n")
