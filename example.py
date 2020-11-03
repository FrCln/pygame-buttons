import pygame

from button import Button


def click():
    print('Hello world!')


pygame.init()
screen = pygame.display.set_mode((400, 400))

btn = Button(
    screen,
    10,
    10,
    click,
    text='Hello world!',
    color=(200, 200, 200),
    hover_color=(235, 146, 37),
    clicked_color=(213,23,23),
    border_radius=5,
    border_width=2
)

clock = pygame.time.Clock()

try:
    while True:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            btn.handle_event(event)
            if event.type == pygame.QUIT:
                exit()
        btn.draw()
        pygame.display.update()

        clock.tick(30)
finally:
    pygame.quit()
