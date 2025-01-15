from main import ouvrir_fichier as of
import matplotlib.pyplot as plt

def graph4(fichier: dict, index: str, asupp:str ,nbr: int = 10):    
    liser = {}
    for i in fichier[index]:
        if i != asupp:
            if i in liser: liser[i] += 1 # Vérifie si la clé existe déjà dans le dictionnaire
            else: liser[i] = 1 # Si la clé n'existe pas, on l'initialise à 1
        else :
            continue

    service_trie = sorted(liser.items(), key=lambda x: x[1], reverse=True)[:nbr]
    label = ()
    size = []
    for i in service_trie:
        l, s = i
        label = label + (l,)
        size.append(s)

    fig, ax = plt.subplots()
    ax.pie(x=size, labels=label, autopct='%1.2f%%') # Création d'un graphique Camembert  
    ax.set_title("Proportion de mouvements par service")
    plt.ylabel(index) # Ajout d'une étiquette sur l'axe Y
    plt.show() 

if __name__=="__main__":
    fichier = of(ezip="medocs_mouvements.zip", nfile="mvtpdt.csv", echantillon=1000000000, separator=";")
    graph4(fichier=fichier, index="SERVICE", asupp="-1")
else:
    from graphiques.main import ouvrir_fichier as of

