import pygame
from random import randint
import time

#khởi tạo game
pygame.init()

#khai báo màu
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GREY = (210, 210, 210)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
PURPLE = (255, 0, 255)

#tạo cửa sổ
WIDTH = 500
HEIGHT = 500

cuaso = pygame.display.set_mode((WIDTH + 200, HEIGHT)) #2 dấu ngoặc
pygame.display.set_caption('Snake Xenzia')

icon = pygame.image.load(r'D:\bt python 4\mk.png') #nếu không có r thì đổi thành dấu /
pygame.display.set_icon(icon)

fps = 10
block = 25
clock = pygame.time.Clock()

#__________Tạo ô bàn cờ_____________
def caro():
    '''for cot in range(WIDTH//block): #hàng ngang so với màn hình, vẽ theo chiều dọc
        pygame.draw.line(cuaso, BLACK, (cot*block, 0), (cot*block, HEIGHT))

    for hang in range(HEIGHT//block):
        pygame.draw.line(cuaso, BLACK, (0, hang * block), (HEIGHT, hang*block))'''

    for cot in range(WIDTH//block):
        for hang in range(HEIGHT//block):
            
            pygame.draw.rect(cuaso, BLACK, (cot*block, hang*block, block, block),1)
        
        

#____________Tạo Rắn________________
class Snake(pygame.sprite.Sprite):
    duoi = []
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.surf = pygame.Surface((block, block))
        self.surf.fill(RED)
        self.rect = self.surf.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.state = 'start'

    def move(self):
        if self.state == 'up':
            self.rect.y -= block

        elif self.state == 'down':
            self.rect.y += block

        elif self.state == 'left':
            self.rect.x -= block

        elif self.state == 'right':
            self.rect.x += block

    def cham_khung(self):
        if self.rect.x <-10:
            self.rect.x = WIDTH 

        if self.rect.x > WIDTH :
            self.rect.x = 0

        if self.rect.y < -10:
            self.rect.y = HEIGHT

        if self.rect.y > HEIGHT :
            self.rect.y = 0


#__________Tạo đuôi rắn______________
class Snaketail(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((block,block))
        self.surf.fill(BLUE)
        self.rect = self.surf.get_rect(topleft = (-25,-25))




        
#________________Tạo Food_____________
class Food(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.surf = pygame.Surface((block, block))
        self.surf.fill(BLUE)
        self.rect = self.surf.get_rect(topleft = (((randint(0, ((WIDTH - block)//block)))*block), ((randint(0, ((HEIGHT - block)//block))) *block)))
        self.x = x 
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y

    def food_location(self):
        pass

    def update(self):
        self.rect.x = (randint(0,((WIDTH - block)//block)))*block
        self.rect.y = (randint(0,((HEIGHT - block)//block)))*block
        




#===================CHƯƠNG TRÌNH CHÍNH======================
ran = Snake(100,100)
food = Food(250,150)
score = 0
highscore = 0
def Score():
    global score
    font = pygame.font.SysFont('Arial Bold', 35)
    text_score = font.render('Score: ' + str(score), True, BLACK)
    cuaso.blit(text_score, (540, 50))

def HighScore():
    global highscore
    font = pygame.font.SysFont('Arial Bold', 35)
    text_highscore = font.render("Highscore" + str(highscore), True, BLACK)
    cuaso.blit(text_highscore, (560, 50))
    f = open('highscore.txt', 'r', encoding = 'utf-8')
    data = f.read()
    f.close()



run = True

while run:
    clock.tick(fps)
    cuaso.fill((WHITE))
    caro()
    Score()
    HighScore()
    

    
    #các sự kiện
    for event in pygame.event.get():
        if event.type  == pygame.QUIT:
            run = False
            print('quit:' + str(len(ran.duoi)))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ran.state != 'down'
                ran.state = 'up'
                     

            elif event.key == pygame.K_DOWN:
                ran.state != 'up'
                ran.state = 'down'


            elif event.key == pygame.K_RIGHT:
                ran.state != 'left'
                ran.state = 'right'

            elif event.key == pygame.K_LEFT:
                ran.state != 'right'
                ran.state = 'left'

    ran.move()
    ran.cham_khung()
        #hiển thị rắn
    cuaso.blit(ran.surf, ran.rect)
    cuaso.blit(food.surf, food.rect)

    
    for i in ran.duoi:
        cuaso.blit(i.surf, i.rect)

    if pygame.sprite.collide_rect(ran,food):
        food.update()
        new = Snaketail()
        ran.duoi.append(new)
        score += 10
        if score > highscore:
            highscore = score
            f = open('highscore.txt', 'w')
            f.write(str(highscore))
            f.close()
        f = open('highscore.txt', 'r')
        data1 = f.read()
        print(data1)

    #Di chuyển đuôi theo thứ tự ngược lại (lấy vị trí cuối cùng)
    for i in range(len(ran.duoi) -1, 0, -1):
        x = ran.duoi[i-1].rect.x
        y = ran.duoi[i-1].rect.y
        ran.duoi[i].rect.x = x
        ran.duoi[i].rect.y = y

    #cho đuôi theo đầu
    if len(ran.duoi)> 0:
        x = ran.rect.x
        y = ran.rect.y
        ran.duoi[0].rect.x = x
        ran.duoi[0].rect.y = y

        
    if len(ran.duoi) >2:
        for i in range(len(ran.duoi)):
            if i == 0:
                continue
            
            if ran.duoi[i].rect.x == ran.rect.x and ran.duoi[i].rect.y == ran.rect.y:
                ran.state = 'start'
                ran.rect.x = (randint(0, ((WIDTH - block)//block)))*block
                ran.rect.y = (randint(0, ((HEIGHT - block)//block)))*block
                
                food.update()
                time.sleep(3)
                score = 0
                #print('collide: ' + str(len(ran.duoi)))
                ran.duoi.clear()
                break
                


    pygame.display.update() #pygame.display.flip()
pygame.quit()
























