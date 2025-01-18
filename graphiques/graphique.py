from reportlab.lib.pagesizes import letter # pip install reportlab
from reportlab.pdfgen import canvas
import os
def create_pdf(output_path:str,img_paths:str="./graphiques/img/"):
    def img_exist(file):return os.path.exists(f"{img_paths}{file}")
    img_paths=[f"{img_paths}graph{i}.png" if img_exist("graphv2{i}.png")==False else f"{img_paths}graphv2{i}.png" for i in range(1,7)]
    text_data=[f"test{i}" for i in range(1,7)]
    text_data2=["""Ce graphique représente le prix moyen des mouvements par mois au travers de chaque année du fichier, par défaut, il
    prend toutes les années contenues dans le fichier mais une option permet de choisir quelles années vous voulez utilisez."""]
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
    for i, (text, image_path) in enumerate(zip(text_data, img_paths)):
        # Ajouter le texte explicatif
        pdf.drawString(espacement, y_position, text)
        y_position -= espacement
        # Ajouter l'image du graphique
        pdf.drawImage(image_path, espacement, y_position - hauteur, width=hauteur*ratio, height=hauteur)
        y_position -= hauteur
        y_position=chgmt_page(y_position,hauteur+espacement)
     

    pdf.save()
create_pdf(output_path="./pdf/test.pdf")