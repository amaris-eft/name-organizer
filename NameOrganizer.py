#Amaris Efthimiou
#amaris.efthimiou66@myhunter.cuny.edu
#October 6th, 2019
#Name Organizer

b= input("Please enter your list of names: ")
namelist = b.split(";")
nit= ""
for name in namelist:
    pos= int(name.find(', '))
    print(name)
    init = name[pos+2] + '.'
    init = init + " " + name[0:pos]
    print(init)
