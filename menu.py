import pygame

class Menu:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.running = True
        self.choice = None

    def run(self):
        while self.running:
            self.screen.fill((0, 0, 0))
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.choice = "quit"
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.choice = "play"
                        self.running = False
                    if event.key == pygame.K_2:
                        self.choice = "quit"
                        self.running = False

            pygame.display.flip()

    def draw(self):
        title = self.font.render("FALLO DE CONFIRMACIÓN", True, (200, 200, 200))
        self.screen.blit(title, title.get_rect(center=(400, 200)))

        opt1 = self.font.render("1) Iniciar", True, (180, 180, 180))
        opt2 = self.font.render("2) Salir", True, (180, 180, 180))

        self.screen.blit(opt1, (330, 300))
        self.screen.blit(opt2, (330, 340))
