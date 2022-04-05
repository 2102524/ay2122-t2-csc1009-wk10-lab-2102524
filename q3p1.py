def switch(module):
    moduleInfo={
        "CSC1009": "Object-Oriented Programming",
        "CSC1006": "Mathematics 2",
        "CSC1010": "Computer Networks",
        "CSC1008": "Data Structure"
    }
    return moduleInfo.get(module, "Unknown Module")
module = input("Enter an input: ")
print(switch(module))