stud_info ={
    "Rajnish Kumar" : 98,
    "Madan Kumar" : 96,
    "Raushan Kumar" : 90,
    "Shobhit Raj" : 70  
}
max =0
str =[]
for i,j in stud_info.items(): # i name and j number
    if(j>max):
        max = j
        str.append(i)
print("Highest marks ",str[-1],":",max)        
    