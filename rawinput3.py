gap = "\n" + "*" * 80 + "\n"
print gap

print "here is another way to get input from a user"
name = raw_input("name? ")
age = raw_input("age? ")
double_age = age * 2
print "wow, " , age , "is half-way to" , double_age

print gap

print "the int() command converts a numerical string into an integer"
age = int(age)
double_age = age * 2
print "wow, " , age , "is half-way to" , double_age
print gap

print "you can also use raw_input with variables as the prompt."
lie_prompt = "hey %s, whats an age you pretended to be? " % name
lie_age = raw_input(lie_prompt)
print "\ncome on %s, you look more like %r than %r" %(name, age, lie_age)
print "\t** notice that %r can be used for both integers and strings,"
print "\tbut strings are displayed in single quotes"
print gap




