gap = "\n" + "$" * 80 + "\n"
print gap

print "the boolean '==' tests the truth of a given condition\n"
print "green" == "green"
print 20 == 19
x = 9
print x == 9
print "god" == "God"
print "\t** notice that boolean values are case-sensitive"
print gap

print """
  lets combine some stuff we've learned to create a test for the user
  that can be graded automatically
"""
print gap

print "\t***  are you smart?  let's see  ***\n\n"
print "please type a single word that best answers each of the following\n"
answers = []
answers.append(raw_input("\nwhat color does chlorophyl make plants? > "))
answers.append(raw_input("\nwhat body sits at the center of our solar system? > "))
answers.append(raw_input("\nwhat is the largest ocean? > "))
answers.append(raw_input("\nwhat is the smallest continent? > "))
answers.append(raw_input("\nwhat is the capital of arizona? > "))
key = ['green', 'sun', 'pacific', 'australia' , 'phoenix',]

print gap
pause = raw_input("press enter to see your results")
print gap
print """
  Thanks for taking the test. Here are your results
"""
for i in range(len(key)):
  print i + 1 , "you said %r The correct answer was %r" % (answers[i], key[i])
  print "\n\n\t were you correct?--->", answers[i] == key[i] , "\n\n"
  pause = raw_input("press enter to see your results")
print gap










