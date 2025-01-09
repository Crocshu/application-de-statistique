from main import ouvrir_fichier as of
import pandas as pd
import matplotlib.pyplot as plt
#Numéro 4 du niveau 5 (parcours)
def graph5(df:pd.DataFrame,axe_x:str,axe_y:str,cherche:str,cherche1:str,cherche2:str,title:str)->plt:
    #print(df)
    data=df[[axe_x, axe_y]]
    typemvt=list(data[axe_x].value_counts().index.values)
    data[axe_y] = pd.to_datetime(data[axe_y],dayfirst=True)
    data[cherche1]=data[axe_y].dt.day_name(locale='fr_FR')
    cherche1_1=f"{cherche1}v2"
    data[cherche1_1]=data["DATEMVT"].dt.weekday
    dic_typemvt={1:"Livraison",3:"Facturation",4:"Retour",5:"Avoir",7:"Dispensation",
    8:"Régulation livraison",10:"Emprunt",20:"Prêt",21:"Perte",22:"Destruction",23:"Rappel",
    24:"Périmé",30:"Transfert"}
    data[cherche2],typemvt=[dic_typemvt[x] for x in data[axe_x]],[dic_typemvt[x] for x in typemvt]
    data2=data.groupby([cherche1,cherche1_1,cherche2]).agg({axe_x:'count'}).rename(columns={axe_x:cherche}).sort_index(level=cherche1_1).droplevel(level=cherche1_1)
    #data2=data.groupby(by=[cherche1,cherche1_1],as_index=True)[cherche2].sort_index(level=cherche1_1).droplevel(level=cherche1_1)
    days=data2.index.get_level_values(cherche1).unique().tolist()
    color=["red","blue","orange","green","purple","yellow","brown"]
    donnees=[0]*len(days)
    print(donnees)
    j1=data2.xs(typemvt[0], level=cherche2)
    val1={k:j1.loc[k].values[0] if k in j1.index.values else 0 for k in days}
    x1,y1=list(val1.keys()),list(val1.values())
    donnees.append(y1)
    plt.barh(x1,y1,label=typemvt[0],color=color[0])
    for i,c in zip(typemvt[1:],color[1:]):
        j=data2.xs(i, level=cherche2)
        val={k:j.loc[k].values[0] if k in j.index.values else 0 for k in days}
        x,y=list(val.keys()),list(val.values())
        plt.barh(x,y,label=i,left=donnees,color=c)
        donnees=[h+j for h,j in zip(donnees,y)]
    plt.show()
    return data2
x=of(nzip="medocs_mouvements.zip",nfile="mvtpdt.csv",echantillon=100000,separator=";",pandas=True)
print(graph5(df=x,axe_x="TYPEMVT",axe_y="DATEMVT",cherche="NBMVT",cherche1='JourSemaine',cherche2="NOMMVT",title='Proportion de mouvements par type de mouvement et par jour de la semaine'))