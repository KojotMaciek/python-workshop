def point(x, y, *, z=0): # The * indicates the end of the positional arguments. Every argument after that can only be specified by keyword
    return (x, y, z)

print(point(1, 2))
print(point(z=1, x=2, y=3))

def steps(*s):
    for step in s:
        print(step)

steps(1, 3, 4, "NN", 7, "LM")

"""
The steps() function in the code uses the star (*) operator to receive an unrestricted number of arguments. Similarly, we can pass an extensive series of parameters in a function using this operator without actually typing them in the function declaration statement.
"""
def directions(max_x, max_y, x, y, direction, *commands):
    return (max_x, max_y, x, y, direction, commands)

print(directions(10, 15, 7, 4, "S", 1, 2, 3))

def task_star(**x): # key, value to define
    for step in x:
        print(step) # prints only key
    for k, v in x.items():
        print(k, " = ", v) # prints key and value 

task_star(a=5, b=2)