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
# level2 = [2,6,4,5,3,5,7,8,4,4]
# level3 = [4,5,8,9,3,5,6,8,6,3]

current_level = level1
pointer = current_level[0]


while(True):
  #game-quit
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      # run = False
      pygame.quit()

  game_over = False


  if pointer==1:
    pygame.draw.rect(win, (0, 0, 100), (110,110,80,80))
  if pointer==2:
    pygame.draw.rect(win, (0, 0, 100), (210,110,80,80))
  if pointer==3:
    pygame.draw.rect(win, (0, 0, 100), (310,110,80,80))
  if pointer==4:
    pygame.draw.rect(win, (0, 0, 100), (110,210,80,80))
  if pointer==5:
    pygame.draw.rect(win, (0, 0, 100), (210,210,80,80))
  if pointer==6:
    pygame.draw.rect(win, (0, 0, 100), (310,210,80,80))
  if pointer==7:
    pygame.draw.rect(win, (0, 0, 100), (110,310,80,80))
  if pointer==8:
    pygame.draw.rect(win, (0, 0, 100), (210,310,80,80))
  if pointer==9:
    pygame.draw.rect(win, (0, 0, 100), (310,310,80,80))



  text = font.render(str(current_level[1]),False,(0,0,255))
  textRect = text.get_rect(center = (150,150))
  win.blit(text, textRect)

  text = font.render(str(current_level[2]),False,(0,0,255))
  textRect = text.get_rect(center = (250,150))
  win.blit(text, textRect)

  text = font.render(str(current_level[3]),False,(0,0,255))
  textRect = text.get_rect(center = (350,150))
  win.blit(text, textRect)

  text = font.render(str(current_level[4]),False,(0,0,255))
  textRect = text.get_rect(center = (150,250))
  win.blit(text, textRect)

  text = font.render(str(current_level[5]),False,(0,0,255))
  textRect = text.get_rect(center = (250,250))
  win.blit(text, textRect)

  text = font.render(str(current_level[6]),False,(0,0,255))
  textRect = text.get_rect(center = (350,250))
  win.blit(text, textRect)

  text = font.render(str(current_level[7]),False,(0,0,255))
  textRect = text.get_rect(center = (150,350))
  win.blit(text, textRect)

  text = font.render(str(current_level[8]),False,(0,0,255))
  textRect = text.get_rect(center = (250,350))
  win.blit(text, textRect)

  text = font.render(str(current_level[9]),False,(0,0,255))
  textRect = text.get_rect(center = (350,350))
  win.blit(text, textRect)

  

  keys = pygame.key.get_pressed()
  if keys[pygame.K_UP] and pointer>3:
    pointer -= 3
    current_level[pointer] += 1
  if keys[pygame.K_DOWN] and pointer<7:
    pointer += 3
    current_level[pointer] += 1
  if keys[pygame.K_RIGHT] and pointer!=3 and pointer!=6 and pointer!=9:
    pointer += 1
    current_level[pointer] += 1
  if keys[pygame.K_LEFT] and pointer!=1 and pointer!=4 and pointer!=7:
    pointer -= 1
    current_level[pointer] += 1
  

  pygame.display.update()
  win.fill((0,0,0))