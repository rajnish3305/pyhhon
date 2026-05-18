# Days = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
# Days.discard("Sun") #Remove sunday from set
# print(Days)

DaysA =set(["Mon","Tue","Wed"])
DaysB =set(["Wed","Thu","Fri","Sat","Sun"])
AllDays =DaysA | DaysB # union of two set
print(AllDays)