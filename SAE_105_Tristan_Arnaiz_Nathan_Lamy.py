import pandas as pd
import os
import zipfile
def ouvrir_fichier(nzip,nfile):
    loc=os.getcwd()
    zip=os.path.join(loc,nzip)
    fich=os.path.join(zip,nfile)
    with zipfile.ZipFile(zip) as myzip:
        with myzip.open(nfile) as file:
            ret = file.read()
            return ret
#print(ouvrir_fichier("medocs_mouvements.zip","mvtpdt.csv")[:1000])
def ouvrir_fichierv2(nzip,nfile):
    loc=os.getcwd()
    if nzip != None :
        print("io")
        zip=os.path.join(loc,nzip)
        fich=os.path.join(zip,nfile)    
        with zipfile.ZipFile(zip) as myzip:
            with myzip.open(nfile) as file:
                df = pd.read_csv(file,sep=';',header=0,index_col=0,encoding='utf-8',nrows=10)
                return df.head(5)
    else:
        print("oi")
        fich=os.path.join(loc,nfile)
        df = pd.read_csv(fich,sep=';',header=0,index_col=0,encoding='latin1',nrows=1,chunksize=10)
        return df
print(ouvrir_fichierv2(nzip=None,nfile="medocs_produits.csv"))