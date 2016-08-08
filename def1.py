gap = "\n" + "><" * 40 + "\n"
print gap

print"""
  the def function allows you to create a command that is made up of multiple
  commands. The command takes the form 'def command(argument)'. If no argument 
  is needed, it will take the form 'def command()'.
"""

def add():
  print "I can add any two numbers, watch:"
  a = int(raw_input("\ngive me a number > "))
  b = int(raw_input("\ngive me another number > "))
  c = a + b
  print "\nanswer ---> %d" % c

add()

print gap

print """
  the command () can be called anywhere in a script. Usually they are all 
  listed near the top of the script instead of right before they are called.
  The argument in def command(argument) is not needed in many cases, but
  comes in handy when variations on the command are useful. 
"""

def gap(symbol):
  print "\n" + symbol * 80 + "\n"

gap("$")
print "I am above questions and below the money line haha"
gap("?")

print """
  the def command(argument) can be as simple or as complex as it needs to be
  to accomplish a goal. You can use if/elif statements in these defs
  to great effect.
"""

def gap(symbol):
  if len(symbol) == 1:
    print "\n" + symbol * 80 + "\n"
  elif len(symbol) == 2:
    print "\n" + symbol * 40 + "\n"
  elif len(symbol) == 3:
    print "\n" + symbol * 26 + "\n"  
  elif len(symbol) == 4:
    print "\n" + symbol * 20 + "\n"
  else:
    print "\n" + "!" * 80 + "\n"

gap("i")
gap("do")
gap("not")
gap("like")
gap("failure")

print """
  coders are lazy by nature. I stop the above def after four if/elif even 
  though I needed 80 to cover all the possible symbols. Coders also hate messy 
  code; an elegant code(like an elegant theory) is one that accomplishes the 
  most with the fewest number of words or symbols. Here are two 'more elegant'
  versions of the above code. 
"""

def gap(char):
  x = len(char)
  print "\n" + char * (80/x) + "\n"

gap("I")
gap("am")
gap("the")
gap("greatest")

def gap(char):
  print "\n" + char * (80/(len(char))) + "\n"

gap("1")
gap("line")
gap("from")
gap("160")




















