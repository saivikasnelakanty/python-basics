class Parent:
    def __init__(self, first_name, middle_name, last_name):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
    def get_address(self, address):
        return(address + ", India")
obj_parent = Parent("Bhaddir","raju","Nelakanty")
print(obj_parent.first_name, obj_parent.middle_name, obj_parent.last_name)

class ChildOne(Parent): #inheritance
    pass
obj_child = ChildOne("Sai","vikas", "Nelakanty")
print(obj_child.first_name, obj_child.middle_name, obj_child.last_name)
print(obj_child.get_address("hyderabad"))

class ChildTwo(Parent): #inheritance
    pass
obj_child_two = ChildTwo("Raja","vijay", "Nelakanty")
print(obj_child_two.first_name, obj_child_two.middle_name, obj_child_two.last_name)
print(obj_child_two.get_address("Rajahmundry"))

#Parent Class "name"
# Child Class "cat" & "dog"
# Module Name : Animal inheritance

