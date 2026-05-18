# DaysA =set(["Mon","Tue","Wed"])
# DaysB =set(["Wed","Thu","Fri","Sat","Sun"])
# AllDays =DaysA & DaysB # intersection of two set
# print(AllDays)

# DaysA =set(["Mon","Tue","Wed"])
# DaysB =set(["Wed","Thu","Fri","Sat","Sun"])
# AllDays =DaysA - DaysB # jo bas DaysA me ho element
# print(AllDays)

DaysA =set(["Mon","Tue","Wed"])
DaysB =set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
SubsetRes = DaysA <= DaysB # means ki all element of set A present in set B ---true/false
SupersetRes = DaysB >= DaysA # kiya daysB is superset of DaysA ---> true/false
print(SubsetRes)
print(SupersetRes)

