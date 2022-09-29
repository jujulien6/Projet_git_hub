def multiplication (a,b):
    print("Multiplication : ", a * b)

def division (a,b):
    if(a>b):
        print("Division : ", a / b)
    else:
        if(a/b == 0):
            print("division impossible")
        else :
            print("Division ", a / b)

def soustraction(a,b):
    print("Soustraction : ", a - b)

def addition(a,b):
    print("Addition : ", a + b)

def affichage():
    try:
        valeur1 = int(input("Valeur 1?\n"))
        valeur2 = int(input("Valeur 2?\n"))
    

        print(multiplication(valeur1,valeur2), division(valeur1,valeur2), addition(valeur1,valeur2), soustraction(valeur1,valeur2))

    except ValueError:
        print("Ce n'est pas un entier!")

affichage()

