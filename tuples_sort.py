#this is how you sort a list of words from longest to shortest

text = 'coboara in jos luceafar bland'
words = text.split() #we split here the string in a sequence of words
print(words)
d = list() #this is how you create a list
for word in words:
    d.append((len(word), word)) #we create a list with (length and word)
    print(d)
#sorting the d list in reverse
d.sort(reverse = True) #this tells sort to go in degreasing order and sort the d list
print(d)

res = list() #here we create a new list
for length, word in d:
    res.append(word) #we create a condition for length and words in the list to add in the new list only the word
print(res) #printing only the second list
