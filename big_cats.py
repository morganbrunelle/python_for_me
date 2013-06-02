#Clone giraffes program for big cats, and have a specific method for each cat, including 4 levels of taxonomy (animalia, mammalia, carivora, feline)

class Animals():
    def have_a_backbone(self):
        print("has a backbone")
    def move(self):
        print("moving")
    def eats(self):
        print("eating")

class Mammals():
    def feeds_babies_with_milk(self):
        print("feeding babies with milk")
    def hair(self):
        print("hairy")
    def endothermic(self):
        print("warm blooded")

class Carnivore():
    def eats_meat(self):
        print("exclusively eating meat")

class Feline():
    def claw_defense(self):
        print("has claws for defense")
    def agile(self):
        print("jumps and lands with extreme ease")

cheetah = Feline()
cheetah.agile()

leopard = Carnivore()
leopard.eats_meat()

class Cheetah():
    def runs_fast(self):
        print("can run up to 73 mph in a single chase!")
    def single_tone_spots(self):
        print("has spots in just one shade--black on a yellow coat")

class Leopard():
    def lives_in_trees(self):
        print("the only big cat that lives in the canopy")
    def hunts_at_night(self):
        print("shy cats that only emerge from the jungle during nighttime")

class Lion():
    def lionness(self):
        print("the females do the hunting")
    def pride(self):
        print("lions live in packs called a pride")

class Tiger():
    def stripes(self):
        print("the only big cats with stripes")
    def big(self):
        print("the biggest species of the big cats")


tayo = Tiger()
tayo.big()

morgies = Lion()
morgies.lionness()
