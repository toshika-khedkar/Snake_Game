import pygame,sys, random
from pygame.math import Vector2



class SNAKE:
    def __init__(self):
        self.body=[Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction=Vector2(1,0)
        self.new_block=False
    def draw_snake(self):
        for block in self.body:
            x_pos=int(block.x*cell_size)
            y_pos=int(block.y*cell_size)
            block_rect=pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            pygame.draw.rect(screen,(183,111,122),block_rect)
    def move_snake(self):
        if self.new_block==True:
             body_copy=self.body[:]
             body_copy.insert(0,body_copy[0]+self.direction)
             self.body=body_copy[:]
             self.new_block=False
        else:
            body_copy=self.body[:-1]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body=body_copy[:]
    def add_block(self):
        self.new_block = True
        
        
class FRUIT:
    def __init__(self):
        self.randomize()
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x*cell_size),int(self.pos.y*cell_size),cell_size,cell_size) #fruit position in #actuall placing of rect #grid illusion
        # pygame.draw.rect(screen,(126,166,114),fruit_rect)
        screen.blit(apple,fruit_rect)
    def randomize(self):
        self.x=random.randint(0,cell_number-1) # x_pos
        self.y=random.randint(0,cell_number-1) # y_pos
        self.pos=Vector2(self.x,self.y)

class MAIN:
    def __init__(self):
        self.snake=SNAKE()
        self.fruit=FRUIT()
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
           self.fruit.randomize()
           self.snake.add_block()
    def check_fail(self):
        if not 0 <= self.snake.body[0].x< cell_number or not 0<= self.snake.body[0].y< cell_number:
            self.game_Over()
        for block in self.snake.body[1:]:
            if block==self.snake.body[0]:
                self.game_Over()
        
    def game_Over(self):
        pygame.quit()
        sys.exit()
        
        
        
pygame.init();
cell_size=20
cell_number=30
screen=pygame.display.set_mode((cell_number*cell_size, cell_number*cell_size)) #px wt,ht
clock=pygame.time.Clock() #limit to speed for FOR Loop in per sec w,h
# test_surface= pygame.Surface((100,200))#  w,h surface in screeen size
# test_surface.fill((0,0,255))
# test_rect=test_surface.get_rect(center=(200,250)) #(x,y,w,h) not surface
apple= pygame.image.load('Graphics/apple1.jpg').convert_alpha()



SCREEN_UPDATE=pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)


main_game=MAIN()
while True:
    #all elements here
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.QUIT()
          sys.exit() #module 
      if event.type == SCREEN_UPDATE:
          main_game.update()
      if event.type == pygame.KEYDOWN:
          if event.key==pygame.K_UP:
              if main_game.snake.direction.y != 1:
                main_game.snake.direction=Vector2(0,-1)
            #   snake.direction=Vector2(0,-1)
          if event.key==pygame.K_RIGHT:
              if main_game.snake.direction.x != -1:
                main_game.snake.direction=Vector2(1,0)
            #   snake.direction=Vector2(1,0)
          if event.key==pygame.K_DOWN:
              if main_game.snake.direction.y != -1:
                main_game.snake.direction=Vector2(0,1)
            #   snake.direction=Vector2(0,1)
          if event.key==pygame.K_LEFT:
              if main_game.snake.direction.x != 1:
                main_game.snake.direction=Vector2(-1,0)
            #   snake.direction=Vector2(-1,0)
          
    screen.fill((175,215,70))
    main_game.draw_elements()
    # test_rect.right +=1
    # pygame.draw.rect(screen,pygame.Color("red"),test_rect)
    # screen.blit(test_surface,test_rect) # where to display in screen     
    pygame.display.update() #window opens
    clock.tick(60)
    