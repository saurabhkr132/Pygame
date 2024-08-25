import pygame

pygame.init()

#game-window
screenHeight = 500
screenWidth = 500

# gameIcon = pygame.image.load('D:\Projects\Pygame\snake\gameicon.png')
# pygame.display.set_icon(gameIcon)

pygame.display.set_caption("Saurabh's Game")
win = pygame.display.set_mode((screenHeight,screenWidth))


### fonts ###
font = pygame.font.Font(None, 80)
bFont = pygame.font.Font(None, 30)
scoreFont = pygame.font.Font(None, 25)


# levels-and-pointer
level1 = [7,9,8,8,8,8,8,8,8,8]
level2 = [2,6,4,5,3,0,7,8,4,4]
level3 = [4,5,9,9,3,2,5,2,6,3]
level4 = [9,5,3,9,3,5,6,4,6,1]
level5 = [8,5,8,9,3,0,6,8,6,3]
level6 = [3,6,8,9,3,5,6,7,6,5]
level7 = [7,9,8,8,8,8,8,8,8,8]
# level7 = [2,5,2,9,3,1,6,8,6,7]

levels = [level1,level2,level3,level4,level5,level6,level7]

levelI = 0
current_level = levels[levelI]
pointer = current_level[0]

#game variables
gameOver = False
score = 0
# pos = pygame.mouse.get_pos()

# buttons
nextBText = bFont.render("NEXT",False,(255,255,255))
nextB = nextBText.get_rect(center = (400,450))
previousBText = bFont.render("PREVIOUS",False,(255,255,255))
previousB = previousBText.get_rect(center = (100,450))
resetBText = bFont.render("RESET",False,(255,255,255))
resetB = resetBText.get_rect(center = (270,450))




###########################################  GAME STARTS HERE  ###########################################
while(not gameOver):
  # print("Game Runing")
  game_over = True

  ################## RENDERING ##################

  #level-score-graphics
  scoreText1 = scoreFont.render(f'Levels solved: {score}',False,(255,255,255))
  scoreText = scoreText1.get_rect(center = (400,40))
  levelText1 = scoreFont.render(f'Current level: {levelI + 1}',False,(255,255,255))
  levelText = levelText1.get_rect(center = (100,40))

  # pointer-border
  pygame.draw.rect(win, (0, 0, 100), (((pointer-1)%3)*100+110,((pointer-1)//3)*100+110,80,80))
  pygame.draw.rect(win, (0, 0, 0), (((pointer-1)%3)*100+115,((pointer-1)//3)*100+115,70,70))

  # rendering-numbers
  for i in range(3):
    for j in range(3):
      text = font.render(str(current_level[(i*3)+(j+1)]),False,(0,0,255))
      textRect = text.get_rect(center = (100*(j+1)+50,100*(i+1)+50))
      win.blit(text, textRect)

  # rendering-buttons-and-score
  # win.blit(nextBText, nextB)
  win.blit(nextBText, nextB)
  win.blit(previousBText, previousB)
  win.blit(resetBText, resetB)

  win.blit(scoreText1, scoreText)
  win.blit(levelText1, levelText)
  


  ################### GAME LOGIC ###################
  # button-key-press-event
    # keys = pygame.key.get_pressed()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      print("Game closed! GOOD BYE")
      pygame.quit()

    if event.type == pygame.MOUSEBUTTONDOWN:
        # print(event.pos)
        if nextB.collidepoint(event.pos):
            if levelI < 6:
              print("NEXT LEVEL")
              levelI += 1
              print("LEVEL:", levelI + 1)
              current_level = levels[levelI]
        if resetB.collidepoint(event.pos):
           print("LEVEL RESET")
           current_level = levels[levelI]
            # win.blit(text, textRect)
        if previousB.collidepoint(event.pos):
            if levelI > 0:
              print("PREVIOUS PREVIOUS")
              levelI -= 1
              print("LEVEL:", levelI + 1)
              current_level = levels[levelI]


    # key-press-event
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP and pointer>3:
        pointer -= 3
        print("Up pressed")
        current_level[pointer] += 1
      if event.key == pygame.K_DOWN and pointer<7:
        pointer += 3
        print("Down pressed")
        current_level[pointer] += 1
      if event.key == pygame.K_LEFT and pointer!=1 and pointer!=4 and pointer!=7:
        pointer -= 1
        print("Left pressed")
        current_level[pointer] += 1
      if event.key == pygame.K_RIGHT and pointer!=3 and pointer!=6 and pointer!=9:
        pointer += 1
        print("Right pressed")
        current_level[pointer] += 1
      print("Pointer at", (pointer))

  #### game-over-logic ####
  if(current_level[1] == current_level[2] == current_level[3]== current_level[4] == current_level[5] == current_level[6] == current_level[7] == current_level[8] == current_level[9]):
    gameOver = True
    print("LEVEL COMPLETED!")
    # print(f"Current score: {score}")
    score += 1
    if current_level == level7:
      print("GAME OVER!")


###########################################  GAME OVER  ###########################################
  while(gameOver):
    print()
    ######### rendering-previous-stuffs-dimmed #########
    pygame.draw.rect(win, (0, 0, 70), (((pointer-1)%3)*100+110,((pointer-1)//3)*100+110,80,80))
    pygame.draw.rect(win, (0, 0, 0), (((pointer-1)%3)*100+115,((pointer-1)//3)*100+115,70,70))

    # rendering-numbers
    for i in range(3):
      for j in range(3):
        text = font.render(str(current_level[(i*3)+(j+1)]),False,(0,0,155))
        textRect = text.get_rect(center = (100*(j+1)+50,100*(i+1)+50))
        win.blit(text, textRect)

    # rendering-buttons
    win.blit(nextBText, nextB)
    win.blit(previousBText, previousB)


    ######### rendering-level/game-over-texts #########
    levelCompleteText1 = font.render("Level Completed!",False,(255,255,255))
    levelCompleteText = levelCompleteText1.get_rect(center = (250,250))
    win.blit(levelCompleteText1, levelCompleteText)

    if current_level == level7:
      gameOverText1 = font.render("GAME OVER!",False,(255,255,255))
      gameOverText = gameOverText1.get_rect(center = (250,350))
      win.blit(gameOverText1, gameOverText)
      print("GAME OVER")


    ############# button-key-press-event #############
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        print("Game closed! GOOD BYE")
        pygame.quit()

      if event.type == pygame.MOUSEBUTTONDOWN:
          if nextB.collidepoint(event.pos):
              if levelI < 6:
                print("NEXT")
                levelI += 1
                print(levelI)
                current_level = levels[levelI]
                gameOver = False
          if previousB.collidepoint(event.pos):
              if levelI > 0:
                print("PREVIOUS")
                levelI -= 1
                print(levelI)
                current_level = levels[levelI]
                gameOver = False


    pygame.display.update()
    win.fill((0,0,0))
    




  
  pygame.display.update()
  win.fill((0,0,0))