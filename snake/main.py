import pygame
import random

pygame.init()

screenHeight = 700
screenWidth = 700

win = pygame.display.set_mode((screenHeight, screenWidth))

gameIcon = pygame.image.load('D:/Projects/Pygame/snake2/gameicon.png')
pygame.display.set_icon(gameIcon)
pygame.display.set_caption("Snake2.0")

clock = pygame.time.Clock()

scoreFont = pygame.font.Font(None, 25)
gameFont = pygame.font.Font(None, 50)

snakeBody = [(20 * (random.randint(0, int(screenHeight / 20) - 1)), 20 * (random.randint(0, int(screenWidth / 20) - 1)))]  # Initial position of the snake
snakeVel = 20  # The movement velocity in pixels (aligned with the grid)


foodWidth = 20
foodHeight = 20
foodX = 20 * random.randint(0, int(screenHeight / 20) - 1)
foodY = 20 * random.randint(0, int(screenWidth / 20) - 1)
foodColor = (255, 0, 0)

ip = 0  # keyboard input: 1->UP, 2->RIGHT, 3->DOWN, 4->LEFT
score = 0 # Score
gameOverMenu = 1

gameOver = False
Run = True
paused = False

# Did snake eat himself
def snakeAte(body):
    return len(body) != len(set(body))

while Run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_w or event.key == pygame.K_UP) and ip != 3:
                ip = 1
                print("UP input")
            elif (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and ip != 4:
                ip = 2
                print("RIGHT input")
            elif (event.key == pygame.K_s or event.key == pygame.K_DOWN) and ip != 1:
                ip = 3
                print("DOWN input")
            elif (event.key == pygame.K_a or event.key == pygame.K_LEFT) and ip != 2:
                ip = 4
                print("LEFT input")
            elif (event.key == pygame.K_p or event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE):  # Press 'P' to pause/unpause
                paused = not paused
    
    if not paused:  # Move the snake's head
      headX, headY = snakeBody[0]
      if ip == 1:  # UP
          headY -= snakeVel
      elif ip == 2:  # RIGHT
          headX += snakeVel
      elif ip == 3:  # DOWN
          headY += snakeVel
      elif ip == 4:  # LEFT
          headX -= snakeVel

      # Insert new position of the head
      newHead = (headX, headY)
      # Check for game over
      if(snakeAte(snakeBody) or headX < 0 or headX > screenWidth or headY < 0 or headY > screenHeight):
        gameOver = True
      snakeBody.insert(0, newHead)

      # print("headX: ", headX,"headY: ", headY)
      # print(snakeBody)

      

      # Check if food is eaten
      if foodX == headX and foodY == headY:
          score += 1
          print("Score: ", score)
          foodX = 20 * random.randint(0, int(screenHeight / 20) - 1)
          foodY = 20 * random.randint(0, int(screenWidth / 20) - 1)
      else:
          # Remove the last segment of the snake's body to maintain the length
          snakeBody.pop()

      # Clear the screen
      win.fill("black")

      # Draw the snake
      for segment in snakeBody:
          pygame.draw.rect(win, (173, 216, 230), (*segment, 20, 20))
          pygame.draw.rect(win, (20, 10, 250), (segment[0] + 2.5, segment[1] + 2.5, 15, 15))

      # Display the score
      scoreText = scoreFont.render(f'Score: {score}',False,(111,196,169))
      scoreTextRect = scoreText.get_rect(center = (50,12))
      win.blit(scoreText, scoreTextRect)
      
      # Draw the food
      pygame.draw.rect(win, foodColor, (foodX, foodY, foodWidth, foodHeight))

    else:
      # Display pause message
      font = pygame.font.Font(None, 74)
      text = font.render("Paused", True, (255, 255, 255))
      win.blit(text, (screenWidth // 2 - text.get_width() // 2, screenHeight // 2 - text.get_height() // 2))
       
    # Update the display
    pygame.display.update()

    ####################### GAME-OVER #######################
    while gameOver == True:
      print("Game Over!")


      for segment in snakeBody:
        pygame.draw.rect(win, (173, 216, 230), (*segment, 20, 20))
        pygame.draw.rect(win, (20, 10, 250), (segment[0] + 2.5, segment[1] + 2.5, 15, 15))
      pygame.draw.rect(win, (255, 0, 0), (foodX,foodY,foodWidth,foodHeight))

      scoreText = gameFont.render(f'Your score is {score}',False,(111,196,169))
      scoreTextRect = scoreText.get_rect(center = (screenWidth/2,screenHeight/3.2))

      restartText = gameFont.render("RESTART",False,(0,0,255))
      restartTextRect = restartText.get_rect(center = (screenWidth/2,screenHeight/2.5))

      quitText = gameFont.render("QUIT",False,(0,0,255))
      quitTextRect = quitText.get_rect(center = (screenWidth/2,screenHeight/2))

      gameOverText = gameFont.render("Game Over!",False,(111,196,169))
      gameOverTextRect = gameOverText.get_rect(center = (screenWidth/2,screenHeight/1.6))

      ######## GAMEOVER-MENUS ########
      ######## toggle-menus ########
      keys = pygame.key.get_pressed()
      if (keys[pygame.K_UP] or keys[pygame.K_w]) and gameOverMenu == 2:
        gameOverMenu = 1
        win.fill((0,0,0))
      if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and gameOverMenu == 1:
        gameOverMenu = 2
        win.fill((0,0,0))
      
      ######## menu-boxes ########
      if gameOverMenu==1:
        pygame.draw.rect(win, (0, 0, 100), (screenWidth/2.7,screenHeight/2.7,180,50))
        if keys[pygame.K_RETURN]:
          snakeBody = [(20 * (random.randint(0, int(screenHeight / 20) - 1)), 20 * (random.randint(0, int(screenWidth / 20) - 1)))]
          Run = True
          gameOver = False
          score = 0
          break
      if gameOverMenu==2:
        pygame.draw.rect(win, (0, 0, 100), (screenWidth/2.7,screenHeight/2.15,180,50))
        if keys[pygame.K_RETURN]:
          pygame.quit()
      
      ######## gameover-messages ########
      win.blit(gameOverText, gameOverTextRect)
      win.blit(scoreText, scoreTextRect)
      win.blit(restartText, restartTextRect)
      win.blit(quitText, quitTextRect)

      pygame.display.update()
      
      ######## game-quit ########
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          # Run = False
          pygame.quit()

    # Control the frame rate
    clock.tick(5)  # FPS
