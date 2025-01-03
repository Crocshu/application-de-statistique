import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from main import ouvrir_fichier as of

"""
# Données aléatoires
data1 = np.random.normal(0, 1, 1000)  # Distribution centrée à 0
data2 = np.random.normal(1, 1, 1000)  # Distribution centrée à 1

#print(data1,data2)
# Histogramme empilé
plt.hist(
    [data1, data2],          # Les données
    bins=1,                 # Nombre d'intervalles
    stacked=True,            # Empilement des histogrammes
    color=['blue', 'orange'], # Couleurs des barres
    alpha=0.7,               # Transparence
    edgecolor='black',        # Contour des barres
    orientation="horizontal"
)

# Ajouter des titres et des étiquettes
plt.title("Histogramme Empilé")
plt.xlabel("Valeurs")
plt.ylabel("Fréquence")

# Afficher le graphique
plt.show()
"""
#Numéro 4 du niveau 5 (parcours)
x=of(nzip="medocs_mouvements.zip",nfile="mvtpdt.csv",echantillon=1000000,separator=";",pandas=True)
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
j=data2.xs(typemvt[0], level=cherche2)
somme=sum(j[cherche])
val={k:(j.loc[k].values[0]/somme)*100 if k in j.index.values else 0 for k in days}
x,y=list(val.keys()),list(val.values())
donnees=y
plt.barh(x,y,label=typemvt[0],color=color[0])
for i,c in zip(typemvt[1:],color[1:]):
    j=data2.xs(i, level=cherche2)
    somme=sum(j[cherche])
    val={k:(j.loc[k].values[0]/somme)*100 if k in j.index.values else 0 for k in days}
    x,y=list(val.keys()),list(val.values())
    plt.barh(x,y,label=i,left=donnees,color=c)
    donnees=[h+j for h,j in zip(donnees,y)]
plt.legend(loc='lower center')
plt.show()
