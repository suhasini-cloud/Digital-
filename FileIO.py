f = open("demotext", "r")
print(f.read())

f = open("demotext", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demotext", "r")
print(f.read())

f = open("demotext.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demotext.txt", "r")
print(f.read())