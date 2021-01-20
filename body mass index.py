name1 = "Shaquille Rashaun O'Neal "
height1 = 2.16
weight1 = 45

def body_mass_index(name, height, weight):
    counting = weight / (height**2)
    print("body mass index: " + name + str(counting))
    if counting <25:
        return name + "Is not overweight"
    else:
        return name + "Overweight, pre-obese "

Shaq = body_mass_index(name1,height1,weight1)

print(Shaq)
