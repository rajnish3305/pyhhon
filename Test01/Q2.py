a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
sym = input("Enter operation symbol: ")
def operation(a,b,sym):
    if(sym=="+"):
        return a+b
    elif(sym=="-"):
        return a-b
    elif(sym=="*"):
        return a*b
    elif(sym=="/"):
        if(b!=0):
            return a/b
        else:
            return "Not Define"
    elif(sym=="//"):
        if(b!=0):
            return a//b
        else:
            return "Not define"
    elif(sym=="%"):
        return a%b
    elif(sym=="**"):
        return a**b
    else:
        return "Invlid operation"
print(operation(a,b,sym))    