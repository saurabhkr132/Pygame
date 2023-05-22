import pygame

pygame.init()

#game-window
screenHeight = 500
screenWidth = 500

# gameIcon = pygame.image.load('D:\Projects\Pygame\snake\gameicon.png')
# pygame.display.set_icon(gameIcon)

pygame.display.set_caption("Saurabh's Game")
win = pygame.display.set_mode((screenHeight,screenWidth))

font = pygame.font.Font(None, 80)


level1 = [7,1,2,3,4,5,6,7,8,9]
level2 = [2,6,4,5,3,5,7,8,4,4]
level3 = [4,5,8,9,3,5,6,8,6,3]

current_level = level1
pointer = current_level[0]

#game variables
gameOver = False


while(not gameOver):

  game_over = True

  # pointer-border
  pygame.draw.rect(win, (0, 0, 100), (((pointer-1)%3)*100+110,((pointer-1)//3)*100+110,80,80))
  pygame.draw.rect(win, (0, 0, 0), (((pointer-1)%3)*100+115,((pointer-1)//3)*100+115,70,70))

  # rendering-numbers
  for i in range(3):
    for j in range(3):
      text = font.render(str(current_level[(i*3)+(j+1)]),False,(0,0,255))
      textRect = text.get_rect(center = (100*(j+1)+50,100*(i+1)+50))
      win.blit(text, textRect)
  

  # key-press-event
    # keys = pygame.key.get_pressed()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      # run = False
      pygame.quit()

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP and pointer>3:
        pointer -= 3
        print("up pressed")
        current_level[pointer] += 1
      if event.key == pygame.K_DOWN and pointer<7:
        pointer += 3
        print("down pressed")
        current_level[pointer] += 1
      if event.key == pygame.K_LEFT and pointer!=1 and pointer!=4 and pointer!=7:
        pointer -= 1
        print("left pressed")
        current_level[pointer] += 1
      if event.key == pygame.K_RIGHT and pointer!=3 and pointer!=6 and pointer!=9:
        pointer += 1
        print("right pressed")
        current_level[pointer] += 1
      print("Pointer at", (pointer))
  
  pygame.display.update()
  win.fill((0,0,0))