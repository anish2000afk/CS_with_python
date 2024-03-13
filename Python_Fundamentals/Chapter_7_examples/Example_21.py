import math
len = float(input("Enter the lenght of the ladder : "))
ang = float(input("Enter the angle of lean(in degrees) : "))
rad_ang = math.radians(ang) # Conversion to radians
height = len * math.sin(rad_ang) # Usign sin on the radians
print("Length of the ladder : ", len,"feet")
print("Angle of lean in radians : ", rad_ang,"radians")
print("Height reached by the ladder : ", height,"feet")

