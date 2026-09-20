import pygame

# 1. Створюємо вікно гри 600 на 700 пікселів:
window_x = 600
window_y = 700
window = pygame.display.set_mode((window_x, window_y))

# 2. Завантажуємо зображення заднього фону:
background = pygame.image.load("background.png")


# 3. КЛАС: Креслення персонажа-чарівника
class wizard:
    # Атрибути (властивості):
    x = 10
    y = 500
    width = 138
    height = 150
    speed = 4

    # Завантажуємо костюми персонажа:
    main_picture = pygame.image.load("1_IDLE_000.png")
    right_picture = pygame.image.load("3_RUN_000.png")
    left_picture = pygame.image.load("3_RUN_000_l.png")

    # Метод: спокійно стояти і малювати себе
    def stand(self, window):
        window.blit(self.main_picture, (self.x, self.y))

    # Метод: рух праворуч із перевіркою правої межі вікна
    def move_right(self, window, max_width):
        # Якщо правий край чарівника ще не торкнувся правого краю вікна:
        if self.x + self.speed <= max_width - self.width:
            self.x += self.speed
        else:
            self.x = max_width - self.width
        window.blit(self.right_picture, (self.x, self.y))

    # Метод: рух ліворуч із перевіркою лівої межі вікна (0)
    def move_left(self, window):
        if self.x - self.speed >= 0:
            self.x -= self.speed
        else:
            self.x = 0
        window.blit(self.left_picture, (self.x, self.y))

    # Універсальний метод руху за напрямком:
    def move(self, direction, window, max_width):
        if direction == "RIGHT":
            self.move_right(window, max_width)
        elif direction == "LEFT":
            self.move_left(window)
        else:
            self.stand(window)


# 4. ОБ'ЄКТ: Створюємо чарівника
player = wizard()

# Стан гри та напрямок руху ("STOP", "RIGHT", "LEFT")
game_status = True
hero_direction = "STOP"

# Контроль частоти кадрів (щоб рух був плавним):
clock = pygame.time.Clock()

# 5. Головний ігровий цикл:
while game_status:
    # Наклеюємо фон найпершим:
    window.blit(background, (0, 0))

    # Відловлюємо події клавіатури та мишки:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_status = False

        # Натиснули клавішу -> починаємо рух:
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                hero_direction = "RIGHT"
            elif event.key == pygame.K_LEFT:
                hero_direction = "LEFT"

        # Відпустили клавішу -> зупиняємось:
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_RIGHT, pygame.K_LEFT):
                hero_direction = "STOP"

    # Малюємо та переміщуємо чарівника відповідно до поточного стану:
    player.move(hero_direction, window, window_x)

    # Оновлюємо картинку на моніторі:
    pygame.display.update()

    # 60 кадрів на секунду:
    clock.tick(60)

pygame.quit()
