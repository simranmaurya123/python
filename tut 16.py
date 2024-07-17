# list1=[["luna",56],["harry",90],["hee",78],["dom",76]]
# dict1=dict(list1)
#
# for item in dict1:
#     print(item)

# for item,lolly in dict1.items():
#     print(item,lolly)
list1=["fairy",45,97,3,2,5,"hello","bye"]
for item in list1:
 if str(item).isnumeric() and item>6:
    print(item)