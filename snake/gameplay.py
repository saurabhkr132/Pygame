#importing-libraries
import pygame
import random

pygame.init()

#game-window
screenHeight = 500
screenWidth = 500

gameIcon = pygame.image.load('D:\Projects\Pygame\snake\gameicon.png')
pygame.display.set_icon(gameIcon)

pygame.display.set_caption("Saurabh's Game")
win = pygame.display.set_mode((screenHeight,screenWidth))

#boundary-variables
boundaryD1 = 10
boundaryD2 = 500
boundaryColor = (150,75,0)

#player-variables
playerX = random.randint(10*boundaryD1,screenHeight-10*boundaryD1)
playerY = random.randint(2*boundaryD1,screenWidth-4*boundaryD1)
playerWidth = 15
playerHeight = 15
#player = pygame.transform.scale(player,(50,100))
#player_rect = player.get_rect(midbottom = (100,365))
playerVel = 0.02
playerPos = 'r'
playerColor = (255,0,0)
# playerLength = 1

#food-variables
foodX = random.randint(5.0*boundaryD1,screenHeight-2.0*boundaryD1)
foodY = random.randint(2.0*boundaryD1,screenWidth-4.0*boundaryD1)
foodWidth = 15
foodHeight = 15
foodColor = (0,255,0)

#gameplay-variables
run = True
score = 0
startScreen = True
gameStartMenu = 1
gameOverMenu = 1

scoreFont = pygame.font.Font(None, 20)
gameFont = pygame.font.Font(None, 50)

# restart = pygame.image.load('D:/Projects/Pygame/snake/restarticon.jpg').convert_alpha()
# restart = pygame.transform.scale(restart,(20,20))
# restartRect1 = restart.get_rect(midbottom = (20,205))


  
############################################## GAMEPLAY ##############################################
while run:
##### WELCOME SCREEN #####
  while(startScreen):
    gameOverText = gameFont.render("Welcome to",False,(111,196,169))
    gameOverTextRect = gameOverText.get_rect(center = (250,100))

    creditText = gameFont.render("Saurabh's Game",False,(111,196,169))
    creditTextRect = creditText.get_rect(center = (250,160))
    startText = gameFont.render("START",False,(0,0,255))
    startTextRect = startText.get_rect(center = (250,260))

    quitText = gameFont.render("QUIT",False,(0,0,255))
    quitTextRect = quitText.get_rect(center = (250,320))

  ### GAMEOVER-MENUS ####
    #toggle-menus
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and gameStartMenu == 2:
      gameStartMenu = 1
      win.fill((0,0,0))
    if keys[pygame.K_DOWN] and gameStartMenu == 1:
      gameStartMenu = 2
      win.fill((0,0,0))
    
    #menu-boxes
    if gameStartMenu==1:
      pygame.draw.rect(win, (0, 0, 100), (160,230,180,50))
      if keys[pygame.K_RETURN]:
        break
    if gameStartMenu==2:
      pygame.draw.rect(win, (0, 0, 100), (160,295,180,50))
      if keys[pygame.K_RETURN]:
        pygame.quit()
      
    #gameover-messages
    win.blit(gameOverText, gameOverTextRect)
    win.blit(creditText, creditTextRect)
    win.blit(startText, startTextRect)
    win.blit(quitText, quitTextRect)
    
    pygame.display.update()

    #game-quit
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        # run = False
        pygame.quit()
  



