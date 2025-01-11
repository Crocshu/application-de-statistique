import pandas as pd
from main import ouvrir_fichier as of

def graph2(fichier: pd.DataFrame,col: str ,supp: str = None): # col est la colones à analyser, supp est une valeur à retirer, fichier et le fichier à analyser
    fichier[col] = fichier[col].astype(str).str.strip() 
    # astype(str) : Convertit toutes les valeurs de la colonne en chaînes pour éviter les conflits de type.
    # str.strip() : Supprime les espaces au début et à la fin des chaînes.
    if supp != None: asupp = fichier[fichier[col] != supp] # Retirer les lignes où le services est -1
    else : asupp = fichier
    # liser = {}
    # for i in asupp[col]:
    #     if i in liser: liser[i] += 1 # Vérifie si la clé existe déjà dans le dictionnaire
    #     else: liser[i] = 1 # Si la clé n'existe pas, on l'initialise à 1
    liser = asupp[col].value_counts()
    service_trie = sorted(liser.items(), key=lambda x: x[1], reverse=True)[:15] # Lambda sert de fonction anonyme qui renvoie la deuxième valeur de x d'où (x[1])
    serviceF = pd.DataFrame(service_trie)
    fig = serviceF.plot(title="Nombre de mouvements par service", kind="bar", x=0, color="orange", legend=False).get_figure()
    fig.savefig("graphique_service.png")

def graph2v2(fichier: pd.DataFrame,col: str ,cherche: str,supp: str = None): # col est la colones à analyser, supp est une valeur à retirer, fichier et le fichier à analyser
    fichier[col] = fichier[col].astype(str).str.strip() 
    # astype(str) : Convertit toutes les valeurs de la colonne en chaînes pour éviter les conflits de type.
    # str.strip() : Supprime les espaces au début et à la fin des chaînes.
    if supp != None: asupp = fichier[fichier[col] != supp] # Retirer les lignes où le services est -1
    else : asupp = fichier
    serviceF=asupp.groupby(col).agg({col:'count'}).rename(columns={col: cherche}).sort_values(by=cherche,ascending=False).head(15)
    print(serviceF,type(serviceF))
    fig = serviceF.plot(title="Nombre de mouvements par service", kind="bar", color="orange", legend=False).get_figure()
    fig.savefig("graphique_servicev2.png")

fichier = of(ezip="medocs_mouvements.zip", nfile="mvtpdt.csv", echantillon=1000000000, separator=";", pandas=True)
graph2(fichier=fichier, col="SERVICE", supp="-1")
graph2v2(fichier=fichier, col="SERVICE", supp="-1", cherche="NBMVT")
