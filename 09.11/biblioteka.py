#klases nosaukums

class Robots:
  """Klases reprezentā robotu ar specifisko vārdu"""

  #klases konstruktoru. inicializēšana.
  def __init__(self, vards):
    """Datu inicializācija"""
    
    #īpasibu definēšana
    self.vards=vards

    print(f"Incializējam{self.vards}")

  def sasveicinaties(self):
    print(f"Sveiks! Mani sauc{self.vards}")  


#klases pārbaudīšana

#1. robota izveide
rob1 = Robots("R1")

#1. robota metodes pārbaude
rob1.sasveicinaties()
rob1.sasveicinaties()

#2.rob ota izveide
rob2= Robots ("R2")

#2. robota izveide 
rob2.sasveicinaties()
rob2.sasveicinaties()