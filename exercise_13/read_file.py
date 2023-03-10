f = open("pelican.txt", "r")  # we are opening the file and reading the file.
# this is a file handle which has access to the file
print(f.read())  # This gives us what is inside the file
print(type(f))  # Text IO Wrapper which is a input and output class

list = open("pelican.txt").readlines()  # We created a variable called list to read each line and create a list
print(list)
print(len(list))  # This returned the items in our list

for x in list:  # a for loop to iterate through the list
    print(x.strip())  # This prints the list without any blanks using the strip method
