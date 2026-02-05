print("Bienvenue dans la calculatrice :")

continuer = "o"

while continuer == "o":

    a = float(input("Entrez un nombre :"))

    print("1-Addition")
    print("2-Soustraction")
    print("3-Multiplication")
    print("4-Division")
    operation = int(input("Entrez l'opération désirée :"))
    

    b = float(input("Entrez le second nombre :"))

    if operation == 1:
        print("Le résultat : ",a+b)

    elif operation == 2:
        print("Le résultat : ",a-b)

    elif operation == 3:
        print("Le résultat : ",a*b)

    elif operation == 4:

        while b == 0:
            print("L'opération n'est pas possible.")
            b = float(input("Entrez le second nombre :"))
        
        print("Le résultat : ",a/b)
    
    else:
        print("Ce n'est pas une opération valide.")
    
    print("Voilà !")
    continuer = input("Veux-tu continuer ? (o/n) :")
    if continuer == "o":
        print("On continue !")
    else:
        print("Au revoir !")
        break
