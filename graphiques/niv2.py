import pandas as pd

def graph2(fichier: pd.DataFrame,col: str ,supp: str = None): # col est la colones à analyser, supp est une valeur à retirer, fichier et le fichier à analyser
    fichier[col] = fichier[col].astype(str).str.strip() 
    # astype(str) : Convertit toutes les valeurs de la colonne en chaînes pour éviter les conflits de type.
    # str.strip() : Supprime les espaces au début et à la fin des chaînes.
    if supp != None: asupp = fichier[fichier[col] != supp] # Retirer les lignes où le services est -1
    else : asupp = fichier
    liser = asupp[col].value_counts()
    service_trie = sorted(liser.items(), key=lambda x: x[1], reverse=True)[:15] # Lambda sert de fonction anonyme qui renvoie la deuxième valeur de x d'où (x[1])
    serviceF = pd.DataFrame(service_trie)
    fig = serviceF.plot(title="Nombre de mouvements par service", kind="bar", x=0, color="orange", legend=False).get_figure()
    fig.savefig("graphique_service.png")

def graph2v2(fichier: pd.DataFrame,supp: str = None,nbr:int=15,couleur:str="orange"):
    # supp est une valeur à retirer, fichier et le fichier à analyser,nbr est le nombre de service à étudier,couleur est la couleur du graphique
    col,cherche="SERVICE","NBMVT"# col est la colones à analyser, cherche est le nom à donner à la colonne après le groupby
    fichier[col] = fichier[col].astype(str)# astype(str) : Convertit toutes les valeurs de la colonne en chaînes pour éviter les conflits de type.a fin des chaînes.
    if supp != None: fichier = fichier[fichier[col] != supp] # Retirer les lignes où le services est -1
    serviceF=fichier.groupby(col).agg({col:'count'}).rename(columns={col: cherche}).sort_values(by=cherche,ascending=False).head(nbr)
    fig = serviceF.plot(title="Nombre de mouvements par service", kind="bar", color=couleur, legend=False).get_figure()
    fig.savefig("graphique_servicev2.png")

if __name__=="__main__":
    from main import ouvrir_fichier as of
    fichier = of(ezip="medocs_mouvements.zip", nfile="mvtpdt.csv", echantillon=1000000000, separator=";", pandas=True)
    graph2(fichier=fichier, col="SERVICE", supp="-1")
    graph2v2(fichier=fichier,supp="-1",nbr=20,couleur='plum')
else:
    from graphiques.main import ouvrir_fichier as of
