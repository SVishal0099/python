def Convert_Fun(tuple_str):
    result = tuple((int(x[0]), int(x[1]))for x in tuple_str)
    return result
tuple_str = (('333', '33'), ('1416', '55'))
print("Original tuple values:")
print(tuple_str)
print("\nNew tuple values:")
print(Convert_Fun(tuple_str))