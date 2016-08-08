def gap(char):
  print "\n" + char * (80/(len(char))) + "\n"

gap("$")

def rochambeau():
  gap("-----><----")
  print "\t\t\_/ let's play roguish rochambeau \_/"
  pick = raw_input("\n\t\ttype your choice(rock/paper/scissors) to begin\n\n\t"
    "\t\t\t> ")

  if pick.lower() == "rock":
    print "slap paper covers rock... you lose sucker"
    again = raw_input("\nplay again? (y/n)")
    if again.lower() == "y" or again.lower() == "yes":
      rochambeau()
    else:
      print "\n\t\t\tthanks for losing"
  elif pick.lower() == "paper":
    print "snip your paper got cut... don't try to come at me with paper bitch"
    again = raw_input("\nplay again? (y/n)")
    if again.lower() == "y" or again.lower() == "yes":
      rochambeau()
    else:
      print "\n\t\t\tthanks for losing"
  elif pick.lower() == "scissors":
    print "bam your scissors got crushed by my rock... loser"
    again = raw_input("\nplay again? (y/n)")
    if again.lower() == "y" or again.lower() == "yes":
      rochambeau()
    else:
      print "\n\t\t\tthanks for losing"
  else: 
    print "\n%r, really?! I guess you are too afraid or too stupid to pick" % pick
    print "rock paper or scissors"
    again = raw_input("\nplay again? (y/n)")
    if again.lower() == "y" or again.lower() == "yes":
      rochambeau()
    else:
      print "\n\t\t\tthanks for losing"

rochambeau()
gap("-----><----")



