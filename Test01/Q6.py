n = input("Enter string: ") # string is immutable not chande or update
def swep(n):
    
    if len(n)<2:
        return n
    else:
        return n[len(n)-1] + n[1:len(n)-1] +n[0] # slicing kar ke add kar do
    
    
print(swep(n))    