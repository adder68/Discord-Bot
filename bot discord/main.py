from random import randrange

mystere3 = randrange(0, 1000)
mystere2 = randrange(0, 100)
mystere1 = randrange(0, 20)

running = True

print("niveau 1: 0 à 20")
print("niveau 2: 0 à 100")
print("niveau 3: 0 à 1000")

saisie = int(input("Entrez le niveau de difficulté"))

if saisie == 1:
    print("Le plus simple bien sûr !")
    input("Appuyer sur entrer pour continuer...")
    while running:
        saisie1 = int(input("Entrez un nombre entre 0 et 20"))
        if saisie1 < mystere1:
            print("C'est plus")
        elif saisie1 > mystere1:
            print("C'est moins")
        else:
            print("Bravo tu as gagné !")
            running = False

if saisie == 2:
    print("ça commence à être pas mal !")
    input("Appuyer sur entrer pour continuer...")
    while running:
        saisie2 = int(input("Entrez un nombre entre 0 et 100"))
        if saisie2 < mystere2:
            print("C'est plus")
        elif saisie2 > mystere2:
            print("C'est moins")
        else:
            print("Bravo tu as gagné !")
            running = False

if saisie == 3:
    print("Bonne chance pour celui là !")
    input("Appuyer sur entrer pour continuer...")
    while running:
        saisie3 = int(input("Entrez un nombre entre 0 et 1000"))
        if saisie3 < mystere3:
            print("C'est plus")
        elif saisie3 > mystere3:
            print("C'est moins")
        else:
            print("Bravo tu as gagné !")
            running = False


input("Appuyer sur entrer pour fermer...")