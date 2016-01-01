#A mass m = 2 kilograms is attached to the end of a rope of
#length r = 3 meters. The mass is whirled around at high speed.
#The rope can withstand a maximum tension of T = 60 Newtons.
#Write a program that accepts a rotation
#speed v and determines whether such a speed will cause the rope to break.
#Hint: =T mv r 2 .
velocity = float(input("What is the rotation speed?"))
mass = 2
length = 3
Tension = mass*velocity*velocity/length
if Tension >= 60:
    print("The rope will break")
else:
    print("The rope will not break")
