pyg = 'ay'

original = raw_input('Enter a word:')
word = original.lower()
first = original[0]
new_word = word[1:len(word)] + first + pyg


if len(original) > 0 and original.isalpha():
    print new_word
elif not original.isalpha():
    print "please don't use numbers or punctuation."
else:
    print 'empty'
