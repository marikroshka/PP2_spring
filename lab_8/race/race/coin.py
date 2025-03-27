import settings
import obstacle

class Coin(obstacle.Obstacle):
  def __init__(self):
    super().__init__(20, 1, "C:/Users/User/Documents/PPSPRING/py/pp2-main/lab 8/race/race/images/coin.png", settings.SPEED)
