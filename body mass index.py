name1 = "Shaquille Rashaun O'Neal "
height1 = 2.16
weight1 = 147

def body_mass_index(name, height, weight):
    counting = weight / (height**2)
    print("body mass index: " + name + str(counting))
    if counting <25:
        return name + "Is not overweight"
    else:
        return name + "is overweight "

Shaq = body_mass_index(name1,height1,weight1)

print(Shaq)
