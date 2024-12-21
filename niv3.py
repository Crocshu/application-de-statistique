from main import ouvrir_fichier
import matplotlib.pyplot as plt
import pandas as pd
#Numéro 2 du niveau 3
def graph3(df:pd.DataFrame,axe_x:str,axe_y:str,cherche:str,title:str)->plt:
    data=df[[axe_x, axe_y]]
    # Dataframe avec les services en index et leur nombre de mouvement en colonne trié en fonction du nombre de mouvement décroissant.
    mvt_par_serv = data.pivot_table(index=[axe_y],values=[axe_y], aggfunc='count').rename(columns={"DATEMVT": "NBMVT"}).sort_values(by='NBMVT',ascending=False)
    print(mvt_par_serv)
    top_serv=mvt_par_serv.head(4).index.values # Récupère les 4 premiers services avec le plus de mouvement.
    #print(x)
    #Récupère uniquement les lignes des top services
    data_top_serv=data[data[axe_y].isin(top_serv)]
    #Reformatage de la date au premier de chaque mois : 01/05/2022
    data_top_serv['DATEMVT'] = pd.to_datetime(data_top_serv['DATEMVT'],dayfirst=True).dt.strftime('%Y/%m')#.strftime('%Y %B')
    #Calcul les lignes par mois puis par service en comptant le nombre de mouvement effectué dans ce mois par le service
    data_top_serv_agg=data_top_serv.groupby(["DATEMVT", axe_y]).agg({axe_y: 'count'})#.sort_values(by='DATEMVT',ascending=True)#.rename(columns={axe_y: "NBMVT"})
    data_top_serv_agg.unstack(axe_y)[axe_y].plot() #En rajoutant le [axe_y], on fait en sorte de prendre uniquement le nom des services et pas le nom des services et celui de la colonne des valeurs
    plt.title('Nombre de mouvements par mois pour les 4 principaux services')
    plt.legend(loc="upper left")
    plt.show()
    return data_top_serv_agg
x=ouvrir_fichier(nzip="medocs_mouvements.zip",nfile="mvtpdt.csv",echantillon=10000000,separator=";",pandas=True)
print(graph3(df=x,axe_x="DATEMVT",axe_y="SERVICE",cherche='NBVMT',title="None"))