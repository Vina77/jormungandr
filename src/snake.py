import pygame
from src.config import LARGEUR_ECRAN, HAUTEUR_ECRAN, TAILLE_BLOC, COULEUR_SERPENT

class Snake: 
    def __init__(self):
        self.x = LARGEUR_ECRAN // 2
        self.y = HAUTEUR_ECRAN // 2

        self.x_change = 0
        self.y_change = 0

        self.corps = [pygame.Rect(self.x, self.y, TAILLE_BLOC, TAILLE_BLOC)]
        self.taille_initiale = 1

    def change_direction(self, direction):
        if direction == 'UP' and self.y_change == 0:
            self.y_change = -TAILLE_BLOC
            self.x_change = 0
        elif direction == 'DOWN' and self.y_change == 0:
            self.y_change = TAILLE_BLOC
            self.x_change =0
        elif direction == 'LEFT' and self.x_change == 0:
            self.x_change = -TAILLE_BLOC
            self.y_change = 0
        elif direction == 'RIGHT' and self.x_change == 0:
            self.x_change = TAILLE_BLOC
            self.y_change = 0
    
    def move(self):
        self.x += self.x_change
        self.y += self.y_change

        nouvelle_tete = pygame.Rect(self.x, self.y, TAILLE_BLOC, TAILLE_BLOC)
        self.corps.insert(0, nouvelle_tete)

        if len(self.corps) > self.taille_initiale:
            self.corps.pop()

    def grow(self):
        self.taille_initiale += 1

    def draw(self, ecran):
        for segment in self.corps:
            pygame.draw.rect(ecran, COULEUR_SERPENT, segment)

    def check_collision(self):
        if self.x >= LARGEUR_ECRAN or self.x < 0 or self.y >= HAUTEUR_ECRAN or self.y < 0:
            return True
        
        for segment in self.corps[1:]:
            if self.corps[0].colliderect(segment):
                return True
        
        return False