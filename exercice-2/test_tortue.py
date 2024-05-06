def test_move_tortue():
  """On teste une classe Tortue(origine_x, origine_y) pourvue des méthodes walk(int), et look_<direction>()
  ainsi que teleport(x, y).

  La tortue est vue de haut comme dans un jeu vidéo et se déplace dans un repère orthonormé
  imaginaire tel que x positif est à droite, y positif est en bas.

  (0,0)              (20,0)
  .                    .



  (0, 5)             (20, 5)
  .                    .

  Implémenter la classe Tortue
  
  Quand on lui dit de regarder dans une direction, elle s'oriente de sorte 
  que quand elle va marcher elle va aller dans cette direction.

  Ainsi, si elle regarde à droite, en marchant sa coordonnée x va augmenter.
  Inversement si elle regarde à gauche elle va diminuer.
  Si elle regarde en bas, y va augmenter et inversement en regardant en haut.

  La tortue est géniale et peut donc se téléporter avec la méthode teleport.
  """
  t = Tortue(x=0, y=0)
  assert t.x == 0 and t.y == 0
  t.look_right()
  t.walk(10)
  assert t.x == 10 and t.y == 0
  t.look_down()
  t.walk(20)
  assert t.x == 10 and t.y == 20
  t.look_left()
  t.walk(4)
  assert t.x == 6 and t.y == 20
  t.look_up()
  t.walk(15)
  assert t.x == 6 and t.y == 5
  t.teleport(21, 42)
  assert t.x == 21 and t.y == 42

class Tortue:
  def __init__(self, x: int, y: int):
    self.x = x
    self.y = y
    self.direction = (0, 0)
  def look_right(self):
    self.direction = (1, 0)

  def look_left(self):
    self.direction = (-1, 0)

  def look_down(self):
    self.direction = (0, 1)

  def look_up(self):
    self.direction = (0, -1)
  
  def teleport(self, x: int, y: int):
    self.x = x
    self.y = y

  def walk(self, steps: int):
    self.x += self.direction[0] * steps
    self.y += self.direction[1] * steps