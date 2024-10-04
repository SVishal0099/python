pi=22/7
radian = float(input('Radius of sphere: '))
sur_area = 4 * pi * radian **2
volume = (4/3) * (pi * radian ** 3)
print("Surface Area is: ", sur_area)
print("Volume is: ", volume)
# Python3 code to find area
# and total surface area of cube

def areaCube( a ):

    return (a * a * a)
def surfaceCube( a ):
    return (6 * a * a)

a = 5
print("Area =", areaCube(a))
print("Total surface area =", surfaceCube(a))