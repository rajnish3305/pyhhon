distance = float(input("Enter distance to travel: "))
budget = int(input("Enter your budget: "))
def suggest_Transport(dis,bud):
    if(dis<=5):
        return "walk"
    elif(bud<=100):
        return "Bus"
    elif(bud>=500):
        return "Flight"
    else:
        return "Taxi"
print(suggest_Transport(distance,budget))    