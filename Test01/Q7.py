s = input("Enter string: ")
n = int(input("Enter index to remove: "))
s = s[0:n]+s[n+1:len(s)] # remove that index from slicing
print(s)