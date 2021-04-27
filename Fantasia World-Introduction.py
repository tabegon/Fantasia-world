import random
import time
choixSortie = "Rien"
while choixSortie != "QUITTER":
    puissance = 0
    print("Bienvenue dans un jeu de rôle !")
    print("C'est parti !")
    print("Tu est dans une plaine magique.")
    time.sleep(4)
    print("???        AHAHAHAHAHAHAHAHAHAHAHA !!!! QUE FAIS TU SUR MON TERRITOIRE ?")
    time.sleep(4)
    print("KING ROY        Je suis King Roy, le roi de ce royaume !!!")
    time.sleep(3)
    print("VOUS        Connais pas. :/")
    time.sleep(2.5)
    print("KING ROY        QUOOOOOOOIIIIIIII !!!!!!!!!!")
    time.sleep(4)
    print("KING ROY        MEURRRRRRRRRRRSSSSSSS !!!!!!!")
    time.sleep(3)
    print()
    print("----------------------")
    print("COMBAT V.S. KING ROY")
    print("----------------------")
    print()
    time.sleep(2.5)
    nombre = 5
    if nombre == random.randint(1,10):
        print("VOUS        Déjà, arrête de crier, le singe.")
        time.sleep(2)
        print("VOUS        J'ai gagné, tu viens dans mon équipe 0:)")
        time.sleep(1.5)
        print("KING ROY        Okkkkkkkkkkk.......")
        time.sleep(1.5)
        print("Félicitations !")
        time.sleep(1.5)
        print("Votre puissance augmente de 5 000 points !")
        puissance = 5000
        time.sleep(1.5)
        print("Les duels sont en chance et en puissance !")
        time.sleep(1.5)
        print("Veuillez passer sur le deuxième scénario dans vos dossiers !")
        time.sleep(2.5)
        choixSortie = input("Appuie sur Entrée pour rejouer ou tape QUITTER pour arrêter.")
    else:
        print("KING ROY        AHAHAHAHAHAHAHAHAHAHA !!!!!!! J'AI GAGNE !!!!!")
        time.sleep(2.5)
        print("KING ROY        MAIS JE SUIS BON JOUEUR, JE VEUT BIEN FAIRE PARTIE DE TON EQUIPE !!")
        time.sleep(2.5)
        print("VOUS        D'accord, mais arrêtes de crier...")
        time.sleep(1.5)
        print("KING ROY        Oups... D'accord...")
        time.sleep(2)
        print("Félicitations !")
        time.sleep(1.5)
        print("Votre puissance augmente de 5 000 points !")
        puissance = 5000
        time.sleep(1.5)
        print("Les duels sont en chance et en puissance !")
        time.sleep(1.5)
        print("Veuillez passer sur le deuxième scénario dans vos dossiers !")
        time.sleep(2.5)
        choixSortie = input("Appuie sur Entrée pour rejouer ou tape QUITTER pour arrêter.")
        
    
