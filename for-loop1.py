gap = "\n" + "#" * 80 + "\n"
print gap

print "lists of strings are stored in variables like this: fish = ['tuna', 'salmon', 'carp']"
fish = ['tuna', 'salmon', 'carp']
print fish

print "calling a certain item on the list is done like this: fish[1]"
print fish[1]
print "\t**notice, the first element in the list is number 0"
print gap

print "a for-loop can be used to move through a list"
for element in fish:
  print "some fish are %s" %element
print gap

print "lists of numbers are stored like this: fives = [5, 10, 15, 20, 25, 30]"
fives = [5, 10, 15, 20, 25, 30]
for i in fives:
  print i
print gap

print "the append function can be used to combine lists"
fish.append(fives)
print fish
print fish[1]
print fish[3]
print gap

print "append can be combined with a for-loop to make a list from a list"
integers = [1,2,3,4,5,6,7,8,9,10]

twos = []
for i in integers:
  twos.append(i*2)

threes = []
for i in integers:
  threes.append(i*3)

fives = []
for i in integers:
  fives.append(i*5)

print twos
print threes
print fives
print gap

print "you can even put lists into lists and for-loops into for-loops!"
counts = [twos,threes,fives]
for each in counts:
  print "\nlook ma, I can count by multiples"
  for i in each:
    print i















