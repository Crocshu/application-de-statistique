from main import ouvrir_fichier
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pandas as pd
#Numéro 2 du niveau 3
x=ouvrir_fichier(nzip="medocs_mouvements.zip",nfile="mvtpdt.csv",echantillon=10000000,separator=";",pandas=True)
df=x
axe_x="DATEMVT"
axe_y="SERVICE"
cherche='NBVMT'
title="None"
data=df[[axe_x,axe_y]]
data[axe_y]=[str(y) for y in data[axe_y]]
# Dataframe avec les services en index et leur nombre de mouvement en colonne trié en fonction du nombre de mouvement décroissant.
mvt_par_serv = data.pivot_table(index=[axe_y],values=[axe_y], aggfunc='count').rename(columns={"DATEMVT": "NBMVT"}).sort_values(by='NBMVT',ascending=False)
# Récupère les 4 premiers services avec le plus de mouvement sans -1.
top_serv=mvt_par_serv.head(5).index.values 
top_serv=[x for x in top_serv if x !="-1"][:4]
#Récupère uniquement les lignes des top services
data2=pd.DataFrame(data)
#Reformatage de la date au premier de chaque mois : 15/05/2022 -> 2022-05-01
data2['DATEMVT'] = pd.to_datetime(pd.to_datetime(data['DATEMVT'],dayfirst=True).dt.strftime('01/%m/%Y'),dayfirst=True)
#Calcul les lignes par mois puis par service en comptant le nombre de mouvement effectué dans ce mois par le service
data2=data2.groupby(["DATEMVT",axe_y]).agg({axe_y:'count'}).rename(columns={"SERVICE": "NBMVT"}).sort_values(by=['DATEMVT','NBMVT'],ascending=[True,False])
val_b,val_h=None,None
for i in top_serv:
    j=data2.xs(i, level='SERVICE') # Récupère un sous-ensemble de data 2, celui d'un des top service
    plt.plot(j.index,j['NBMVT'],label=i) # Création du graph, en abscisse une date et en ordonnée le nombre de mouvement
    # Val_b -> Valeur basse pour la limite basse des abscisses et Val_h -> Valeur haute pour la limite haute des abscisses
    if not val_b : val_b=j.index[0]
    if not val_h : val_h=j.index[-1]
    val_b=min(val_b,j.index[0])
    val_h=max(val_h,j.index[-1])
plt.title('Nombre de mouvements par mois pour les 4 principaux services') # Donne un titre au graphique
plt.legend(loc="upper left") # Positionne la légende en haut à gauche
def custom_date_format(x,pos=None): #Formatage de la date sur l'axe des abscisses sachant que la valeur en abscisse donnée par matplotlib est en Epoch Unix
    datess = pd.to_datetime(x,unit='D', origin='unix')  # Convertir epoch Unix en datetime
    # Condition : Si le mois est Juillet
    if datess.month == 7: return datess.strftime("%b")  # Afficher le mois en lettre 
    return None  # Sinon, ne rien afficher
ax=plt.gca()
ax.set_xlim(val_b,val_h)
ax.xaxis.set_major_locator(mdates.MonthLocator(1))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b\n%Y"))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
ax.xaxis.set_minor_formatter(FuncFormatter(custom_date_format))
plt.show()


