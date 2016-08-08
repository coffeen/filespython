gap = "\n" + "$" * 80 + "\n"
print gap

print """
  an if-statement looks to a boolean value to see if it is true or false.
  if the boolean is true, python follows the instructions of the indented
  line(s) below. If false, python skips those steps. 
"""

age = int(raw_input("How old are you? > "))

if age > 30:
  print "\nnevermind, you are too old to be trusted."
if age < 30: 
  print "\ngood then let's talk"
print gap

print """
  if the "if-statement" is false and followed by an "else-statement" python 
  will follow the commands after the else-statement
"""

age = int(raw_input("How old are you? > "))

if age > 30:
  print "\nnevermind, you are too old to be trusted."
else: 
  print "\ngood then let's talk"
print gap

print """
  in boolean terms: 
  True and True = True 
  True and False = False
  False and False = False
"""

first = raw_input("first name? > ")
last = raw_input("last name? > ")

if first == "max":
  print "\ncool we have the same name"

if first == "max" and last == "coffeen":
  print "\n...wait, is this identity theft, or what?"
else: 
  print "\nnice to meet you %s %s" % (first, last)
print gap

print """
  in boolean terms: 
  True or True = True
  True or False = True
  False or False = False
"""

answer = raw_input("John has 6 slices of pizza"
  " what percent is left after he eats 3 slices? > ")

if answer == '50%' or answer == '50' or answer == 'fifty':
  print "\ncorrect"
else: 
  print "\nwrong"
print gap

















