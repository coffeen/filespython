def gap(char):
  print "\n" + char * (80/(len(char))) + "\n"
gap ("#|")

print """
  A while-loop is similar to a for-loop but begins with a
  boolean like an if statement. Python follows the 
  instructions below the while statement and then returns
  to the beginning to see if the while statement is still true. If
  it is True, the instructions are followed again. This continues
  untill the boolean is False. This means a while-loop will 
  continue forever unless it is designed to eventually make the 
  boolean False.
"""

print "Here is a while-loop that will go on forever."

# x = 1
# while x > 0:
#   x = x + 1
#   print "\nx is now %d" % x
#   z = raw_input("""
#     press enter to see the next iteration.
#     hold enter to see what would happen without the raw_input line
#     you have to break this program by pressing Ctrl+C
#     or closing this window.""")

gap("#|")

print """
  You have to comment out the while-loop above to continue. Please
  note a while-loop that doesn't end can be dangerous. 
"""

gap("#|")

print "Here is a similar while-loop that will end."
x = 0
while x < 10:
  print "x is now %d" % x
  x = x + 1

gap("#|")

print """
  while-loops use this 'x = x + 1' so often there is a short-hand: 
  'x += 1' 
  another symbol used in while loops is:
  '!=' which means not equal to
"""

x = 0
power2_list = []

while x != 10:
  powers = 2**x #** means an exponent
  print "2 to the %d power is %d" % (x, powers)
  power2_list.append(powers)
  x += 1
  print power2_list, '\n'





