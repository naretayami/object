import pgzrun
import random

WIDTH = 300
HEIGHT = 300

def draw():
    screen.fill((128, 0, 0))

alien = Actor('humanpicto')
alien.pos = 100, 56

WIDTH = 500
HEIGHT = alien.height + 20

def draw():
    screen.clear()
    alien.draw()

alien.topright = 0, 10
def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        print("Eek!")
    else:
        print("You missed me!")

pgzrun.go()