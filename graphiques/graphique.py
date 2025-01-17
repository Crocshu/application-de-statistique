from reportlab.lib.pagesizes import letter # pip install reportlab
from reportlab.pdfgen import canvas
import os
def create_pdf(output_path:str,img_paths:str="./graphiques/img/"):
    def img_exist(file):return os.path.exists(f"{img_paths}{file}")
    img_paths=[f"{img_paths}graph{i}.png" if img_exist("graphv2{i}.png")==False else f"{img_paths}graphv2{i}.png" for i in range(1,7)]
    text_data=[f"test{i}" for i in range(1,7)]
    # Créer le PDF
    pdf = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter

    def chgmt_page(y,taille):
        if y < taille:
            pdf.showPage()
            return height - 50
        return y
    y_position = height - 50  # Position de départ pour écrire le texte
    for i, (text, image_path) in enumerate(zip(text_data, img_paths)):
        # Ajouter le texte explicatif
        pdf.drawString(50, y_position, text)
        y_position -= 50
        # Ajouter l'image du graphique
        pdf.drawImage(image_path, 50, y_position - 400, width=500, height=400)
        y_position -= 400
        y_position=chgmt_page(y_position,450)
     

    pdf.save()
create_pdf(output_path="./pdf/test.pdf")