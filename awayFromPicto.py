import pgzrun
import random
from random import randint

WIDTH = 800
HEIGHT = 800
TITLE = "A Big Adventure"
time = 0
point = 0


class House(Actor):
    def __init__(self):
        super().__init__("house")
        self.pos = 400, 700

class Human(Actor):
    def __init__(self):
        super().__init__("human")
        self.pos = 400, 600

class Enemy(Actor):
    def __init__(self):
        super().__init__("zombie")
        self.pos = random.randrange(800), random.randrange(800)
        self.dx = random.randrange(21) - 10
        self.dy = random.randrange(21) - 10
    def update(self):
        if self.x >= WIDTH - self.width or self.x <= self.height:
            self.dx = - self.dx
        if self.y >= HEIGHT - self.height or self.y <= self.height:
            self.dy = - self.dy
        self.x = self.x + self.dx
        self.y = self.y + self.dy

class Obstacle(Actor):
    def __init__(self):
        super().__init__("robot_down")
        self.pos = 400, 200
    

class Obstacle2(Actor):
    def __init__(self):
        super().__init__("robot_fall")
        self.pos = 100, 300

ob1 = Obstacle()
ob2 = Obstacle2()
human = Human()                  
house = House()
enemys = [Enemy() for _ in range(5)]
istouch = False

def place_obstracle():
    ob1.x = randint(20, (WIDTH - 20))
    ob1.y = randint(20, (HEIGHT - 20))
    ob2.x = randint(30, (WIDTH - 20))
    ob2.y = randint(30, (HEIGHT - 20))


def draw():
    global time, point, istouch
    screen.fill([255,255,255])
    screen.draw.text("Let's leave the house and on on a big big adventure!!!!!", (10, 10),color="orange")
    screen.draw.text("Time:" + str(time), (10,30), color="black") 
    screen.draw.text("Score:" + str(point), (10,50), color="black")    
    house.draw()
    human.draw()
    ob1.draw()
    ob2.draw()
    for enemy in enemys:
        enemy.draw()
    if istouch == True:
        screen.fill([0,0,0])
        screen.draw.text("Game Over", (220, 300),color="orange",fontsize=100)
        screen.draw.text("Time:" + str(time), (320, 380),color="white",fontsize=70)
        screen.draw.text("Number of people who set out on a big adventure is ...", (40, 450),color="white",fontsize=40)
        screen.draw.text(str(point) + " people", (330, 480),color="white",fontsize=50)

    
def update():
    global istouch, time
    if istouch == True:
        return
    time = time + 1
    for enemy in enemys:
        enemy.update()
        if abs(human.x - enemy.x) <= human.width - 40 and abs(human.y - enemy.y) <= human.height - 40:
            istouch = True
        if abs(human.x - ob1.x) <= human.width - 40 and abs(human.y - ob1.y) <= human.height - 40:
            istouch = True
        if abs(human.x - ob2.x) <= human.width - 40 and abs(human.y - ob2.y) <= human.height - 40:
            istouch = True
    if human.y == 0:
        human.x = house.x
        human.y = house.y - 100
        global point
        point = point + 1
        place_obstracle()
    if keyboard.left:
        house.x -= 2
        human.x -= 2
    if keyboard.right:
        house.x += 2
        human.x += 2
    if keyboard.space:
        human.y -= 2
            

pgzrun.go()