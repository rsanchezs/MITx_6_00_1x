from getpass import _raw_input

def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count
count = occurrences("azcbobobegghakl", "bob")
print (count)
s = _raw_input("Enter a string:")
count = 0
start = 0
for letter in s:
    start = s.find("bob", start) + 1
    if start > 0:
        count += 1
print ("Number of times bob occurs is:", count)
