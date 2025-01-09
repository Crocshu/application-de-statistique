import pandas as pd
import os
import zipfile

def test(l1:list,l2:list): #Fonction utilisée pour troubleshoot l'ouverture de fichier sans Pandas en comparant deux listes de liste
    for i in l1 : 
        if i not in l2 : print(i)

def crea_df(fich,echan:int,separ:str,tbsht:bool) -> dict:
    lire = fich.read()
    if type(lire) == type(b'hduiaoh') : lire=lire.decode("latin1") # Le .decode permet de passer le type de crea_df de bytes à str car la librarie Zipfile travaille sur les données binaires
    lire=lire.replace("\r","")
    l_l1=[w.split(separ) for w in lire.split("\n")] #Transformation de la lecture du fichier csv (str) en liste de liste en prenant une partie du fichier suivant ce qui est demandé
    if echan>len(l_l1) : echan=len(l_l1)
    l_l1=l_l1[:echan+1]
    if l_l1[echan-1]==[""]:
        l_l1.pop(echan-1) # Enlève la dernière ligne si elle est vide à cause d'un saut de ligne pour ne pas la compter comme erreur.
        echan=len(l_l1)
    l_l1=[[y.replace('"','') for y in x] for x in l_l1] #Permet de supprimer les côtes dédoublées
    l_l=[x for x in l_l1 if (len(x)==len(l_l1[0]) and sum([1 for z in x if z==' ']) == 0)] #Création d'une nouvelle liste sans erreurs
    if tbsht : test(l_l1,l_l) # Appel de la fonction test si jamais tbsht == True
    t_e=(round(1-(len(l_l)/echan),3))*100 #Calcul du taux d'erreur
    print((f" Il y a {t_e} % d'erreur et il y a {echan-len(l_l)} mauvaise(s) ligne(s) ").center(102,"#")+"\n")
    ini_dico={i:[] for i in l_l[0]} #Initialisation du dictionnaire 
    {ini_dico[list(ini_dico.keys())[j.index(k)]].append(k) for j in l_l[1:] for k in j} #Remplissage du dictionnaire en faisant correspondre chaque élément à sa colonne grâce à la liste de liste
    return ini_dico

def crea_dfv2(fich,echan:int,separ,tbsht:bool) -> pd.DataFrame:
    lire = pd.read_csv(fich,sep=separ,encoding='latin1',chunksize=10000,nrows=echan) #chunksize permet de diviser le fichier en plusieurs morceaux et nrows permet de prendre un nombre de lignes définies
    fichier = pd.concat(lire) #Concat permet de rassembler les différents chunks du fichiers, chunks fait pour ne pas surchargé la mémoire lors de l'ouverture du fichier.
    l, L = fichier.shape
    fichierf = fichier.copy()
    for i in fichierf.columns:
        fichierf = fichierf[fichierf[i] != " "]
    d, D = fichierf.shape
    t_e=(round((l/d-1), 3))*100 #Calcul du taux d'erreur
    print((" Il y a "+str(t_e)+" % d'erreur et il y a "+str((l-d))+" mauvaise(s) ligne(s) ").center(102,"#")+"\n")
    return fichierf

def ouvrir_fichier(nzip,nfile,echantillon:int,separator:str,pandas:bool = False,troubleshoot:bool = False) -> dict:
    func=crea_df
    if pandas : func=crea_dfv2 
    loc=os.getcwd()
    if nzip != None :
        zip=os.path.join(loc,nzip) # Joindre les chemins pour faire un script multiOS
        with zipfile.ZipFile(zip) as myzip:
            with myzip.open(nfile) as file:
                return func(fich=file,echan=echantillon,separ=separator,tbsht=troubleshoot)
    else:
        with open(nfile,"r",encoding="latin1") as file:
            return func(fich=file,echan=echantillon,separ=separator,tbsht=troubleshoot)

#Changement de séparateur pour l'ouverture du fichier medocs_produits.csv après étude de la structure du fichier, pour éviter l'erreur du produit 35469
#y=ouvrir_fichier(nzip=None,nfile="medocs_produits.csv",echantillon=1000000000,separator=';"',pandas=False,troubleshoot=True)
#y=ouvrir_fichier(nzip="medocs_mouvements.zip",nfile="mvtpdt.csv",echantillon=1000000000,separator=";",pandas=False)
#x=ouvrir_fichier(nzip=None,nfile="medocs_produits.csv",echantillon=10000000000,separator=";",pandas=True)
# print(ouvrir_fichier(nzip="medocs_mouvements.zip",nfile="mvtpdt.csv",echantillon=1000000000,separator=";",pandas=True))
#Batterie de test utilisée pour troubleshoot
"""
print(len(y["CLE_PRODUIT"]))#,len(x),list(x["CLE_PRODUIT"])[0])#,list(x["CLE_PRODUIT"]),y["CLE_PRODUIT"])#,x[x.CLE_PRODUIT == 35469])
for i in list(x["CLE_PRODUIT"]):
    if str(i) not in y["CLE_PRODUIT"]:print(i,"io")
for i in y["CLE_PRODUIT"]:
    if int(i) not in list(x["CLE_PRODUIT"]):print(i,"oi")
"""