# ####################### GAME STARTS HERE #######################
  startScreen = False

  #game-quit
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
      pygame.quit()

  #drwaing-stuff
  pygame.draw.rect(win, playerColor, (playerX,playerY,playerWidth,playerHeight))
  pygame.draw.rect(win, foodColor, (foodX,foodY,foodWidth,foodHeight))
  pygame.draw.rect(win, boundaryColor, (0,0,boundaryD1,boundaryD2))
  pygame.draw.rect(win, boundaryColor, (screenWidth-boundaryD1,0,boundaryD1,boundaryD2))
  pygame.draw.rect(win, boundaryColor, (0,screenHeight-boundaryD1,boundaryD2,boundaryD1))
  pygame.draw.rect(win, boundaryColor, (0,0,boundaryD2,2.5*boundaryD1))

  scoreText = scoreFont.render(f'Score: {score}',False,(111,196,169))
  scoreTextRect = scoreText.get_rect(center = (450,12))
  win.blit(scoreText, scoreTextRect)

  # win.blit(restart, (395,3))
  # restartRect1


  #game-over
  if playerX < boundaryD1 or playerX > (screenWidth - 2*boundaryD1) or playerY < 2*boundaryD1 or playerY > (screenHeight - 2*boundaryD1):
    run = False

  #eating-food
  if playerX in range(foodX-1,foodX) and playerY in range(foodY-1,foodY):
    score = score + 1
    foodX = random.randint(5*boundaryD1,screenHeight-2*boundaryD1)
    foodY = random.randint(2*boundaryD1,screenWidth-4*boundaryD1)

  #checking-key-condition
  keys = pygame.key.get_pressed() 
  if playerPos == 'l' and playerX > 0.5*boundaryD1:
    playerX -= playerVel
  if playerPos == 'r' and playerX < screenWidth - 3*(playerWidth - boundaryD1):
    playerX += playerVel
  if playerPos == 'u' and playerY > 1.5*boundaryD1:
    playerY -= playerVel
  if playerPos == 'd' and playerY < screenHeight - 3*(playerWidth - boundaryD1):
    playerY += playerVel

  # playerX += 0.02
  
  #detecting-key-press
  if keys[pygame.K_LEFT]:
    playerPos = 'l'

  if keys[pygame.K_RIGHT]:
    playerPos = 'r'

  if keys[pygame.K_UP]:
    playerPos = 'u'

  if keys[pygame.K_DOWN]:
    playerPos = 'd'

  #display-update
  pygame.display.update()



# ####################### GAME-OVER #######################
  if run == False:
    while True:
      pygame.draw.rect(win, (128,0,0), (playerX,playerY,playerWidth,playerHeight))
      pygame.draw.rect(win, (144, 238, 144), (foodX,foodY,foodWidth,foodHeight))
      pygame.draw.rect(win, (196, 164, 132), (0,0,boundaryD1,boundaryD2))
      pygame.draw.rect(win, (196, 164, 132), (screenWidth-boundaryD1,0,boundaryD1,boundaryD2))
      pygame.draw.rect(win, (196, 164, 132), (0,screenHeight-boundaryD1,boundaryD2,boundaryD1))
      pygame.draw.rect(win, (196, 164, 132), (0,0,boundaryD2,2.5*boundaryD1))

      gameOverText = gameFont.render("Game Over!",False,(111,196,169))
      gameOverTextRect = gameOverText.get_rect(center = (250,100))

      scoreText = gameFont.render(f'Your score is {score}',False,(111,196,169))
      scoreTextRect = scoreText.get_rect(center = (250,160))

      restartText = gameFont.render("RESTART",False,(0,0,255))
      restartTextRect = restartText.get_rect(center = (250,260))

      quitText = gameFont.render("QUIT",False,(0,0,255))
      quitTextRect = quitText.get_rect(center = (250,320))

      #### GAMEOVER-MENUS ####
      #toggle-menus
      keys = pygame.key.get_pressed()
      if keys[pygame.K_UP] and gameOverMenu == 2:
        gameOverMenu = 1
        win.fill((0,0,0))
      if keys[pygame.K_DOWN] and gameOverMenu == 1:
        gameOverMenu = 2
        win.fill((0,0,0))
      
      #menu-boxes
      if gameOverMenu==1:
        pygame.draw.rect(win, (0, 0, 100), (160,230,180,50))
        if keys[pygame.K_RETURN]:
          run = True
      if gameOverMenu==2:
        pygame.draw.rect(win, (0, 0, 100), (160,295,180,50))
        if keys[pygame.K_RETURN]:
          pygame.quit()
      
      #gameover-messages
      win.blit(gameOverText, gameOverTextRect)
      win.blit(scoreText, scoreTextRect)
      win.blit(restartText, restartTextRect)
      win.blit(quitText, quitTextRect)

      pygame.display.update()
      
      #game-quit
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          # run = False
          pygame.quit()

  #filling windows
  win.fill((0,0,0))
  

  

