LARGEUR_ECRAN = 640
HAUTEUR_ECRAN = 480

TAILLE_BLOC = 20
assert LARGEUR_ECRAN % TAILLE_BLOC == 0, "La largeur de l'écran doit être un multiple de la taille du bloc."
assert HAUTEUR_ECRAN % TAILLE_BLOC == 0, "La hauteur de l'écran doit être un multiple de la taille du bloc."

COULEUR_FOND = (0, 0, 0)
COULEUR_SERPENT = (0, 255, 0)
COULEUR_ALIMENT = (255, 0, 0)
COULEUR_TEXTE = (255, 255, 255)

FPS = 10