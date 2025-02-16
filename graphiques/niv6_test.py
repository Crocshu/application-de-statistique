#Niveau 6 Graphique motivé
from main import ouvrir_fichier as of
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
#ID Chloroquine : 4243 ; ID OLANZAPINE :7599,7600,7601 ; ZOLMITRIPTAN ; EFAVIRENZ ; DESLORATADINE
x=of(ezip="../medocs_mouvements.zip",nfile="mvtpdt.csv",echantillon=10000000,separator=";",pandas=True)
y=of(ezip=None,nfile="../medocs_produits.csv",echantillon=10000000,separator=";",pandas=True)
df1=x
df2=y
axe_x="DATEMVT"
axe_y1="QUANTITE"
axe_y2="VALHT"
prod="PRCLEUNIK"
prod2="CLE_PRODUIT"
typ="CODEUD"
nom="PRNOM"
nom2="Médicament"
nom3="Médicament (n°) (type)"
nprod=15
exclusions=[]
e_p=[2187]
data=df1[[prod,axe_x,axe_y1,axe_y2]]
data[axe_x] = pd.to_datetime(pd.to_datetime(data[axe_x],dayfirst=True).dt.strftime('01/%m/%Y'),dayfirst=True)
#data[data[axe_y1].apply(lambda x: not isinstance(x, (int))] Filtre pour le type de chaque élément, ici prend les éléments qui ne sont pas int
# Remplacement des virgules par des points pour les str et passage en str pour les int avec le .apply puis conversion en float
data = pd.merge(data, df2[[prod2, nom,typ]], left_on=prod, right_on=prod2).drop(columns=[prod2]).rename(columns={nom: nom2})
data[nom2]=data[nom2].str.split(',').str[0]
data[nom3] = data.apply(lambda row: f"{row[nom2]} ({row[prod]}) ({row[typ]})", axis=1)
data[axe_y1]=data[axe_y1].apply(lambda x: str(x).replace(',', '.') if isinstance(x, (int, str)) else x).astype(float).dropna()
data[axe_y2]=data[axe_y2].str.replace(',', '.').astype(float)
top_prod=list(data.groupby(prod)[axe_y1].sum().sort_values(ascending=False).index.values)[:nprod] if len(e_p)==0 else e_p
data_filtered=data[(data[prod].isin(top_prod)) & (~data[prod].isin(exclusions))]
data_quant=pd.pivot_table(data_filtered, values=axe_y1, index=axe_x, columns=nom3, aggfunc='sum')
data_value=pd.pivot_table(data_filtered, values=axe_y2, index=axe_x, columns=nom3, aggfunc='sum')
dataf=data_value/data_quant
ax=dataf.plot()
ax.set_ylabel("Valeur Unitaire (en €)")  # Nom de l'index (l'axe des X)
title=f'Evolution du prix unitaire des {len(dataf.columns)} produit(s) avec le plus de mouvements' if len(e_p)==0 else 'Evolution du prix unitaire pour la liste de produit demandée'
plt.title(title)
plt.show()
"""
donnee_prod=df2[df2["LIBELLE_DCI"].str.contains(prod.upper())]
liste_cle=list(donnee_prod["CLE_PRODUIT"].values)
print(liste_cle)
data_chloro=data[data["PRCLEUNIK"].isin(liste_cle)]
data_chloro2=data_chloro.groupby(axe_y)[axe_x].sum()
print(data_chloro)

g6=graph6()
print(g6)
"""
