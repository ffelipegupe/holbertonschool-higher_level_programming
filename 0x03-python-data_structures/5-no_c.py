#!/usr/bin/python3
def no_c(my_string):
    l_string = list(my_string)
    str = ""
    if "c" in l_string:
        l_string.remove("c")
    if "C" in l_string:
        l_string.remove("C")
    str = str.join(l_string)
    return str

#my_string = "C is fun"
#l = list(my_string)
#print("c" in l)
#l.remove("c")
#l.remove("C")
#s = ""
#s = s.join(l)
#print(my_string)
#print(s)
print(no_c("Holberton School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
