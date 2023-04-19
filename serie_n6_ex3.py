# Les bibliotheques : 

    #1 array:
from numpy import array
T = array([int()]*13)
    #2 randint:
from random import randint

# Algorithme de procedure saisie :


def saisie() :
    n = int(input("Donner la taille de tableau de 2 a 25  :  "))
    while n<=2 or n>=25 :
        n = int(input("Donner la taille de tableau de 2 a 25  :  "))
    return(n)

# Algorithme de procedure remplire:


def remplire(n, T) :
    for i in range (n) :
        T[i] = randint(10,25)
    for i in range (n) :
        print("T["+ str(i) +"]=  ",T[i])


# Algorithme de procedure affichage

def affichage(n, T):
    for i in range (n-1,-1,-1):
        print("T["+ str(n-i) +"]=  ",T[i])


# Algorithme inverse

n = saisie()
print("Le tableau : ")
remplire(n, T)

print("=" * 50)

print("L'inverse de tableau : ")
affichage(n, T)