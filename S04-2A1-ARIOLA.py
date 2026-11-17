first = input("First name: ")
last = input("Last name: ")
section = input("Section: ")
subject = input("Favorite subject: ")

name = (first + " " + last).title()

print("Name:", name)
print("Name Code:", name.upper())
print("Section:", section.upper())
print("Favorite Subject:", subject.title())
print("Character Count:", len(name))