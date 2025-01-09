from screeninfo import get_monitors

ecran = get_monitors()[0]
hauteur = int(ecran.height*0.5)
largueur = int(ecran.width*0.5)
WINDOW_SIZE = f"{largueur}x{hauteur}+{ecran.width_mm}+{ecran.height_mm}"

COLORS = {
    "bg": "#ffffff",
    "primary": "#4A90E2",
    "text": "#333333"
}


