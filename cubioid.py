width = float(input("enter width: \n"))
height = float(input("enter height: \n"))
length = float(input("enter length: \n"))

volume = width * height * length
print("your cuboid has the volume of", volume, "m^3")

face1 = (width * length) * 2
face2 = (height * length) * 2
face3 = (width * height) * 2

SA = face1 + face2 + face3

print("the total surface area is", SA, "m^2")
