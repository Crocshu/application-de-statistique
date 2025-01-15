import matplotlib.pyplot as plt
import pandas as pd
from main import ouvrir_fichier as of
from matplotlib.ticker import FuncFormatter
#Numéro 4 du niveau 5 (parcours)
x=of(ezip="../medocs_mouvements.zip",nfile="mvtpdt.csv",echantillon=10000000,separator=";",pandas=True)
df=x
axe_x="TYPEMVT"
axe_y="DATEMVT"
cherche="NBMVT"
cherche1='JourSemaine'
title='Proportion de mouvements par type de mouvement et par jour de la semaine'
days={
    'Monday': 'Lundi',
    'Tuesday': 'Mardi',
    'Wednesday': 'Mercredi',
    'Thursday': 'Jeudi',
    'Friday': 'Vendredi',
    'Saturday': 'Samedi',
    'Sunday': 'Dimanche'
    }
dic_typemvt={1:"Livraison",3:"Facturation",4:"Retour",5:"Avoir",7:"Dispensation",
8:"Régulation livraison",10:"Emprunt",20:"Prêt",21:"Perte",22:"Destruction",23:"Rappel",
24:"Périmé",30:"Transfert"}

typemvt=sorted(list(df[axe_x].value_counts().index.values))
typemvt2=[dic_typemvt[x] for x in typemvt]
#Partie test
#Prise d'un échantillon de la dataframe
data3=df[[axe_y,axe_x,"QUANTITE"]].sample(n=20)
#Ajout d'une colonne avec le jour de la semaine correspondant à la datemvt d'abord en anglais puis transformation en français grâce au dictionnaire days
data3[cherche1]=pd.to_datetime(data3[axe_y],dayfirst=True).dt.day_name().map(days)
#Transformation colonne avec le type de mvt pour passer des n° de mvt aux noms grâce au dic_typemvt
data3[axe_x]=data3[axe_x].map(dic_typemvt)
#Partie graph
data4=pd.DataFrame(data3)
#Transformation colonne avec le jour de la semaine en catégorie pour pouvoir donner un ordre (celui de la semaine)
data4[cherche1]=pd.Categorical(data4[cherche1], categories=list(days.values()), ordered=True)
#Transformation colonne avec le type de mvt en catégorie pour pouvoir donner un ordre (celui du dictionnaire, ordre croissant du n° de mvt)
data4[axe_x]=pd.Categorical(data4[axe_x], categories=typemvt2, ordered=True)
#Création tableau croisé dynamique avec en index les jours, en colonne les type de mvt et en valeur le nombre de mvt d'un certain type par jour
data6=pd.pivot_table(data4, values="QUANTITE", index=cherche1, columns=axe_x, aggfunc='count')
#Fait le total de mvt peu importe le type par jour, axis=1 pour itérer par ligne
total_mouvements_par_type = data6.sum(axis=1)
#Applique une division entre les valeurs de data6 et celles de total_mouvements_par_type divisé par 100 (pour les %) à chaque colonne, axis=0 pour itérer par colonne
prc_presence = data6.div(total_mouvements_par_type/100, axis=0)
#Définission du graphique avec un .plot
ax=prc_presence.plot(kind='barh', stacked=True, figsize=(10, 6))
"""
Affiche la Dataframe sans modification trié alphabétiquement en fonction
des jours avec en dessous le tableau croisé dynamique des calculs de pourcentage
"""
print(f"{data3[[axe_y,axe_x,cherche1]].sort_values(by=[cherche1,axe_x])}\n\r{prc_presence}")
# Ajout des annotations pour chaque portion des barres
for i, (index, row) in enumerate(prc_presence.iterrows()):
    cumulative_width = 0  # Largeur cumulative pour le stacking
    for value in row: # Va itérer sur chaque ligne du tableau tableau prc_presence
        if value > 4:  # Ajouter une annotation si la portion dépasse 4
            # Position x (milieu de la portion) , Position y (ligne correspondante) , Texte à afficher , Centrage du texte ,, Style du texte
            ax.text(cumulative_width + value / 2, i,  f'{int(round(value, 0))}%', va='center',ha='center', color="white", fontsize=9)
        cumulative_width += value  # Mise à jour de la position cumulative pour le stacking
# Change le formatage de l'axe des abscisses pour le faire apparaître sous forme de pourcentage
plt.gca().xaxis.set_major_formatter(FuncFormatter(lambda x,pos : f'{int(x)}%'))
#Fixe la position de la légende
plt.legend(loc='best')
plt.title(title)
plt.show()

