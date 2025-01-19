from reportlab.lib.pagesizes import letter # pip install reportlab
from reportlab.pdfgen import canvas
import os
def create_pdf(output_path:str,img_paths:str="./graphiques/img/"):
    def img_exist(file):return os.path.exists(f"{img_paths}{file}")
    img_paths=[f"{img_paths}graph{i}.png" if img_exist("graphv2{i}.png")==False else f"{img_paths}graphv2{i}.png" for i in range(1,7)]
    text_data=[f"test{i}" for i in range(1,7)]
    text_data2=["""Ce graphique représente le prix moyen des mouvements par mois au travers de chaque année du fichier. Par défaut, il
    prend toutes les années contenues dans le fichier mais une option permet de choisir quelles années vous voulez utilisez.""",
    """Ce graphique représente le nombre de mouvements effectué par les 10 services les plus actifs du fichier. Par défaut, ils sont 10 
    mais vous pouvez modifier ce nombre, rajouter un service qui n'est pas censé apparaître et la couleur suivant ce qui vous paraît le 
    plus approprié""",
    """Ce graphique représente le nombre de mouvement par mois des 4 principaux services pour toutes les années du fichier. Par défaut,
    il n'y en a que 4 mais vous pouvez modifier ce nombre.""",
    """Ce graphique représente la proportion de mouvement des principaux services du fichier. Il donne un pourcentage de mouvement effectués
    par le service en fonction des services totaux, vous pouvez modifier le nombre de service à afficher mais mettre plus de 15 est déconseillé"""
    ,"""Ce graphique représente la proportion des différents types de mouvement en fonction du jour de la semaine. Cela permet de donner un
    ordre d'idée des mouvements fait en fonction du jour de la semaine pour en ressortir une dynamique.""",
    """Ce graphique représente le prix unitaire des produits les plus présents dans les mouvements. Par défaut, il affiche les 9 premiers avec
    leurs noms, n° et leur forme. Cependant, vous pouvez aussi faire une étude précise en précisant le/les numéros du/des produits que vous voulez
    analyser."""]
    # Créer le PDF
    pdf = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter

    espacement=50 # Espacement avec le début de la page 
    hauteur=400
    ratio=640/480
    def chgmt_page(y,taille):
        result=(pdf.showPage(), height-espacement) if y < taille else (None,y)
        return result[1]
    y_position = height - espacement  # Position de départ pour écrire le texte
    for i, (text, image_path) in enumerate(zip(text_data2, img_paths)):
        # Ajouter le texte explicatif
        pdf.drawString(espacement, y_position, text)
        y_position -= espacement
        # Ajouter l'image du graphique
        pdf.drawImage(image_path, espacement, y_position - hauteur, width=hauteur*ratio, height=hauteur)
        y_position -= hauteur
        y_position=chgmt_page(y_position,hauteur+espacement)
     

    pdf.save()
create_pdf(output_path="./pdf/test.pdf")