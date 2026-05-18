test_str = 'gfg_is_best_for_geeks'
print("The original string is : " + str(test_str))
delim = "_"
temp = test_str.split(delim)
print(temp)
res = dict()
for idx, ele in enumerate(temp):
    res[idx] = ele
print("Dictionary after splits ordering : " + str(res))
print(type(res))