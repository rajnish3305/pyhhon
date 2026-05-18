str ="python programming language is a hard language"
s = str.split()
dic = {}
for i in s:
    dic[i] = dic.get(i,0)+1
for key,value in dic.items():
    print(key,":",value)
print("\n")     
for key,value in sorted(dic.items()): #sorted manner me print
    print(key,":",value)  
             