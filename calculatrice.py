print("Bienvenue dans la calculatrice :")

a = float(input("Entrez un nombre :"))

operation = int(input("Entrez l'opération désirée (Tapez 1 pour addition, 2 pour soustraction, 3 pour multiplication, 4 pour la division) :"))

b = float(input("Entrez le second nombre :"))

if operation == 1:
    print("Le résultat : ",a+b)

elif operation == 2:
    print("Le résultat : ",a-b)

elif operation == 3:
    print("Le résultat : ",a*b)

elif operation == 4:

    if b == 0:
    
        while b == 0:
            print("L'opération n'est pas possible.")
            b = float(input("Entrez le second nombre :"))
        
        print("Le résultat : ",a/b)
    else:
        print("Le résultat : ",a/b)

else:
    print("Ce n'est pas une opération valide.")