# PyGame-Buttons

Easy to use beautiful buttons in pygame.

[Русская версия](README-rus.md)

There is only one class Button. The simpliest example is:

```python
btn = Button(screen, 10, 10, lambda: print('Hello world!'), 'Hello world!')
```

and in main loop methods `handle_event` and `draw` must be called:

```python
while True:
    for event in pygame.event.get():
        btn.handle_event(event)
        if event.type == pygame.QUIT:
            exit()
    btn.draw()
    pygame.display.update()
```

Contructor params:
surface: pygame.Surface instance to display button
x, y: top-left coordinates
click_handler: function that is called when the button is clicked, default is lambda, doing nothing
text: text to display on button
width, height: button size. If not provided, calculated by size of text
color: button color, default is (224, 224, 224)
hover_color: button color when hovered, if None (default), no effect
clicked_color: button color when clicked, if None (default), no effect
border_color, border_width, border_radius - border params
font: text font, pygame.font.Font instance, default is Courier New 20
font_color: default is black

Methods defined:
draw(): draws the button on given surface

handle_event(event): handles mouse events (hover and click). Must be called in main loop.

handle_events(event_list): handles all events in event_list

To check if given point is inside the button, use 'in' operator:
```python
if (x, y) in button: ...
```

For more complicated example see [example.py](example.py).
