#Niveau 6 Graphique motivé
from main import ouvrir_fichier as of
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
#ID Chloroquine : 4243 ; ID OLANZAPINE :7599,7600,7601 ; ZOLMITRIPTAN ; EFAVIRENZ ; DESLORATADINE
def graph6(df1:pd.DataFrame,df2:pd.DataFrame,axe_x:str,axe_y:str,prod:str,title:str):
    data=df1[[axe_x, axe_y]]
    donnee_prod=df2[df2["LIBELLE_DCI"].str.contains(prod.upper())]
    liste_cle=list(donnee_prod["CLE_PRODUIT"].values)
    print(liste_cle)
    data_chloro=data[data["PRCLEUNIK"].isin(liste_cle)]
    data_chloro[axe_y] = pd.to_datetime(pd.to_datetime(data[axe_y],dayfirst=True).dt.strftime('01/%m/%Y'),dayfirst=True)
    data_chloro2=data_chloro.groupby(axe_y)[axe_x].sum()
    print(data_chloro)
    return data_chloro2
x=of(ezip="medocs_mouvements.zip",nfile="mvtpdt.csv",echantillon=10000000,separator=";",pandas=True)
y=of(ezip=None,nfile="medocs_produits.csv",echantillon=10000000,separator=";",pandas=True)
g6=graph6(df1=x,df2=y,axe_x="PRCLEUNIK",axe_y="DATEMVT",prod="OLANZAPINE",title='Proportion de mouvements par type de mouvement et par jour de la semaine')
print(g6)