class Character:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed
        
    def DoubleStats(self):
        self.health *= 2
        self.damage *= 2
        self.speed *= 2
        
class Brute(Character):
    def Potion(self):
        self.health += 50
class Ninja(Character):
    def Boost(self):
        self.speed += 5
        

Brute_1 = Brute(200, 50, 10)
Ninja_1 = Ninja(100, 20, 50)

print("Brute stats: ", Brute_1.health, Brute_1.damage, Brute_1.speed)
print("Brute used a potion!")
Brute_1.Potion()
print("Brute new stats: ", Brute_1.health, Brute_1.damage, Brute_1.speed)
Brute_1.DoubleStats()
print("Brute used Double Stats! New stats: ", Brute_1.health, Brute_1.damage, Brute_1.speed)