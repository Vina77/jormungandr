import pygame
from src.config import LARGEUR_ECRAN, HAUTEUR_ECRAN, COULEUR_FOND, COULEUR_TEXTE, FPS
from src.snake import Snake
from src.food import Food

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))
        pygame.display.set_caption('Jeu de serpent')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.running = True
        self.game_over = False

        self.snake = Snake()
        self.food = Food()
        self.score = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction('UP')
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction('DOWN')
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction('LEFT')
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction('RIGHT')
    
    def update(self):
        if not self.game_over:
            self.snake.move()

            if self.snake.corps[0].colliderect(self.food.rect):
                self.snake.grow()
                self.food.randomize_position()
                self.score += 10

            if self.snake.check_collision():
                self.game_over = True
    
    def draw_score(self):
        score_text = self.font.render(f'Score: {self.score}', True, COULEUR_TEXTE)
        self.screen.blit(score_text, (10, 10))

    def draw_game_over(self):
        over_text = self.font.render('GAME OVER', True, COULEUR_TEXTE)
        text_rect = over_text.get_rect(center=(LARGEUR_ECRAN / 2, HAUTEUR_ECRAN / 2))
        self.screen.blit(over_text, text_rect)

    def draw(self):
        self.screen.fill(COULEUR_FOND)
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        self.draw_score()

        if self.game_over:
            self.draw_game_over()
        
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()