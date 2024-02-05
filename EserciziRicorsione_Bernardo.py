#Calcolare il fattoriale di un numero;

 #Con il ciclo for

def fattoriale1(n):
    x=1
    for j in range(1, n + 1):
        x*=j
    return x

#print(fattoriale1(5))

#Facciamolo con la ricorsione
def fattoriale(n):
    risultato=n
    if n==0:
        return 1
    else:
        risultato=risultato*fattoriale(n-1)
    return risultato

# ------------------------------------------------------------------------------------------------------
#Verificare se una parola è un palindromo;

def palindromo(x):
    if len(x)%2==1:
        a=int((len(x)-1)/2)
        b=int((len(x)+1)/2)
        x=x[0:a]+x[b:len(x)+1]
        print(x)
    for j in range(len(x)):
        if x[j]==x[-(j+1)]:
            a=True
        else:
            return False
    return a
#print(palindromo('assa'))  #Dovremmo ottenere True


#Facciamolo con la ricorsione:
def palindromo1(parola):
    n=len(parola)
    m=parola
    if n!=0:
        x=bool(m[0]==m[-1])
        if not x:
         return False
        else:
            return palindromo1(parola[1:n-1])
    else:
        return True

def palindromo2(parola,a=True):
    n=len(parola)
    if n<=1:
        return True
    elif parola[0]==parola[-1]:
        a=True
        return palindromo2(parola[1:n-1])
    else:
        return False
#print(palindromo2('astsa'))

def palindromo3(parola,x=''):
    n=len(parola)
    if len(parola)==0:
        return x[::-1]==x
    else:
        x+=parola[-1]
        return palindromo3(parola[0:n-1],x)
#print(palindromo3('ciao'))

# -------------------------------------------------------------------------------------------------------------
# ESERCIZI FIBONACCI
def fiboex(n):
    x=[1 for j in range(n)]
    for j in range(2,n):
        x[j]=x[j-1]+x[j-2]
    return x
#print(fiboex(8)


def fiboex1(n,lista=[0,1]):
    if len(lista) == n:   #Condizione Base
        return lista
    else:
        x=lista[-1]+lista[-2]
        lista.append(x)
        return fiboex1(n,lista)
#print(fiboex1(8))

#-----------------------------------------------------------------------------------------------------------
#Calcolo del MCD
def massimo_comun_div(n,m):
    r=1
    while r>=1:
        if m>=n:
            r=m%n
            if r==0:
                return n
            k=m//n
            m=k
            n=r
        else:
            r = n % m
            if r==0:
                return m
            k = n // m
            n = k
            m = r
    return k
print(massimo_comun_div(1,1))


#Proviamo con la ricorsione

def massimo_comun_div_ric(m,n):
    r=m % n
    if m>=n:
        if r == 0:
            return m
        m=m//n
        n=r
        return massimo_comun_div(m, r)
    else:
        if r == 0:
            return m
        m=m//n
        n=r
        return massimo_comun_div(m, r)

print(massimo_comun_div_ric(36,8))
