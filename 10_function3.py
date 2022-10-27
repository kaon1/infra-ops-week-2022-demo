# visualize the execution flow of functions

# declare 3 functions
def function_a():
    print("Printing from FUNCTION A")
# calling a function within a function
    function_b()

def function_b():
    print("Printing from FUNCTION B")
    function_c()

def function_c():
    print("Printing from FUNCTION C")

# start
print("Printing from the MAIN function -- This is the start of my execution flow")

function_a()

print("Printing from the MAIN function -- This is the end of my execution flow")