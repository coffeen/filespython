gap = "\n" + "*" * 80 + "\n"
print gap

print"""
  when a decision involes more than two independent choices, the command
  'elif' (else/if) can be used. Python will check the if statement 
  then each elif statement in order. If any are true, it will do the commands
  and skip the rest. If none of the if or elif's are true it will follow the 
  else command(s). 
"""

print "let's play roguish rochambeau:"
pick = raw_input("\ntype your choice (rock/paper/scissors) to begin\n:")

if pick.lower() == "rock":
  print "slap paper covers rock... you lose sucker"

elif pick.lower() == "paper":
  print "snip your paper got cut... don't try to come at me with paper bitch"

elif pick.lower() == "scissors":
  print "bam your scissors got crushed by my rock... loser"

else: 
  print "\n%r, really?! I guess you are too afraid or too stupid to pick" % pick
  print "rock paper or scissors"
print gap

print """
  it is also possible to put if/elif statements inside of other if/elif 
  statements. 
"""

age = float(raw_input("how old are you > "))
gender = raw_input("male or female > ")
smoking = raw_input("do you smoke? >")

if gender.lower() == "m" or gender.lower() == "male":
  if smoking.lower() == "yes" or smoking.lower() == "y":
    print "you have about %s years left to live." % (70.1 - age)
  elif smoking.lower() == "no" or smoking.lower() == "n":
    print "you have about %s years left to live." % (80.1 - age)
  else:
    print "sorry %r is not recognized, please type 'yes' or 'no'" % smoking


elif gender.lower() == "f" or gender.lower() == "female":
  if smoking.lower() == "yes" or smoking.lower() == "y":
    print "you have about %s years left to live." % (68.7 - age)
  elif smoking.lower() == "no" or smoking.lower() == "n":
    print "you have about %s years left to live." % (78.7 - age)
  else:
    print "sorry %r is not recognized, please type 'yes' or 'no'" % smoking
else:
  print "sorry %r is not recognized, please type 'male' or 'female'" % gender












