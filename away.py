import pgzrun
import random


WIDTH = 800
HEIGHT = 800
TITLE = "Away from Pictogram"
time = 0

px = 400
py = 400
tx=px
ty=py
   
# プレイヤークラス（Actorクラスを継承）

class Player(Actor):
    def __init__(self):
        super().__init__("humanpicto")
        self.pos = px, py

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

               
player = Player()
enemys = [Enemy() for _ in range(5)]
istouch = False

def on_mouse_move(pos):
    player.pos = pos
 
def draw():
    global time
    screen.fill([255,255,255])
    screen.draw.text("Time:" + str(time), (10,10), color="black")    
    screen.draw.circle((10,10,10),(tx,ty),5)
    player.draw()
    for enemy in enemys:
        enemy.draw()
    
def update():
    global istouch, time
    if istouch == True:
        return
    time = time + 1
    for enemy in enemys:
        enemy.update()
        if abs(player.x - enemy.x) <= player.width - 5 and abs(player.y - enemy.y) <= player.height - 10:
            istouch = True

pgzrun.go()



