#Niveau 6 Graphique motivé
import pandas as pd
import matplotlib.pyplot as plt
#ID Chloroquine : 4243 ; ID OLANZAPINE :7599,7600,7601 ; ZOLMITRIPTAN ; EFAVIRENZ ; DESLORATADINE
def graph6(df1:pd.DataFrame,df2:pd.DataFrame,nprod:int=9):
    axe_x,axe_y1,axe_y2,prod,prod2,nom,nom2="DATEMVT","QUANTITE","VALHT","PRCLEUNIK","CLE_PRODUIT","PRNOM","Nom_Produit"
    title=f'Evolution du prix unitaire des {nprod} produits les plus vendus'
    data=df1[[prod,axe_x,axe_y1,axe_y2]]
    data[axe_x] = pd.to_datetime(pd.to_datetime(data[axe_x],dayfirst=True).dt.strftime('01/%m/%Y'),dayfirst=True)
    #data[data[axe_y1].apply(lambda x: not isinstance(x, (int))] Filtre pour le type de chaque élément, ici prend les éléments qui ne sont pas int
    # Remplacement des virgules par des points pour les str et passage en str pour les int avec le .apply puis conversion en float
    data[axe_y1]=data[axe_y1].apply(lambda x: str(x).replace(',', '.') if isinstance(x, (int, str)) else x).astype(float).dropna()
    data[axe_y2] = data[axe_y2].str.replace(',', '.').astype(float)
    top_prod=list(data.groupby(prod)[axe_y1].sum().sort_values(ascending=False).index.values)[:nprod] #Les quatres produits avec la plus grande quantité en mouvement
    data_filtered=data[data[prod].isin(top_prod)]
    data_filtered_2 = pd.merge(data_filtered, df2[[prod2, nom]], left_on=prod, right_on=prod2).drop(columns=[prod2]).rename(columns={'PRNOM': 'Nom_Produit'})
    data_filtered_2[nom2]=data_filtered_2[nom2].str.split(',').str[0]
    data_quant=pd.pivot_table(data_filtered_2, values=axe_y1, index=axe_x, columns=nom2, aggfunc='sum')
    data_value=pd.pivot_table(data_filtered_2, values=axe_y2, index=axe_x, columns=nom2, aggfunc='sum')
    dataf=data_value/data_quant
    ax=dataf.plot()
    ax.set_ylabel("Valeur Unitaire (en €)")  # Nom de l'index (l'axe des X)
    plt.title(title)
    plt.show()
def graph6v2(df1:pd.DataFrame,df2:pd.DataFrame,exclusions:list=[],nprod:int=9,e_p:list=[]):
    axe_x,axe_y1,axe_y2,prod,prod2,nom,nom2="DATEMVT","QUANTITE","VALHT","PRCLEUNIK","CLE_PRODUIT","PRNOM","Médicament"
    nom3,typ="Médicament (n°) (type)","CODEUD"
    data=df1[[prod,axe_x,axe_y1,axe_y2]]
    e_p,exclusions=list(map(int,e_p)),list(map(int,exclusions))
    #Reformatage de la date au premier de chaque mois : 15/05/2022 -> 2022-05-01, 22/05/2022 -> 2022-05-01, ...
    data[axe_x] = pd.to_datetime(pd.to_datetime(data[axe_x],dayfirst=True).dt.strftime('01/%m/%Y'),dayfirst=True)
    #Jonction du DataFrame de donnée et d'informations grâce aux colonnes prod et prod 2 en supprimant la colonne prod2 et en renommant la colonne nom
    data = pd.merge(data, df2[[prod2,nom,typ]], left_on=prod, right_on=prod2).drop(columns=[prod2]).rename(columns={nom: nom2})
    #Modification du format du nom du produit en ne gardant que ce qu'il y a avant la première virgule
    data[nom2]=data[nom2].str.split(' ').str[0]
    #Création d'une colonne nom3 contenant le nom2 prod typ
    data[nom3] = data.apply(lambda row: f"{row[nom2]} ({row[prod]}) ({row[typ]})", axis=1)
    # Remplacement des virgules par des points pour les str et passage en str en plus pour les int avec le .apply puis conversion en float et suppression des lignes avec Nan
    data[axe_y1]=data[axe_y1].apply(lambda x: str(x).replace(',', '.') if isinstance(x, (int, str)) else x).astype(float).dropna()
    # Remplacement des virgules par des points puis conversion en float et suppression des lignes avec Nan
    data[axe_y2]=data[axe_y2].str.replace(',', '.').astype(float).dropna()
    #Groupby pour trier en fonction  de la somme de quantité des produits en mouvement puis récupération des nprod premiers si pas d'étude précise
    top_prod=list(data.groupby(prod)[axe_y1].sum().sort_values(ascending=False).index.values)[:nprod] if len(e_p)==0 else e_p
    #Filtrage du DataFrame pour n'avoir plus que les valeurs des produit de top_prod qui n'appartiennent pas à exclusions
    data_filtered=data[(data[prod].isin(top_prod)) & (~data[prod].isin(exclusions))]
    #Tableau croisé dynamique de la somme des quantité de produit en mouvement pour chaque produit en fonction de la date
    data_quant=pd.pivot_table(data_filtered, values=axe_y1, index=axe_x, columns=nom3, aggfunc='sum')
    #Tableau croisé dynamique de la somme des prix hors taxes des produit en mouvement pour chaque produit en fonction de la date
    data_value=pd.pivot_table(data_filtered, values=axe_y2, index=axe_x, columns=nom3, aggfunc='sum')
    #Tableau croisé dynamique du prix unitaire moyen des produit en mouvement pour chaque produit en fonction de la date
    dataf=data_value/data_quant
    ax=dataf.plot()#Création du graphique
    ax.set_ylabel("Valeur Unitaire (en €)")  # Nom de l'index (l'axe des X)
    # Nom du graphique 'dynamique'
    title=f'Prix unitaire des {len(dataf.columns)} produits les plus actifs' if len(e_p)==0 else 'Prix unitaire pour le(s) produit(s) demandé(s)'
    plt.title(title)
    plt.legend(fontsize=6 ,loc='best')
    plt.tight_layout()
    if __name__=="__main__":plt.show()
if __name__=="__main__":
    from main import ouvrir_fichier as of
    x=of(ezip="medocs_mouvements.zip",nfile="mvtpdt.csv",echantillon=10000000,separator=";",pandas=True)
    y=of(ezip=None,nfile="medocs_produits.csv",echantillon=10000000,separator=";",pandas=True)
    #graph6(df1=x,df2=y)
    graph6v2(df1=x,df2=y,e_p=['2187'])