from turtle import *
import random

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()
    tim.color(R, G, B)

def tick():
    for action in keys_pressed:
        actions[action]()
        
    update()
    screen.ontimer(tick, frame_delay_ms)

tim = Turtle()
tim.width(3)
tim.pencolor('white')

tracer(0)
frame_delay_ms = 1000 // 30 # default for turtle is 10 in _CFG["delay"]
steps = 10

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

actions = dict(
    a=lambda: tim.left(steps),
    d=lambda: tim.right(steps),
    w=lambda: tim.forward(steps),
    s=lambda: tim.backward(steps),
    c=lambda: clear_screen(),
    f=lambda: change_color(),
)

screen = Screen()
screen.bgcolor('black')
screen.setup(1600, 900)
screen.title('Rainbow Etch A Sketch')

keys_pressed = set()

screen.onkeypress(lambda: keys_pressed.add("w"), "w")
screen.onkeypress(lambda: keys_pressed.add("a"), "a")
screen.onkeypress(lambda: keys_pressed.add("d"), "d")
screen.onkeypress(lambda: keys_pressed.add("s"), "s")
screen.onkeypress(lambda: keys_pressed.add("c"), "c")
screen.onkeypress(lambda: keys_pressed.add("f"), "f")

screen.onkeypress(key="q", fun=tim.penup)
screen.onkeypress(key="e", fun=tim.pendown)

screen.onkeyrelease(lambda: keys_pressed.remove("w"), "w")
screen.onkeyrelease(lambda: keys_pressed.remove("a"), "a")
screen.onkeyrelease(lambda: keys_pressed.remove("d"), "d")
screen.onkeyrelease(lambda: keys_pressed.remove("s"), "s")
screen.onkeyrelease(lambda: keys_pressed.remove("c"), "c")
screen.onkeyrelease(lambda: keys_pressed.remove("f"), "f")

screen.listen()
tick()
screen.exitonclick()