print ("Enter your name ")
name1 = str(input())
print ("Enter your height ")
height1 = float(input())
print ("Enter your weight ")
weight1 = int(input())

def body_mass_index(name, height, weight):
    counting = weight / (height**2)
    print(" body mass index: "+ name    + "=" + str (counting))
    if counting <25:
        return name + " You are not overweight "
    else:
        return name + " you are overweight, it's time to lose some weight "

someone = body_mass_index(name1, height1, weight1)
print (someone)
