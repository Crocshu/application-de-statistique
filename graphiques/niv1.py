import matplotlib.pyplot as plt
import datetime as dt
def graph1(df:dict)->plt:
    axe_x,axe_y,title="DATEMVT","VALHT",'Prix moyen des mouvements par mois'
    ax,ay=df[axe_x],df[axe_y]
    mois=[[x] for x in range(1,13)]
    [mois[x-1].append(float(z.replace(",","."))) for y,z in zip(ax,ay) for x in range(1,13) if y[3:5]=="{:02}".format(x)]# Le replace est nécessaire, sinon la conversion en float est impossible car le séparateur d'un nombre réel pour python est le point et non la virgule
    moy_mois=[round(sum(x)/len(x),2) if len(x)!=0 else 0 for x in mois]
    mois=["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre"]
    plt.figure(figsize=(6.4,4.8))
    plt.bar(mois, moy_mois,color='orange')# Faire graphique en barre avec mois en valeur abscisse et moy_mois en valeur ordonnée avec une couleur orange
    plt.xticks(rotation=90)  # Rotation de 90 degrés pour rendre les valeurs en abscisses verticales
    plt.title(title)# Ajout du titre
    plt.tight_layout()
    plt.show()# Afficher le graphique

def graph1v2(df:dict,years:str=None, color:str='orange')->plt:
    axe_x,axe_y,title="DATEMVT","VALHT",'Prix moyen des mouvements par mois' 
    ax,ay=[dt.datetime.strptime(x, '%d/%m/%Y') for x in df[axe_x]],[float(x.replace(",", ".")) for x in df[axe_y]]
    years=set(map(int, years.split(','))) if years else {date.year for date in ax}
    mois={i: [] for i in range(1, 13)}
    # Le replace est nécessaire, sinon la conversion en float est impossible car le séparateur d'un nombre réel pour python est le point et non la virgule
    {mois[date.month].append(val) for date,val in zip(ax,ay) if date.year in years}
    moy_mois=[round(sum(valeurs)/len(valeurs),2) if valeurs else 0 for valeurs in mois.values()]
    mois=["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre"]
    plt.bar(mois, moy_mois,color=color)# Faire graphique en barre avec mois en valeur abscisse et moy_mois en valeur ordonnée avec une couleur orange
    plt.xticks(rotation=90)  # Rotation de 90 degrés pour rendre les valeurs en abscisses verticales
    plt.title(title)# Ajout du titre
    plt.tight_layout()
    if __name__=="__main__":plt.show()# Afficher le graphique

if __name__=="__main__":
    from main import ouvrir_fichier as of
    #Valeurs test :
    x1={'PRCLEUNIK': ['5926', '3716', '29207', '2034', '11675', '2386', '1855', '1856', '14522'], 'DATEMVT': ['03/06/2020', '03/06/2020', '03/06/2020', '03/06/2020', '06/03/2020', '06/03/2020', '06/03/2020', '06/03/2020', '06/03/2020'], 'HEUREMVT': ['0823', '0823', '0833', '0833', '1224', '1224', '1224', '1224', '1224'], 'SENSMVT': ['2', '2', '2', '2', '2', '2', '2', '2', '2'], 'TYPEMVT': ['7', '7', '7', '7', '7', '7', '7', '7', '7'], 'SERVICE': ['1602', '1602', '1901', '1901', '5121', '5121', '5121', '5121', '5121'], 'MAGASIN': ['0433', '0433', '0433', '0433', '0433', '0433', '0433', '0433', '0433'], 'QUANTITE': ['20', '10', '12', '20', '56', '24', '10', '20', '20'], 'VALHT': ['0,7', '5,197', '10,7988', '43,002', '1,0024', '0,288', '0,37', '0,598', '0,4'], 'B_URGENT': ['1', '1', '1', '1', '0', '0', '0', '0', '0']}
    x=of(ezip="medocs_mouvements.zip",nfile="mvtpdt.csv",echantillon=1000000000,separator=";",pandas=False)
    graph1(x)
    graph1v2(x)
