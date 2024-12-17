from modifs_crea_df import ouvrir_fichier
import matplotlib.pyplot as plt
def graph1(df:dict,axe_x:str,axe_y:str,title:str)->plt:
    print(df)
    ax,ay=df[axe_x],df[axe_y] #Ancienne version : df[f'"{axe_x}"'],df[f'"{axe_y}"']
    vals_mois=[[float(z.replace(",",".")) for y,z in zip(ax,ay) if y[3:5]=="{:02}".format(x)] for x in range(1,13)]# Le replace est nécessaire, sinon la conversion en float est impossible car le séparateur d'un nombre réel pour python est le point et non la virgule
    moy_mois=[round(sum(x)/len(x),2) if len(x)!=0 else 0 for x in vals_mois ]
    mois=["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre"]
    #print(ax,ay,"\r\n",vals_mois)
    plt.bar(mois, moy_mois,color='orange')# Faire graphique en barre avec mois en valeur abscisse et moy_mois en valeur ordonnée avec une couleur orange
    plt.xticks(rotation=90)  # Rotation de 90 degrés pour rendre les valeurs en abscisses verticales
    plt.title(title)# Ajout du titre
    plt.show()# Afficher le graphique
    return None
#Valeurs test :
#x={'PRCLEUNIK': ['5926', '3716', '29207', '2034', '11675', '2386', '1855', '1856', '14522'], 'DATEMVT': ['03/06/2020', '03/06/2020', '03/06/2020', '03/06/2020', '06/03/2020', '06/03/2020', '06/03/2020', '06/03/2020', '06/03/2020'], 'HEUREMVT': ['0823', '0823', '0833', '0833', '1224', '1224', '1224', '1224', '1224'], 'SENSMVT': ['2', '2', '2', '2', '2', '2', '2', '2', '2'], 'TYPEMVT': ['7', '7', '7', '7', '7', '7', '7', '7', '7'], 'SERVICE': ['1602', '1602', '1901', '1901', '5121', '5121', '5121', '5121', '5121'], 'MAGASIN': ['0433', '0433', '0433', '0433', '0433', '0433', '0433', '0433', '0433'], 'QUANTITE': ['20', '10', '12', '20', '56', '24', '10', '20', '20'], 'VALHT': ['0,7', '5,197', '10,7988', '43,002', '1,0024', '0,288', '0,37', '0,598', '0,4'], 'B_URGENT': ['1', '1', '1', '1', '0', '0', '0', '0', '0']}
x=ouvrir_fichier(nzip="medocs_mouvements.zip",nfile="mvtpdt.csv",echantillon=1000000000,separator=";")
graph1(x,"DATEMVT","VALHT",'Prix moyen des mouvements par mois')
