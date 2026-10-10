class demo:
    a = 4

o = demo()
print(o.a) ## Print the class attribute because instance attribute is not present
o.a = 0 #Instance attribute is set
print(o.a) ## Prints the insrance attribute because instance attribute is present
print(demo.a) ## Print the class attribute