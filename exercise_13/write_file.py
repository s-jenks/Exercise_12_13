f = open("pelican.txt","w")
f= open("pelican.txt","a")
f.write("A wonderful bird is the pelican\n")
f.write("His bill holds more than his belican")
f.close()

f = open("pelican.txt","r")
print(f.read())

f = open("pelican.txt", "a")
f.writelines(["He can take in his break,\n","Enough food for a week,\n","But I am damned if I see how the helican.\n"])
f= open("pelican.txt","r")
print(f.read())

