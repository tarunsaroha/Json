# import json
# json_obj =  '{ "Name":"David", "Class":"I", "Age":6 }'
# python_obj = json.loads(json_obj)
# print("\nJSON data:")
# print(python_obj)
# print("\nName: ",python_obj["Name"])
# print("Class: ",python_obj["Class"])
# print("Age: ",python_obj["Age"])






# import json
# python_obj = {
#   "name": "David",
#   "class":"I",
#   "age": 6  
# }
# j_data = json.dumps(python_obj)
# print(j_data)







# import json
# python_obj={
#     "name":"tarun",
#     "class":"I",
#     "age":"18"
# }
# j_str=json.dumps(python_obj)
# print(j_str)






# import json
# j_str = {'4': 5, '6': 7, '1': 3, '2': 4}
# print("Original String:")
# print(j_str)
# print("\nJSON data:")
# print(json.dumps(j_str, sort_keys=True, indent=4))






# import json
# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None)) 






# import json

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
# print(json.dumps(x))



# import json
# x =  '{ "name":"John", "age":30, "city":"New York"}'
# y = json.loads(x)
# print(y["age"]) 



