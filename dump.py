# # class Employee:
# #     n = 0
# #
# #     def __init__(self, emp_id):
# #         self.i = emp_id
# #
# #
# # x = Employee(15)
# #
# # print("Employee is ", callable(Employee))
# # print("x is ", callable(x))
# 
# 
# class Person:
#     person_id = 0
#     person_name = ""
# 
#     def __init__(self, personid, personname):
#         self.person_id = personid
#         self.person_name = personname
# 
#     def __call__(self, *args, **kwargs):
#         print("Args:")
#         print(*args)
# 
#         print("Kwargs:")
#         for key, value in kwargs.items():
#             print("%s == %s" % (key, value))
# 
# m = Person(15, "Gleb")
# 
# print(m)
# 
# print("Person object is", callable(m))
# m("adsfad", p="sdfasd")

class LengthStr:
    
    def __init__(self, text):
        self.text = text
        self.length = len(text)

    def __str__(self):
        return self.text

    def __call__(self, *args, **kwargs):
        return self.length


line = LengthStr("Gleb")
print(f"String {line} contains {line()} symbols.")