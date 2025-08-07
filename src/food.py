import pygame
import random
from src.config import LARGEUR_ECRAN, HAUTEUR_ECRAN, TAILLE_BLOC, COULEUR_ALIMENT

class Food: 
    def __init__(self):
        self.rect = pygame.Rect(0, 0, TAILLE_BLOC, TAILLE_BLOC)
        self.randomize_position()

    def randomize_position(self):
        
        max_x_pos = LARGEUR_ECRAN // TAILLE_BLOC
        max_y_pos = HAUTEUR_ECRAN // TAILLE_BLOC

        grid_x = random.randrange(max_x_pos)
        grid_y = random.randrange(max_y_pos)

        self.rect.x = grid_x * TAILLE_BLOC
        self.rect.y = grid_y * TAILLE_BLOC

    def draw(self, ecran):
        pygame.draw.rect(ecran, COULEUR_ALIMENT, self.rect) 