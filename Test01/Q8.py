def case_str(str1):
    result_str = ""
    for item in str1:
        if item.isupper():
            result_str += item.lower()
        else:
            result_str += item.upper()
    return result_str  
print(case_str("Python Exercise"))
print(case_str("Java"))
print(case_str("NumPy"))  
            
    