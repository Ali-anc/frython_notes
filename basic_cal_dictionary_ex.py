person = input ("What mathematical operator would like to you? \n Ex: '+ - % * ^ /' : ")
x = float (input("input your first digit: "))
y = float (input("input your second digit: "))

# The following are prompt var used to next steps

ops = {
    
    "+": x + y
}

# ops is dictionary (in Python is like a lookup table).You give it a key, and it gives you a value.
# If person is "+", it returns x + y. Further ex below
'''
operations = {"+": 5, "-": 3}
person = "+"          # valid key
result = operations.get(person, "Invalid operator")  # returns 5

person = "^"          # invalid key
result = operations.get(person, "Invalid operator")  # returns "Invalid operator"
'''

results = ops.get(person, "invalid operator")
## Couple things to understand ##

# new var called results which gives whats inside the dictionary
# ops.get(person) - looks in lookup to find the value that matches the key stored in person.
print (results)
