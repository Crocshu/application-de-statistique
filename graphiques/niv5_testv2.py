import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import FuncFormatter
from main import ouvrir_fichier as of
#Numéro 4 du niveau 5 (parcours)
x=of(ezip="medocs_mouvements.zip",nfile="mvtpdt.csv",echantillon=10000000,separator=";",pandas=True)
df=x
axe_x="TYPEMVT"
axe_y="DATEMVT"
cherche="NBMVT"
cherche1='JourSemaine'
cherche2="NOMMVT"
title='Proportion de mouvements par type de mouvement et par jour de la semaine'
data=df[[axe_x, axe_y]]
typemvt=sorted(list(data[axe_x].value_counts().index.values))
data[axe_y] = pd.to_datetime(data[axe_y],dayfirst=True)
#Ajout d'une colonne avec le jour de la semaine correspondant à la datemvt
data[cherche1]=data[axe_y].dt.day_name(locale='fr_FR')
cherche1_1=f"{cherche1}v2"
data[cherche1_1]=data[axe_y].dt.weekday
dic_typemvt={1:"Livraison",3:"Facturation",4:"Retour",5:"Avoir",7:"Dispensation",
8:"Régulation livraison",10:"Emprunt",20:"Prêt",21:"Perte",22:"Destruction",23:"Rappel",
24:"Périmé",30:"Transfert"}
data[cherche2]=[dic_typemvt[x] for x in data[axe_x]]#,[dic_typemvt[x] for x in typemvt],typemvt
days=['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
color=["red","orange","khaki","palegreen","greenyellow","green"]#,"purple","yellow","brown"]
liste_liste=[[len(data[(data[axe_x]==m)&(data[cherche1]==d)]) for m in typemvt]for d in days]
somme=[[s2*100/sum(s) for s2 in s] for s in liste_liste]
check=[sum(x) for x in somme]
print(somme,"\n\r",check)
donnees=[0]*7
# i= index mouvement
for c,i in zip(color,range(len(typemvt))):
    print(i)
    # tmvt = liste des mouvements par jour
    tmvt=[x[i] for x in somme]
    plt.barh(days,tmvt,label=dic_typemvt[typemvt[i]],left=donnees,color=c,height=0.4)
    # Ajouter les valeurs en pourcentage sur les barres
    for i,(g,p) in enumerate(zip(tmvt,donnees)):
        if g>=4:plt.text(p+g/2-2,i-0.1,f'{int(round(g,0))}%',color="white")
    #print(days,tmvt,dic_typemvt[typemvt[i]],c)
    # avancement des barres pour dessiner le nouvel incrément
    donnees=[h+j for h,j in zip(donnees,tmvt)]
check1=[sum([x[i] for x in somme]) for i in range(len(somme[0]))]
# Fonction de formatage pour afficher des pourcentages
def format_percent(x, pos):
    return f'{int(x)}%'
# Applique le formatage à l'axe des abscisses
plt.gca().xaxis.set_major_formatter(FuncFormatter(format_percent))
plt.legend(loc='lower center')
plt.title(title)
plt.show()
"""
#Création dic par typemvt, clé = jour, valeur = nbmvt 
val={k:[] if k in j.index.values else 0 for k in days}
x,y=list(val.keys()),list(val.values())
donnees=y
#plt.barh(x,y,label=typemvt[0],color=color[0])
for i,c in zip(typemvt[],color[]):
    #Récupération d'une partie de la dataframe
    j=data2.xs(i, level=cherche2)
    somme=sum(j[cherche])
    val={k if k in j.index.values else 0 for k in days}
    x,y=list(val.keys()),list(val.values())
    #plt.barh(x,y,label=i,left=donnees,color=c)
    #donnees=[h+j for h,j in zip(donnees,y)]
plt.legend(loc='lower center')
plt.show()
"""
"""
donnees=[0]*7
d={}
for c,i in zip(color,range(len(typemvt))):
    print(i)
    tmvt=[x[i] for x in somme]
    plt.barh(tmvt,days,label=i,color=c,**d)
    donnees=[h+j for h,j in zip(donnees,tmvt)]
    d['left']=[h+j for h,j in zip(donnees,tmvt)]
    
"""
