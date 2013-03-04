def print_parent_names(parent, firstname, lastname):
	print("Your %s's name is %s %s" % (parent, firstname, lastname))

print("Whose name is this?")
parent_they_gave = input()

print("What's their first name?")
first_name = input()

print("What's their last name?")
last_name = input()

print_parent_names(parent_they_gave, first_name, last_name)
