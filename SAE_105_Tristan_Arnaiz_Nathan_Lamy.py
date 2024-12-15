import pandas as pd
import os
import zipfile

def crea_df(fich,echan:int):
    lire = fich.read()
    return lire[:echan]

def ouvrir_fichier(nzip,nfile,echantillon:int):
    loc=os.getcwd()
    if nzip != None :
        zip=os.path.join(loc,nzip)
        with zipfile.ZipFile(zip) as myzip:
            with myzip.open(nfile) as file:
                return crea_df(fich=file,echan=echantillon).decode("latin1") # Le .decode permet de passer le type de crea_df de bytes à str car la librarie Zipfile travaille sur les données binaires
    else:
        with open(nfile,"r",encoding="latin1") as file:
            return crea_df(fich=file,echan=echantillon)
#print(ouvrir_fichier(nzip=None,nfile="medocs_produits.csv",echantillon=10000))
#print()
#print(ouvrir_fichier(nzip="medocs_mouvements.zip",nfile="mvtpdt.csv",echantillon=10000))


def crea_dfv2(fich,echan:int):
    lire = pd.read_csv(fich,sep=';',encoding='latin1',chunksize=10000,nrows=echan) #chunksize permet de diviser le fichier en plusieurs morceaux et nrows permet de prendre un nombre de lignes définies
    return pd.concat(lire) #Concat permet de rassembler les différents chunks du fichiers, chunks fait pour ne pas surchargé la mémoire lors de l'ouverture du fichier.

def ouvrir_fichierv2(nzip:str,nfile:str,echantillon:int):
    loc=os.getcwd()
    if nzip != None :
        zip=os.path.join(loc,nzip)  
        with zipfile.ZipFile(zip) as myzip:
            with myzip.open(nfile) as file:
                return crea_dfv2(fich=file,echan=echantillon)
    else:
        return crea_dfv2(fich=nfile,echan=echantillon)
print(ouvrir_fichierv2(nzip=None,nfile="medocs_produits.csv",echantillon=10000))
print(ouvrir_fichierv2(nzip="medocs_mouvements.zip",nfile="mvtpdt.csv",echantillon=10000))