class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self):
        print("move")
    def draw(self):
        print("draw")

class Czlowiek:
    def __init__(self,wiek):
        self.wiek = wiek
    def przywitanie(self):
        print(f"Witaj masz : {self.wiek}")
Czlowiek1 = Czlowiek(21)
Czlowiek1.przywitanie()