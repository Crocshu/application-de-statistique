import pandas as pd
import os
import zipfile

#Script test erreur : [x if len(x)==len(l_l[0]) and sum([1 for z in x if z==" "]) == 0 and for x in l_l]

def crea_df(fich,echan:int,separ) -> dict:
    lire = fich.read()
    if type(lire) == type(b'hduiaoh') : lire=lire.decode("latin1") # Le .decode permet de passer le type de crea_df de bytes à str car la librarie Zipfile travaille sur les données binaires
    lire=lire.replace("\r","")
    l_l=[w.split(separ) for w in lire.split("\n")] #Transformation de la lecture du fichier csv (str) en liste de liste en prenant une partie du fichier suivant ce qui est demandé
    if echan>len(l_l) : echan=len(l_l)
    l_l=l_l[:echan]
    l_l=[[y.replace('"','') for y in x] for x in l_l] #Permet de supprimer les côtes dédoublées
    l_l=[x for x in l_l if (len(x)==len(l_l[0]) and sum([1 for z in x if z==' ']) == 0)] #Création d'une nouvelle liste sans erreurs len(x)==len(l_l[0]) and 
    t_e=(1-round((len(l_l)/echan),3))*100 #Calcul du taux d'erreur
    print(t_e,echan,len(l_l))
    ini_dico={i:[] for i in l_l[0]} #Initialisation du dictionnaire     for x in l_l: print(l_l) for y in x: y=y.replace("\r","")
    {ini_dico[list(ini_dico.keys())[j.index(k)]].append(k) for j in l_l[1:] for k in j} #Remplissage du dictionnaire en faisant correspondre chaque élément à sa colonne grâce à la liste de liste
    return ini_dico #[list(ini_dico.keys())[2]]

def ouvrir_fichier(nzip,nfile,echantillon:int,separator:str) -> dict:
    loc=os.getcwd()
    if nzip != None :
        zip=os.path.join(loc,nzip) # Joindre les chemins pour faire un script multiOS
        with zipfile.ZipFile(zip) as myzip:
            with myzip.open(nfile) as file:
                return crea_df(fich=file,echan=echantillon,separ=separator)
    else:
        with open(nfile,"r",encoding="latin1") as file:
            return crea_df(fich=file,echan=echantillon,separ=separator)
#print(ouvrir_fichier(nzip=None,nfile="medocs_produits.csv",echantillon=10000000000,separator=";"))
ouvrir_fichier(nzip="medocs_mouvements.zip",nfile="mvtpdt.csv",echantillon=1000,separator=";")


def crea_dfv2(fich,echan:int,separ) -> pd.DataFrame:
    lire = pd.read_csv(fich,sep=separ,encoding='latin1',chunksize=10000,nrows=echan) #chunksize permet de diviser le fichier en plusieurs morceaux et nrows permet de prendre un nombre de lignes définies
    fichier = pd.concat(lire) #Concat permet de rassembler les différents chunks du fichiers, chunks fait pour ne pas surchargé la mémoire lors de l'ouverture du fichier.
    l, L = fichier.shape
    for i in fichier.head(0):
        fichierf = fichier[fichier[i] != " "]
    t_e=round((l/echan),3)*100 #Calcul du taux d'erreur
    print((" Il y a "+str(t_e)+" % d'erreur ").center(102,"#")+"\n")
    return fichierf

def ouvrir_fichierv2(nzip:str,nfile:str,echantillon:int,separator:str)-> pd.DataFrame:
    loc=os.getcwd()
    if nzip != None :
        zip=os.path.join(loc,nzip)  
        with zipfile.ZipFile(zip) as myzip:
            with myzip.open(nfile) as file:
                return crea_dfv2(fich=file,echan=echantillon,separ=separator)
    else:
        return crea_dfv2(fich=nfile,echan=echantillon,separ=separator)
#print(ouvrir_fichierv2(nzip=None,nfile="medocs_produits.csv",echantillon=10000,separator=";"))
#print(ouvrir_fichierv2(nzip="medocs_mouvements.zip",nfile="mvtpdt.csv",echantillon=1000000000,separator=";"))