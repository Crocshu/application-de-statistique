from main import ouvrir_fichier as of
import pandas as pd
import matplotlib.pyplot as plt
#Numéro 4 du niveau 5 (parcours)
def graph5(df:pd.DataFrame,axe_x:str,axe_y:str,cherche:str,cherche1:str,cherche2:str,title:str)->plt:
    data=df[[axe_x, axe_y]]
    data[axe_y] = pd.to_datetime(data[axe_y],dayfirst=True)
    data[cherche1]=data[axe_y].dt.day_name(locale='fr_FR')
    dic_typemvt={1:"Livraison",3:"Facturation",4:"Retour",5:"Avoir",7:"Dispensation",
    8:"Régulation livraison",10:"Emprunt",20:"Prêt",21:"Perte",22:"Destruction",23:"Rappel",
    24:"Périmé",30:"Transfert magasin"}
    data[cherche2]=[dic_typemvt[x] for x in data[axe_x]]
    data2=data.groupby([cherche1,cherche2]).agg({axe_x:'count'}).rename(columns={axe_x: cherche})#.sort_values(by=cherche1)
    print(data)
    return data2
x=of(nzip="medocs_mouvements.zip",nfile="mvtpdt.csv",echantillon=10000000,separator=";",pandas=True)
print(graph5(df=x,axe_x="TYPEMVT",axe_y="DATEMVT",cherche="NBMVT",cherche1='JourSemaine',cherche2="NOMMVT",title='Proportion de mouvements par type de mouvement et par jour de la semaine'))