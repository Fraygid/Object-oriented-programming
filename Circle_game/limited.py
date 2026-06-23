import pgzrun
import random
import math

# === 1. КОНСТАНТЫ ===
TITLE = 'Тык-тык (Рандомный лимит)'
WIDTH = 800
HEIGHT = 600

BACKGROUND_COLOR = (20, 30, 40)
TEXT_COLOR = (220, 220, 220)
SECONDARY_TEXT_COLOR = (200, 200, 200)
HINT_TEXT_COLOR = (180, 180, 200)
HELP_TEXT_COLOR = (160, 160, 180)
GAME_OVER_COLOR = (255, 80, 80)

MIN_SPEED = 1.0
MAX_SPEED = 3.0
MIN_CIRCLES = 3
MAX_CIRCLES = 5

# Диапазон общего количества шаров на игру
MIN_BALLS_IN_GAME = 30
MAX_BALLS_IN_GAME = 50


# === 2. КЛАСС КРУЖОЧКА ===
class Circle:
    def __init__(self):
        self.radius = random.randint(15, 35)
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        self.x = random.randint(self.radius, WIDTH - self.radius)
        self.y = random.randint(self.radius, HEIGHT - self.radius)

        speed = random.uniform(MIN_SPEED, MAX_SPEED)
        angle = random.uniform(0, 2 * math.pi)
        self.dx = math.cos(angle) * speed
        self.dy = math.sin(angle) * speed

        self.is_popping = False
        self.pop_progress = 0.0
        self.pop_speed = 0.2

    def move(self, multiplier):
        if self.is_popping: return

        self.x += self.dx * multiplier
        self.y += self.dy * multiplier

        if self.x - self.radius < 0:
            self.x = self.radius;
            self.dx = -self.dx
        if self.x + self.radius > WIDTH:
            self.x = WIDTH - self.radius;
            self.dx = -self.dx
        if self.y - self.radius < 0:
            self.y = self.radius;
            self.dy = -self.dy
        if self.y + self.radius > HEIGHT:
            self.y = HEIGHT - self.radius;
            self.dy = -self.dy

    def update(self):
        if not self.is_popping: return False
        self.pop_progress += self.pop_speed
        return self.pop_progress >= 1

    def draw(self):
        if not self.is_popping:
            screen.draw.filled_circle((self.x, self.y), self.radius, self.color)
            screen.draw.circle((self.x, self.y), self.radius, (255, 255, 255))
            return

        r = int(self.radius * (1 - self.pop_progress))
        if r < 1: r = 1
        screen.draw.filled_circle((self.x, self.y), r, self.color)

    def is_clicked(self, pos):
        d = math.sqrt((self.x - pos[0]) ** 2 + (self.y - pos[1]) ** 2)
        return d <= self.radius


# === 3. КЛАСС ИГРЫ ===
class Game:
    def __init__(self):
        self.setup_game()

    def setup_game(self):
        self.circles = []
        self.score = 0
        self.speed_multiplier = 1.0

        # Случайное количество шаров от 30 до 50
        self.balls_left = random.randint(MIN_BALLS_IN_GAME, MAX_BALLS_IN_GAME)
        self.total_balls = self.balls_left  # запоминаем для HUD
        self.game_over = False

        start_count = min(random.randint(MIN_CIRCLES, MAX_CIRCLES), self.balls_left)
        for _ in range(start_count):
            self.circles.append(self.spawn_circle())
            self.balls_left -= 1

    def spawn_circle(self):
        return Circle()

    def handle_click(self, pos):
        if self.game_over:
            return

        for circle in self.circles:
            if circle.is_clicked(pos):
                circle.is_popping = True
                self.score += 1
                self.speed_multiplier = 1 + self.score * 0.1
                break

    def update(self):
        if self.game_over:
            return

        new_circles = []
        popped = 0

        for c in self.circles:
            if c.update():
                popped += 1
            else:
                new_circles.append(c)
        self.circles = new_circles

        for _ in range(popped):
            if self.balls_left > 0:
                self.circles.append(self.spawn_circle())
                self.balls_left -= 1

        if len(self.circles) == 0 and self.balls_left == 0:
            self.game_over = True

        for c in self.circles:
            c.move(self.speed_multiplier)

    def draw(self):
        screen.fill(BACKGROUND_COLOR)

        for c in self.circles:
            c.draw()

        screen.draw.text(f'Счет: {self.score}',
                         topleft=(20, 20), fontsize=30, color=TEXT_COLOR)

        # Показываем общее количество шаров в этой игре
        screen.draw.text(f'Всего шаров: {self.total_balls} | В резерве: {self.balls_left}',
                         topright=(WIDTH - 20, 20), fontsize=26, color=SECONDARY_TEXT_COLOR)

        if self.game_over:
            screen.draw.filled_rect(Rect((0, 0), (WIDTH, HEIGHT)), (0, 0, 0, 150))
            screen.draw.text('ИГРА ОКОНЧЕНА',
                             center=(WIDTH // 2, HEIGHT // 2 - 50), fontsize=60, color=GAME_OVER_COLOR)
            screen.draw.text(f'Твой итоговый счет: {self.score}',
                             center=(WIDTH // 2, HEIGHT // 2 + 10), fontsize=40, color=TEXT_COLOR)
            screen.draw.text('Нажми R для новой игры',
                             center=(WIDTH // 2, HEIGHT // 2 + 60), fontsize=30, color=HINT_TEXT_COLOR)
        else:
            screen.draw.text('Нажимай ЛКМ на шарики, чтобы лопать их',
                             center=(WIDTH // 2, HEIGHT - 40), fontsize=24, color=HINT_TEXT_COLOR)
            screen.draw.text('R - новая игра | ESC - выход',
                             center=(WIDTH // 2, HEIGHT - 15), fontsize=20, color=HELP_TEXT_COLOR)


# === 4. ХУКИ PYGAME ZERO (СТРОГО В КОНЦЕ!) ===
game = Game()
def update():
    game.update()

def draw():
    game.draw()

def on_mouse_down(pos, button):
    if button == mouse.LEFT:
        game.handle_click(pos)

def on_key_down(key):
    if key == keys.R:
        game.setup_game()
    elif key == keys.ESCAPE:
        exit()
pgzrun.go()
