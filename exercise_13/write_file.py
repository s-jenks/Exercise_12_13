f = open("pelican.txt", "w")
f.write("A wonderful bird is the pelican\n")
f.write("His bill holds more than his belican\n")
f.close()
# open the file to read
f = open("pelican.txt", "r")
print(f.read())
# open the file and appending which allows you to make changes to a file and adds to the end
f = open("pelican.txt", "a")
# \n represents a new line
f.writelines(["He can take in his beak,\n", "Enough food for a week,\n", "But I'm damned if I see how the helican.\n"])
f = open("pelican.txt", "r")
# read allows the text to be outputted in the console
print(f.read())
