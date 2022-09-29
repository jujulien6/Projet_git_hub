def multiplication (a,b):
    print("Multiplication : ", a * b)

def division (a,b):
    if(a>b):
        print("Division : ", a / b)
    else:
        print("L'opération n'est pas possible")

def soustraction(a,b):
    print("Soustraction : ", a - b)

def addition(a,b):
    print("Addition : ", a + b)

def affichage():
    valeur1 = int(input("Valeur 1?\n"))
    valeur2 = int(input("Valeur 2?\n"))
    print(multiplication(valeur1,valeur2), division(valeur1,valeur2), addition(valeur1,valeur2), soustraction(valeur1,valeur2))

affichage()
