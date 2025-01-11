from main import ouvrir_fichier
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pandas as pd
#Numéro 2 du niveau 3
x=ouvrir_fichier(ezip="../medocs_mouvements.zip",nfile="mvtpdt.csv",echantillon=10000000,separator=";",pandas=True)
df=x
axe_x="DATEMVT"
axe_y="SERVICE"
cherche='NBVMT'
title='Nombre de mouvements par mois pour les 4 principaux services'
#Transforme
df[axe_y] = df[axe_y].astype(str)
# Récupère les 4 premiers services avec le plus de mouvement sans -1.
top_serv=list(df[df[axe_y] != "-1"][axe_y].value_counts()[:4].index.values)
#Récupère uniquement les lignes des top services
data4=df[df[axe_y].isin(top_serv)]
data4[cherche] = 0
#Reformatage de la date au premier de chaque mois : 15/05/2022 -> 2022-05-01
data4['DATEMVT'] = pd.to_datetime(pd.to_datetime(data4['DATEMVT'],dayfirst=True).dt.strftime('01/%m/%Y'),dayfirst=True)
#Création d'une catégorie pour pouvoir trier les ervices en fonction de leur nb de mvt total
data4[axe_y] = pd.Categorical(data4[axe_y], categories=top_serv, ordered=True)
#Fait un tableau croisé, met en ligne les dates et en colonnes les services et renvoie comme valeur le nb de ligne où le service est mentionné sur ce mois
donnee_graph=pd.pivot_table(data4, values=cherche, index=axe_x, columns=axe_y, aggfunc='count')
donnee_graph.plot()
plt.show()
"""
data2=df[df[axe_y].isin(top_serv)]
data2['DATEMVT'] = pd.to_datetime(pd.to_datetime(data['DATEMVT'],dayfirst=True).dt.strftime('01/%m/%Y'),dayfirst=True)
data2[axe_y] = pd.Categorical(data2[axe_y], categories=top_serv, ordered=True)
data3=data2.groupby(["DATEMVT",axe_y]).size()
donnee_graph=data3.unstack(level=axe_y)
"""
"""
for i in top_serv:
    j=data3.xs(i, level='SERVICE') # Récupère un sous-ensemble de data 2, celui d'un des top service
    plt.plot(j.index,j.values,label=i) # Création du graph, en abscisse une date et en ordonnée le nombre de mouvement
"""
"""
plt.title(title) # Donne un titre au graphique
plt.legend(loc="upper left") # Positionne la légende en haut à gauche
def custom_date_format(x,pos=None): #Formatage de la date sur l'axe des abscisses sachant que la valeur en abscisse donnée par matplotlib est en Epoch Unix
    datess = pd.to_datetime(x,unit='D', origin='unix')  # Convertir epoch Unix en datetime
    #print(x,datess)
    # Condition : Si le mois est Juillet
    if datess.month == 7: return datess.strftime("%b")  # Afficher le mois en lettre 
    return None  # Sinon, ne rien afficher
def custom_date_format2(x, pos=None, min_date=None, max_date=None):
"""
#Formatage personnalisé pour un axe normalisé (pandas plot).
    
#Args:
#    x (float): La valeur normalisée des ticks.
#    pos (int): Position (ignorée ici).
#    min_date (datetime): Date réelle correspondant à la borne inférieure.
#    max_date (datetime): Date réelle correspondant à la borne supérieure.
    
#Returns:
#    str: Format personnalisé pour l'axe des abscisses.
"""
    # Conversion inverse : valeur normalisée -> date réelle
    if min_date is not None and max_date is not None:
        # Calcul de la proportion
        frac = (x - min_val) / (max_val - min_val)
        # Interpolation pour obtenir la date
        date = min_date + frac * (max_date - min_date)
    else:
        return ""

    # Si le mois est juillet
    if date.month == 7:
        return date.strftime("%b")  # Affiche "Jul" pour juillet
    return None  # Sinon, ne rien afficher

ax=plt.gca() #Récupère l'axe actuel pour ne pas avoir à le définir à chaque fois lors des modifications pour le style du graph
min_val, max_val = ax.get_xlim()
min_date, max_date=min(data2['DATEMVT']),max(data2['DATEMVT'])
formatter = lambda x, pos: custom_date_format2(x, pos, min_date, max_date)
ax.set_xlim(min_date, max_date) #Permet de borner le graph, pour éviter d'avoir des abscisses qui n'ai de valeurs pour aucune courbe
ax.xaxis.set_major_locator(mdates.MonthLocator(1))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b\n%Y"))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
ax.xaxis.set_minor_formatter(FuncFormatter(formatter))
"""


