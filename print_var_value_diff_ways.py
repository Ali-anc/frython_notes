fav_car = "audi"
print ("my fav car is " + fav_car)
#Combines two strings manually. Only works on string, might run into issues if the var was number
print ( "my fav car is {}" .format(fav_car) )
# Good for inserting multiple variables: print("I like {} and {}".format("BMW", "Audi"))
print ("my fav car is %s" %fav_car)
# The %s is a placeholder for a string. A bit older method
print (f"my fav car is {fav_car}")
#f-string (formatted string literal)
