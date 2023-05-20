  if playerPos == 'l' and playerX > 0.5*boundaryD1:
    playerX -= 1
  if playerPos == 'r' and playerX < screenWidth - 3*(playerWidth - boundaryD1):
    playerX += 1
  if playerPos == 'u' and playerY > 1.5*boundaryD1:
    playerY -= 1
  if playerPos == 'd' and playerY < screenHeight - 3*(playerWidth - boundaryD1):
    playerY += 1