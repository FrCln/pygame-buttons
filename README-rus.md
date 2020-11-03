# PyGame-Buttons

Простые и симпатичные кнопочки для pygame.

Объявлен один класс Button. Пример создания простой кнопки:

```python
btn = Button(screen, 10, 10, lambda: print('Hello world!'), 'Hello world!')
```

после чего в главном цикле следует вызывать методы `handle_event` и `draw` :

```python
while True:
    for event in pygame.event.get():
        btn.handle_event(event)
        if event.type == pygame.QUIT:
            exit()
    btn.draw()
    pygame.display.update()
```

Параметры конструктора:
surface: объект pygame.Surface, на котором будет расположена кнопка
x, y: координаты левого верхнего угла
click_handler: функция, которая будет вызвана при нажатии на кнопку. По умолчанию - lambda-функция, которая ничего не делает
text: текст на кнопке, по умолчанию нет
width, height: Размер кнопки. Если не указан, рассчитывается исходя из размера текста
color: цвет кнопки, по умолчанию (224, 224, 224)
hover_color: цвет кнопки при наведении мыши
clicked_color: цвет кнопки при щелчке
border_color, border_width, border_radius - параметры рамки
font: text шрифт, объект pygame.font.Font, по умолчанию Courier New 20
font_color: по умолчанию черный

Методы:
draw(): рисует кнопку

handle_event(event): обрабатывает событие (наведение или щелчок мыши)

handle_events(event_list): обрабатывает список событий

Чтобы проверить, попадает ли точка внутрь кнопки можно использовать оператор `in`:
```python
if (x, y) in button: ...
```

Более подробный пример см. в файле [example.py](example.py).
