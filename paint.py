"""Paint, for drawing shapes.

Exercises

1. Add a color.-Iñaki
2. Complete circle. -Edrick
3. Complete rectangle.-Iñaki
4. Complete triangle.-Iñaki
"""

from turtle import *

from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    """Draw circle from start to end."""
    begin_fill()
    turtle.speed(15)
    for i in range(40):
        turtle.forward(100)
        turtle.right(90)
        for j in range(1):
                turtle.forward(100)
                  turtle.right(80)
    pass  # TODO


def rectangle(start, end):#hace rectángulo alto
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for count in range(4):
        forward(end.x - start.x)
        if count%2==1:
            forward((end.x-start.x)/2)
        left(90)
    end_fill()
    pass  # TODO


def triangle(start, end): #hace triángulo equilátero
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for count in range(3):
        forward(end.x - start.x)
        left(120)
    end_fill()
    pass  # TODO


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('yellow'), 'Y') #agregué el amarillo
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: grosor('10'), 'Q')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
