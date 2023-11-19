Rockwall_ha= float(input("enter the rockwall hardness: "))
Carbon_co= float(input("enter the carbon content: "))
tensile_st= float(input("enter the tensile stength: "))

if(Rockwall_ha>50 and Carbon_co>0.7 and tensile_st>5600):
    Grade=10
elif(Rockwall_ha>50 and Carbon_co>0.7):
    Grade=9
elif(Carbon_co>0.7 and tensile_st>5600):
    Grade=8
elif(Rockwall_ha>50 and tensile_st>5600):
    Grade=7
else:
    Grade=0
print("The steal grade is: ", Grade)




