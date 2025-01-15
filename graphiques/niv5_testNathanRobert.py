import matplotlib.pyplot as plt
import pandas as pd
from main import ouvrir_fichier as of
from matplotlib.ticker import FuncFormatter
#Numéro 4 du niveau 5 (parcours)
x=of(ezip="../medocs_mouvements.zip",nfile="mvtpdt.csv",echantillon=10000000,separator=";",pandas=True)
df=x
axe_x="TYPEMVT"
axe_y="MAGASIN"
cherche="NBMVT"
cherche1='JourSemaine'
title='Proportion de mouvements par type de mouvement et par jour de la semaine'
dic_typemvt={1:"Livraison",3:"Facturation",4:"Retour",5:"Avoir",7:"Dispensation",
8:"Régulation livraison",10:"Emprunt",20:"Prêt",21:"Perte",22:"Destruction",23:"Rappel",
24:"Périmé",30:"Transfert"}

typemvt=sorted(list(df[axe_x].value_counts().index.values))
typemvt2=[dic_typemvt[x] for x in typemvt]
#Partie test
#Prise d'un échantillon de la dataframe
data3=df[[axe_y,axe_x,"QUANTITE"]]
#Transformation colonne avec le type de mvt pour passer des n° de mvt aux noms grâce au dic_typemvt
data3[axe_x]=data3[axe_x].map(dic_typemvt)
data4=pd.pivot_table(data3,index=axe_y,columns=axe_x,values="QUANTITE",aggfunc='count')
# Change le formatage de l'axe des abscisses pour le faire apparaître sous forme de pourcentage
#Fixe la position de la légende
plt.legend(loc='best')
plt.title(title)
plt.show()

