import pygame
import random

from game_questions import QUESTIONS
from game_memory import Memory
from state import MentalState
from ui import UI
from endings import ending_text
from enemy import CognitiveNoise

WIDTH, HEIGHT = 800, 600

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Fallo de Confirmación")

        self.clock = pygame.time.Clock()
        self.ui = UI(self.screen)

        self.memory = Memory()
        self.state = MentalState()
        self.noise = CognitiveNoise()

        self.running = True
        self.index = 0
        self.current = QUESTIONS[0]
        self.questions_asked = 0

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.handle_events()

            self.ui.draw_all(
                self.state,
                self.memory.history,
                self.current,
                self.questions_asked
            )

            pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_1, pygame.K_2):
                    self.answer(event.key)

    def answer(self, key):
        answer = self.current[1][0] if key == pygame.K_1 else self.current[1][1]

        self.memory.store(self.current[0], answer)
        self.state.degrade()
        self.noise.maybe_attack(self.state)
        self.memory.corrupt()

        self.questions_asked += 1

        if random.random() < 0.15 and self.state.stability < 70:
            self.state.repetition += 1

        if (
            self.state.stability <= 0
            or self.questions_asked >= 50
            or (self.state.blame > 5 and self.state.distortion > 5)
        ):
            self.end_game()
            return

        if self.questions_asked > 5 and random.random() < 0.3:
            recalled = self.memory.recall()
            if recalled:
                self.current = (
                    recalled[0] + " (registro alterado)",
                    ["Sí", "No"]
                )
                return

        self.index = (self.index + 1) % len(QUESTIONS)
        if self.index == 0:
            self.state.degrade_extra()

        self.current = QUESTIONS[self.index]

    def end_game(self):
        self.screen.fill((0, 0, 0))

        lines = ending_text(self.state).split("\n")
        y = HEIGHT // 2 - len(lines) * 20

        for line in lines:
            rendered = self.ui.large_font.render(line, True, (240, 240, 240))
            rect = rendered.get_rect(center=(WIDTH // 2, y))
            self.screen.blit(rendered, rect)
            y += 35

        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type in (pygame.QUIT, pygame.KEYDOWN):
                    waiting = False
            self.clock.tick(60)

        self.running = False
