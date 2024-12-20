from main import ouvrir_fichier
import matplotlib.pyplot as plt
import pandas as pd
#Numéro 2 du niveau 3
def graph3(df:pd.DataFrame,axe_x:str,axe_y:str,cherche:str,title:str)->plt:
    data=df[[axe_x, axe_y]]
    # Dataframe avec les services en index et leur nombre de mouvement en colonne trié en fonction du nombre de mouvement décroissant.
    MVT_par_SERV = data.pivot_table(index=[axe_y],values=[axe_y], aggfunc='count').rename(columns={"DATEMVT": "NBMVT"}).sort_values(by='NBMVT',ascending=False)
    x=MVT_par_SERV.head(4).index.values # Récupère les 4 premiers services avec le plus de mouvement.
    print(x)
    return None
x=ouvrir_fichier(nzip="medocs_mouvements.zip",nfile="mvtpdt.csv",echantillon=100000000,separator=";",pandas=True)
print(graph3(df=x,axe_x="DATEMVT",axe_y="SERVICE",cherche='NBVMT',title="None"))