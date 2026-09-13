import pygame

# 1. Створюємо вікно гри 600 на 700 пікселів:
window_x = 600
window_y = 700
window = pygame.display.set_mode((window_x, window_y))

# 2. Завантажуємо зображення заднього фону:
background = pygame.image.load("background.png")

game_status = True

# 3. Головний ігровий цикл:
while game_status:
    # Наклеюємо фон у координати (0, 0) найпершим:
    window.blit(background, (0, 0))

    # Відловлюємо закриття вікна на хрестик:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_status = False

    # Оновлюємо картинку на моніторі:
    pygame.display.update()
