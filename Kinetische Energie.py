print("if you mass and meters per sec are integers type: 'full'")
print("if you mass and meters per sec are half numbers type: 'half'")
print("if your m/s is an int and your mass is a half num type: 'half_full' ")
print("if your mass is an int and your m/s is a half num type: 'full_half' ")
first_quest = input("Chose your option: ")

if first_quest == 'full':
    x = int(input("Mass: "))
    y = int(input("M/s: "))
    z = 1/2*x*y*y
    print("Your Ekin = : ", z, "joule")

if first_quest == 'half':
    x = float(input("Mass: "))
    y = float(input("M/s: "))
    z = 1/2*x*y*y
    print("Your Ekin = : ", z, "joule")

if first_quest == 'half_full':
    x = int(input("Mass: "))
    y = float(input("M/s: "))
    z = 1/2*x*y*y
    print("Your Ekin = : ", z, "joule")
if first_quest == 'full_half':
    x = float(input("Mass: "))
    y = int(input("M/s: "))
    z = 1/2*x*y*y
    print("Your Ekin = : ", z, "joule")
