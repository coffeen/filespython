print "\nhere is another way to collect info with raw_input\n"
first = raw_input("first name >")
last = raw_input("last name >")
eyes = raw_input("eye color >")
weight = raw_input("weight >")
add = raw_input("size >")

print "\n\nhello " + first + last + ", I like your" + eyes +"eyes. I bet you weight about" + weight + "and you have a" + add + "dick"

print "\n\tthese plus signs can get to be too much, commas can be used instead"
print "\nhello " , first , last , ", I like your" , eyes , "eyes. I bet you weigh about"  , weight , "and you have a" , add , "dick"

print "\n\n\tconcatenating variables into strings is tedious, the percent sign can help"
print "\tpercent s is a symbol that indicates to python that a string variable %s should be inserted" % first

print "\n\tnow our code becomes"
print "hello %s %s, I like your %s eyes. I bet you weight about %s. I bet you have a %s dick" % (first, last, eyes, weight, add)

print "\nthis system may not seem much better now, but there is something to be said for having all"
print "the variables at the end so you don't have to search through the text to find which are being called\n"

print "\nnotice that weight is a number, but %s calls it as a string. raw_input stores all input as strings"
print eyes * 3
print weight * 3




