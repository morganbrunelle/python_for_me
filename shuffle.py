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

    def move_foot(self, foot_side, direction):
        print(foot_side + " foot " + direction)

    def dance(self):
        self.move_foot("left", "forward")
        self.move_foot("left", "back")
        self.move_foot("right", "forward")
        self.move_foot("right", "back")

reginald = Giraffes(800)
reginald.dance()
