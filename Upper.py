fname = input("Enter the name of file: ")
try:
    file = open(fname,'r')
except:
    print("Error opening file!")
    quit()
text = ""
for line in file:
    text += line.upper()
print(text)
