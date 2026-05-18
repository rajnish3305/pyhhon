# number = [1,2,3,4,5,6,7,8]
# number1=[1,2,3,4,5,6,7,8]
# add = list(map(lambda x,y: x+y, number,number1))
# print(add)

# num = [1,2,3]
# sqr = list(map(lambda x:x*x,num))
# print(sqr)


# num = [1,2,3]
# def cube(i):
#     return i**3
# num2 = list(map(cube,num))
# print(num2)

# num = [1,2,3,4,5,6,7,8]
# def is_even(i):
#     if(i%2==0):
#         return i
#     else:
#         return 0
# num2 = list(map(is_even,num))
# print(num2)


# from functools import reduce
# num = [1,2,3,4,5,6,7,8]
# def add(x,y):
#     return x+y
# num1 = reduce(add,num)
# print(num1)

lt = [1,3,4,5,6]
it = iter(lt)
print(next(it))
print(next(it))


