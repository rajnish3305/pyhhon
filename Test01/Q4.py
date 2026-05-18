name = "My name is ! . ? Rajnish kumar"
for p in "!,?.":
    name = name.replace(p,"")#replace all inneccesary thing into " "
    
lowercase = name.lower() # all character change to small alphabet

words = lowercase.split() # split sentance into words and store in list word (excluding spacing)
print("Total Words",len(words))

sum =0
for i in words:
    sum = sum +len(i)
print("Total Character(excluding spaces): ",sum) # total chracter in sentace calcuated by length of each word   

s = ""
for i in words:
    if(len(s)<len(i)):
        s = i
print(s)  # return longest words      
