def addition(a,b):
    return a+b

def soustraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    return a/b

def menu():
    print("1-Addition")
    print("2-Soustraction")
    print("3-Multiplication")
    print("4-Division")


def main():


    print("Bienvenue dans la calculatrice !")

    continuer = "o"

    while continuer.lower() == "o":
    
        a = float(input("Entrez le premier nombre :"))

        menu()

        op = int(input("Entrez l'opérateur :"))

        b = float(input("Entrez le deuxième nombre :"))

        if op == 1:
            print("Le résultat : ",addition(a,b))

        elif op == 2:
            print("Le résultat : ",soustraction(a,b))

        elif op == 3:
            print("Le résultat : ",multiplication(a,b))

        elif op == 4:
            while b == 0:
                print("L'opération est impossible.")
                b = float(input("Entrez le deuxième nombre :"))
            print("Le résultat : ",division(a,b))

        else:
            print("L'opérateur est incorrecte.")
        
        continuer = input("Voulez vous continuer à jouer ? (o/n) :")

        if continuer.lower() == "o":
            print("C'est reparti !")

        else:
            print("Au revoir !")
            break


if __name__ == "__main__":
    main()

