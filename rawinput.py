print "\nthe raw_input command allows you to gather input from a user"
print "\n\nplease type your name below\n"
name = raw_input()

print "\nhello " + name + " welcome to this script\n"

print "\nyou can also put a string in the raw_input parenthesis for clarity"
print "\nwhat city are you from"
city = raw_input("> ")

print "\n\nso " + name + ", I have never heard of " + city + "...is it nice?"

print "\n\nraw_input can also be used as a stopping point in the program where the user must press enter to continue"
print "\n\nplease press enter to continue"
pause = raw_input()

print "\n\n\tthank you " + name