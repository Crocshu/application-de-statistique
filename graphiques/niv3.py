import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import pandas as pd
#Numéro 2 du niveau 3 (parcours)
def graph3(df:pd.DataFrame)->plt:
    axe_x,axe_y,title,cherche="DATEMVT","SERVICE",'Nombre de mouvements par mois pour les 4 principaux services','NBVMT'
    data=df[[axe_x, axe_y]]
    data[axe_y]=[str(y) for y in data[axe_y]] # Mise sous même format des noms des services
    # Dataframe avec les services en index et leur nombre de mouvement en colonne trié en fonction du nombre de mouvement décroissant.
    mvt_par_serv = data.pivot_table(index=[axe_y],values=[axe_y], aggfunc='count').rename(columns={axe_x: cherche}).sort_values(by=cherche,ascending=False)
    # Récupère les 4 premiers services avec le plus de mouvement sans -1.
    top_serv=mvt_par_serv.head(5).index.values 
    top_serv=[x for x in top_serv if x !="-1"][:4]
    data2=pd.DataFrame(data) # Copie du dataframe pour ne pas l'altérer
    #Reformatage de la date au premier de chaque mois : 15/05/2022 -> 2022-05-01, 22/05/2022 -> 2022-05-01, ...
    data2[axe_x] = pd.to_datetime(pd.to_datetime(data[axe_x],dayfirst=True).dt.strftime('01/%m/%Y'),dayfirst=True)
    #Rassemble les lignes par mois puis par service en comptant le nombre de mouvement effectué dans ce mois par le service
    data2=data2.groupby([axe_x,axe_y]).agg({axe_y:'count'}).rename(columns={axe_y: cherche}).sort_values(by=[axe_x,cherche],ascending=[True,False])
    val_b,val_h=None,None
    for i in top_serv:
        j=data2.xs(i, level=axe_y) # Récupère un sous-ensemble de data 2, celui d'un des top service
        plt.plot(j.index,j[cherche],label=i) # Création du graph, en abscisse une date et en ordonnée le nombre de mouvement
        # Val_b -> Valeur basse pour la limite basse des abscisses et Val_h -> Valeur haute pour la limite haute des abscisses
        if not val_b : val_b=j.index[0]
        if not val_h : val_h=j.index[-1]
        val_b=min(val_b,j.index[0])
        val_h=max(val_h,j.index[-1])
    plt.title(title) # Donne un titre au graphique
    plt.legend(loc="upper left") # Positionne la légende en haut à gauche
    def custom_date_format(x,pos=None): #Formatage de la date sur l'axe des abscisses sachant que la valeur en abscisse donnée par matplotlib est en Epoch Unix
        datess = pd.to_datetime(x,unit='D', origin='unix')  # Convertir epoch Unix en datetime
        print(x,datess)
        # Condition : Si le mois est Juillet
        if datess.month == 7: return datess.strftime("%b")  # Afficher le mois en lettre 
        return None  # Sinon, ne rien afficher
    ax=plt.gca() # gca=GetCurrentAxis
    ax.set_xlim(val_b,val_h)
    ax.xaxis.set_major_locator(mdates.MonthLocator(1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b\n%Y"))
    ax.xaxis.set_minor_locator(mdates.MonthLocator())
    ax.xaxis.set_minor_formatter(FuncFormatter(custom_date_format))
    plt.show()
def graph3v2(df:pd.DataFrame)->plt:
    axe_x,axe_y,title,cherche="DATEMVT","SERVICE",'Nombre de mouvements par mois pour les 4 principaux services','NBVMT'
    #Transforme le type de chaque élément de la colonne axe_y(DATEMVT) en str
    df[axe_y] = df[axe_y].astype(str)
    # Récupère les 4 premiers services avec le plus de mouvement sans -1.
    top_serv=list(df[df[axe_y] != "-1"][axe_y].value_counts()[:4].index.values)
    #Récupère uniquement les lignes des top services
    data4=df[df[axe_y].isin(top_serv)]
    #Création d'une colonne cherche(NBMVT) qui a sur chaque ligne la valeur 0 pour que lors de la création de la pivot_table, il n'y ait pas d'erreur
    data4[cherche] = 0
    #Reformatage de la date au premier de chaque mois : 15/05/2022 -> 2022-05-01
    data4[axe_x] = pd.to_datetime(pd.to_datetime(data4[axe_x],dayfirst=True).dt.strftime('01/%m/%Y'),dayfirst=True)
    #Création d'une catégorie pour pouvoir trier les ervices en fonction de leur nb de mvt total
    data4[axe_y] = pd.Categorical(data4[axe_y], categories=top_serv, ordered=True)
    #Fait un tableau croisé, met en ligne les dates et en colonnes les services et renvoie comme valeur le nb de ligne où le service est mentionné sur ce mois
    donnee_graph=pd.pivot_table(data4, values=cherche, index=axe_x, columns=axe_y, aggfunc='count')
    donnee_graph.plot(figsize=(6.4,4.8))
    plt.title(title)
    plt.tight_layout()
    plt.show()

def graph3int(df:pd.DataFrame, title="Mouvement par mois des 4 principaux services")->plt:
    axe_x,axe_y,cherche="DATEMVT","SERVICE",'NBVMT'
    #Transforme le type de chaque élément de la colonne axe_y(DATEMVT) en str
    df[axe_y] = df[axe_y].astype(str)
    # Récupère les 4 premiers services avec le plus de mouvement sans -1.
    top_serv=list(df[df[axe_y] != "-1"][axe_y].value_counts()[:4].index.values)
    #Récupère uniquement les lignes des top services
    data4=df[df[axe_y].isin(top_serv)]
    #Création d'une colonne cherche(NBMVT) qui a sur chaque ligne la valeur 0 pour que lors de la création de la pivot_table, il n'y ait pas d'erreur
    data4[cherche] = 0
    #Reformatage de la date au premier de chaque mois : 15/05/2022 -> 2022-05-01
    data4[axe_x] = pd.to_datetime(pd.to_datetime(data4[axe_x],dayfirst=True).dt.strftime('01/%m/%Y'),dayfirst=True)
    #Création d'une catégorie pour pouvoir trier les ervices en fonction de leur nb de mvt total
    data4[axe_y] = pd.Categorical(data4[axe_y], categories=top_serv, ordered=True)
    #Fait un tableau croisé, met en ligne les dates et en colonnes les services et renvoie comme valeur le nb de ligne où le service est mentionné sur ce mois
    donnee_graph=pd.pivot_table(data4, values=cherche, index=axe_x, columns=axe_y, aggfunc='count')
    donnee_graph.plot(figsize=(6.4,4.8))
    plt.title(title)
    plt.tight_layout()


if __name__=="__main__":
    from main import ouvrir_fichier as of
    x=of(ezip="medocs_mouvements.zip",nfile="mvtpdt.csv",echantillon=10000000,separator=";",pandas=True)
    #graph3(df=x,axe_x="DATEMVT",axe_y="SERVICE",cherche='NBMVT',title='Nombre de mouvements par mois pour les 4 principaux services')
    graph3v2(x)
else:
    from graphiques.main import ouvrir_fichier as of