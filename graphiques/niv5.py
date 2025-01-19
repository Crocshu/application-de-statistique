import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
#Numéro 4 du niveau 5 (parcours)
def graph5(df:pd.DataFrame,axe_x:str,axe_y:str,niveau:str,cherche1:str,title:str)->plt:
    days=['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    color=["red","orange","khaki","greenyellow","palegreen","green"] if niveau=="noob" else ["red","orange","greenyellow","khaki","palegreen","green"]
    dic_typemvt={1:"Livraison",3:"Facturation",4:"Retour",5:"Avoir",7:"Dispensation",
    8:"Régulation livraison",10:"Emprunt",20:"Prêt",21:"Perte",22:"Destruction",23:"Rappel",
    24:"Périmé",30:"Transfert"}
    data=df[[axe_x, axe_y]]
    typemvt=sorted(list(data[axe_x].value_counts().index.values))
    data[axe_y] = pd.to_datetime(data[axe_y],dayfirst=True)
    #Ajout d'une colonne avec le jour de la semaine correspondant à la datemvt
    data[cherche1]=data[axe_y].dt.day_name(locale='fr_FR')
    # Génère une liste de nbmvt par typemvt en valeur absolue pour chaque jour
    liste_liste=[[len(data[(data[axe_x]==m)&(data[cherche1]==d)]) for m in typemvt]for d in days]
    # Génère une liste de nbmvt par typemvt en valeur relative (%) pour chaque jour
    prc_mvt_jour=[[s2*100/sum(s) for s2 in s] for s in liste_liste]
    #Vérifie les valeurs pour la somme des pourcentages (doit être = à 100)
    check=[sum(x) for x in prc_mvt_jour]
    print(prc_mvt_jour,"\n\r",check)
    donnees=[0]*7
    plt.figure(figsize=(10, 6))
    # i= index mouvement
    for c,i in zip(color,range(len(typemvt))):
        print(i)
        # tmvt = liste des mouvements par jour pour le typemvt d'index i dans la liste typemvt
        tmvt=[x[i] for x in prc_mvt_jour]
        plt.barh(days,tmvt,label=dic_typemvt[typemvt[i]],left=donnees,color=c,height=0.4)
        # Ajouter les valeurs en pourcentage sur les barres
        for j,(g,p) in enumerate(zip(tmvt,donnees)):
            dx=0
            if niveau=="noob":dx=0 if g>10 else g
            if g>=4:plt.text(p+g/2-2+dx,j-0.1,f'{int(round(g,0))}%',color="white")
        #print(days,tmvt,dic_typemvt[typemvt[i]],c)
        # avancement des barres pour dessiner le nouvel incrément
        donnees=[h+j for h,j in zip(donnees,tmvt)]
    #Vérifie les valeurs pour la somme des pourcentages (doit être = à 100*nb_de_jour)
    check1=sum([sum([x[i] for x in prc_mvt_jour]) for i in range(len(prc_mvt_jour[0]))])
    # Fonction de formatage pour afficher des pourcentages
    def format_percent(x, pos):
        return f'{int(x)}%'
    # Applique le formatage à l'axe des abscisses
    plt.gca().xaxis.set_major_formatter(FuncFormatter(format_percent))
    plt.legend(loc='lower center')
    plt.title(title)
    plt.show()
def graph5v2(df:pd.DataFrame):
    axe_x,axe_y,cherche1="TYPEMVT","DATEMVT",'JourSemaine'
    title='Proportion de mouvements par jour'
    days={'Monday': 'Lundi','Tuesday': 'Mardi','Wednesday': 'Mercredi','Thursday': 'Jeudi','Friday': 'Vendredi','Saturday': 'Samedi','Sunday': 'Dimanche'}
    colors=["red","orange","greenyellow","khaki","palegreen","green"]
    dic_typemvt={1:"Livraison",3:"Facturation",4:"Retour",5:"Avoir",7:"Dispensation",8:"Régulation livraison",
    10:"Emprunt",20:"Prêt",21:"Perte",22:"Destruction",23:"Rappel", 24:"Périmé",30:"Transfert"}
    #Copie du DataFrame original
    df1=pd.DataFrame(df)
    """
    Ajout d'une colonne avec le jour de la semaine correspondant à la datemvt d'abord en anglais puis transformation en français 
    grâce au dictionnaire days avec création de catégorie pour pouvoir donner un ordre (celui de la semaine)
    """
    df1[cherche1] = pd.Categorical(pd.to_datetime(df1[axe_y],dayfirst=True).dt.day_name().map(days), categories=list(days.values()), ordered=True)
    #Transformation colonne avec le type de mvt en catégorie pour pouvoir donner un ordre (celui du dictionnaire, ordre croissant du n° de mvt)
    df1[axe_x]=pd.Categorical(df1[axe_x].map(dic_typemvt), categories=list(dic_typemvt.values()), ordered=True)
    data6=pd.pivot_table(df1, values="QUANTITE", index=cherche1, columns=axe_x, aggfunc='count', observed=True)
    #Fait le total de mvt peu importe le type par jour, axis=1 pour itérer par ligne
    total_mouvements_par_type = data6.sum(axis=1)
    #Applique une division entre les valeurs de data6 et celles de total_mouvements_par_type divisé par 100 (pour les %) à chaque colonne, axis=0 pour itérer par colonne
    prc_presence = data6.div(total_mouvements_par_type/100, axis=0)
    #Définission du graphique avec un .plot
    ax=prc_presence.plot(kind='barh', stacked=True, color=colors if len(colors)==len(prc_presence.index)-1 else None)
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
    plt.tight_layout()
    if __name__=="__main__": plt.show()
if __name__=="__main__":
    from main import ouvrir_fichier as of
    x=of(ezip="medocs_mouvements.zip",nfile="mvtpdt.csv",echantillon=10000000,separator=";",pandas=True)
    #graph5(df=x,axe_x="TYPEMVT",axe_y="DATEMVT",niveau="pasnoob",cherche1='JourSemaine',title='Proportion de mouvements par type de mouvement et par jour de la semaine')
    graph5v2(df=x)