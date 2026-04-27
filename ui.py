import pygame
import random

WHITE = (240, 240, 240)
BLACK = (10, 10, 10)
GRAY = (140, 140, 140)
GREEN = (120, 220, 120)
DARK_GRAY = (40, 40, 40)
PANEL_BG = (20, 20, 20)
WARNING = (200, 120, 120)

class UI:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("consolas", 22)
        self.small_font = pygame.font.SysFont("consolas", 18)
        self.large_font = pygame.font.SysFont("consolas", 28)

    def draw_text(self, text, y, size="medium", color=WHITE, center=False, x=40, jitter=0):
        font = (
            self.font if size == "medium"
            else self.small_font if size == "small"
            else self.large_font
        )

        rendered = font.render(str(text), True, color)
        rect = rendered.get_rect()

        dx = random.randint(-jitter, jitter) if jitter else 0
        dy = random.randint(-jitter, jitter) if jitter else 0

        if center:
            rect.centerx = self.screen.get_width() // 2 + dx
            rect.y = y + dy
            self.screen.blit(rendered, rect)
        else:
            self.screen.blit(rendered, (x + dx, y + dy))

    def draw_stability_bar(self, stability, x, y, distorted=False):
        width, height = 200, 14
        ratio = max(0, min(1, stability / 100))

        pygame.draw.rect(self.screen, DARK_GRAY, (x, y, width, height), border_radius=3)

        # La barra empieza a mentir si hay distorsión
        if distorted and random.random() < 0.25:
            fake_ratio = max(0, min(1, ratio + random.uniform(-0.15, 0.15)))
            ratio = fake_ratio

        pygame.draw.rect(
            self.screen,
            GREEN,
            (x, y, int(width * ratio), height),
            border_radius=3
        )

    def draw_all(self, state, history, current, questions_asked):
        # Apagón ocasional
        if random.random() < 0.003:
            self.screen.fill(BLACK)
            return

        self.screen.fill(BLACK)
        h = self.screen.get_height()

        # ─────────────── HUD ───────────────
        hud_x, hud_y, hud_w, hud_h = 20, 20, 280, 180

        pygame.draw.rect(self.screen, PANEL_BG, (hud_x, hud_y, hud_w, hud_h), border_radius=6)
        pygame.draw.rect(self.screen, GRAY, (hud_x, hud_y, hud_w, hud_h), 1, border_radius=6)

        self.draw_text(
            "ESTADO DEL SISTEMA",
            hud_y + 10,
            size="small",
            x=hud_x + 20,
            color=GRAY
        )

        distorted_ui = state.distortion > 3

        self.draw_stability_bar(
            state.stability,
            hud_x + 20,
            hud_y + 40,
            distorted=distorted_ui
        )

        self.draw_text(f"Estabilidad: {state.stability}", hud_y + 65, size="small", x=hud_x + 20)
        self.draw_text(f"Distorsión: {state.distortion}", hud_y + 85, size="small", x=hud_x + 20)
        self.draw_text(f"Culpa: {state.blame}", hud_y + 105, size="small", x=hud_x + 20)

        fake_rep = (
            state.repetition + random.randint(3, 8)
            if state.distortion > 4 and random.random() < 0.3
            else state.repetition
        )
        self.draw_text(f"Repetición: {fake_rep}", hud_y + 125, size="small", x=hud_x + 20)

        # ───────────── CONTENIDO ─────────────
        question, options = current
        if state.repetition > 8:
            options = ["Sí", "Sí"]

        jitter = 1 if state.stability < 50 else 0

        content_y = 260

        self.draw_text(
            f"Pregunta #{questions_asked + 1}",
            content_y - 40,
            size="small",
            center=True,
            color=GRAY
        )

        # Mejora clave: la pregunta pierde fuerza mental
        if state.stability > 60:
            q_color = WHITE
        elif state.stability > 30:
            q_color = GRAY
        else:
            q_color = WARNING

        self.draw_text(
            question,
            content_y,
            size="large",
            center=True,
            jitter=jitter,
            color=q_color
        )

        self.draw_text("1) " + options[0], content_y + 110, center=True)
        self.draw_text("2) " + options[1], content_y + 150, center=True)

        # ───────────── FOOTER ─────────────
        self.draw_text(
            "Algunas decisiones no se registran. Otras no se olvidan.",
            h - 40,
            size="small",
            center=True,
            color=GRAY
        )


