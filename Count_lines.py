"""
fname = input("Enter file name: ")
try:
    fh = open(fname,'r')
    print("Seccessed")
except:
    print("Failed")
    quit()
list_conf = list()
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
         continue
    list_conf.append(float(line[20:]))
res = sum(list_conf)/len(list_conf)
print("Average spam confidence: {}".format(res))
"""

fname = input("Enter file name: ")
if len(fname) < 1: fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    if not line.startswith("From "):
        continue
    lst = line.split()
    print(lst[1])
print("There were", count, "lines in the file with From as the first word")
