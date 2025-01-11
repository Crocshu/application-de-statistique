import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import FuncFormatter
from main import ouvrir_fichier as of
#Numéro 4 du niveau 5 (parcours)
x=of(ezip="../medocs_mouvements.zip",nfile="mvtpdt.csv",echantillon=10000000,separator=";",pandas=True)
df=x
axe_x="TYPEMVT"
axe_y="DATEMVT"
cherche="NBMVT"
cherche1='JourSemaine'
title='Proportion de mouvements par type de mouvement et par jour de la semaine'
days=['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
dic_typemvt={1:"Livraison",3:"Facturation",4:"Retour",5:"Avoir",7:"Dispensation",
8:"Régulation livraison",10:"Emprunt",20:"Prêt",21:"Perte",22:"Destruction",23:"Rappel",
24:"Périmé",30:"Transfert"}

typemvt=sorted(list(df[axe_x].value_counts().index.values))
typemvt2=[dic_typemvt[x] for x in typemvt]
data4=pd.DataFrame(df)
#Ajout d'une colonne avec le jour de la semaine correspondant à la datemvt
data4[cherche1] = pd.to_datetime(df[axe_y],dayfirst=True).dt.day_name(locale='fr_FR')
data4[cherche1]=pd.Categorical(data4[cherche1], categories=days, ordered=True)
data4[axe_x]=data4[axe_x].map(dic_typemvt)
data4[axe_x]=pd.Categorical(data4[axe_x], categories=typemvt2, ordered=True)
data6=pd.pivot_table(data4, values="QUANTITE", index=cherche1, columns=axe_x, aggfunc='count')
total_mouvements_par_type = data6.sum(axis=1)
taux_presence = data6.div(total_mouvements_par_type/100, axis=0)

ax=taux_presence.plot(kind='barh', stacked=True, figsize=(10, 6))
# Ajout des annotations pour chaque portion des barres
for i, (index, row) in enumerate(taux_presence.iterrows()):
    cumulative_width = 0  # Largeur cumulative pour le stacking
    for value in row:
        if value > 4:  # Ajouter une annotation si la portion dépasse 4
            # Position x (milieu de la portion) , # Position y (ligne correspondante) , # Texte à afficher , # Centrage du texte ,, # Style du texte
            ax.text(cumulative_width + value / 2, i,  f'{int(round(value, 0))}%', va='center',ha='center', color="white", fontsize=9)
        cumulative_width += value  # Mise à jour de la position cumulative pour le stacking
plt.gca().xaxis.set_major_formatter(FuncFormatter(lambda x,pos : f'{int(x)}%'))
plt.legend(loc='lower center')
plt.title(title)
plt.show()
"""
color=["red","orange","khaki","greenyellow","palegreen","green"]
# Génère une liste de nbmvt par typemvt en valeur absolue pour chaque jour
liste_liste=[[len(data[(data[axe_x]==m)&(data[cherche1]==d)]) for m in typemvt]for d in days]
#data["nmvt/typmvt"]=data.groupby(cherche1)[axe_x].transform('count')
#data3=data.groupby([cherche1,axe_x]).describe()["count"]
# Génère une liste de nbmvt par typemvt en valeur relative (%) pour chaque jour
prc_mvt_jour=[[s2*100/sum(s) for s2 in s] for s in liste_liste]
#Vérifie les valeurs pour la somme des pourcentages (doit être = à 100)
check=[sum(x) for x in prc_mvt_jour]
print(prc_mvt_jour,"\n\r",check)
donnees=[0]*7
plt.figure(figsize=(10, 6))
# i= index mouvement
for c,i in zip(color,range(len(typemvt))):
    print(i)
    # tmvt = liste des mouvements par jour pour le typemvt d'index i dans la liste typemvt
    tmvt=[x[i] for x in prc_mvt_jour]
    plt.barh(days,tmvt,label=dic_typemvt[typemvt[i]],left=donnees,color=c,height=0.4)
    # Ajouter les valeurs en pourcentage sur les barres
    for j,(g,p) in enumerate(zip(tmvt,donnees)):
        dx=0 if g>10 else g
        if g>=4:plt.text(p+g/2-2+dx,j-0.1,f'{int(round(g,0))}%',color="white")
    #print(days,tmvt,dic_typemvt[typemvt[i]],c)
    # avancement des barres pour dessiner le nouvel incrément
    donnees=[h+j for h,j in zip(donnees,tmvt)]
check1=[sum([x[i] for x in prc_mvt_jour]) for i in range(len(prc_mvt_jour[0]))]
# Fonction de formatage pour afficher des pourcentages
def format_percent(x, pos):
    return f'{int(x)}%'
# Applique le formatage à l'axe des abscisses
plt.gca().xaxis.set_major_formatter(FuncFormatter(format_percent))
"""
