import pgzrun
import random

WIDTH = 800
HEIGHT = 800
TITLE = "A Big Adventure"
time = 0
point = 0

# プレイヤークラス（Actorクラスを継承）
class House(Actor):
    def __init__(self):
        super().__init__("humanpicto")
        self.pos = 400, 700

class Human(Actor):
    def __init__(self):
        super().__init__("humanpicto")
        self.pos = 400, 600
    
# エネミークラス（Actorクラスを継承）
class Enemy(Actor):
    def __init__(self):
        super().__init__("humanpicto")
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
        super().__init__("humanpicto")
        self.pos = 400, 200

class Obstacle2(Actor):
    def __init__(self):
        super().__init__("humanpicto")
        self.pos = 100, 300

ob1 = Obstacle()
ob2 = Obstacle2()
human = Human()                  
house = House()
enemys = [Enemy() for _ in range(5)]
istouch = False

# RED = 200, 0, 0
# BOX = Rect((20, 20), (100, 100))

# def on_mouse_move(pos):
#     player.pos = pos

def draw():
    global time, point
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
    # screen.draw.circle((400, 400), 30, 'yellow')
    # screen.draw.text("hello world", (20, 100),color="orange")
    
       
def update():
    if human.y == 0:
        human.x = house.x
        human.y = house.y - 100
        global point
        point = point + 1
    if keyboard.left:
        house.x -= 2
        human.x -= 2
    if keyboard.right:
        house.x += 2
        human.x += 2
    if keyboard.space:
        human.y -= 2

    global istouch, time
    if istouch == True:
        return
    time = time + 1
    for enemy in enemys:
        enemy.update()
        if abs(human.x - enemy.x) <= human.width - 5 and abs(human.y - enemy.y) <= human.height - 10:
            istouch = True
        if abs(human.x - ob1.x) <= human.width and abs(human.y - ob1.y) <= human.height:
            istouch = True
        if abs(human.x - ob2.x) <= human.width and abs(human.y - ob2.y) <= human.height:
            istouch = True

pgzrun.go()


# 画像を変える
# 位置を変える