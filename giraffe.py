class Animals():
	def breathe(self):
		print("breathing")
	def move(self):
		print("moving")
	def eat_food(self):
		print("eating food")

class Mammals(Animals):
	def feed_young_with_milk(self):
		print("feeding young")

class Giraffes(Mammals):
    def __init__(self, spots):
        self.giraffe_spots = spots

    def eat_leaves_from_trees(self):
        print("eating leaves")

    def dance_a_jig(self):
        self.move()
        self.move()
        self.move()
        self.move()

class Rabbits(Mammals):
    def hop_through_forest(self):
        print("hopping through the forest")

class Cats(Mammals):
    def eat_meat(self):
        pass

harold = Giraffes(3)
harold.move()

reginald = Giraffes(88)
harold = Giraffes(456)
reginald.move()
harold.eat_leaves_from_trees()

reginald.breathe()
reginald.eat_food()
reginald.feed_young_with_milk()

def eats_leaves_from_trees(self):
    self.eat_food()

reginald = Giraffes(98)
reginald.dance_a_jig()

ozwald = Giraffes(100)
gertrude = Giraffes(150)
print(ozwald.giraffe_spots)
print(gertrude.giraffe_spots)

class Giraffes:
    def __init__ (self, spots):

