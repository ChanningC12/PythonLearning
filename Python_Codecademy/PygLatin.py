print ("Pig Latin")
print ("Welcome to the Pig Latin Translator!")

original = input("Name:")
if len(original)>0 and original.isalpha():
    print ("original")
else:
    print ("empty")



pyg='ay'

dropbox=input('Enter a word:')
if len(dropbox)>0 and dropbox.isalpha():
    print (dropbox)
word=dropbox.lower()
first="dropbox"[0]
newword=word+first+pyg
new_word=newword[0:]
print (word)
print (first)
print (new_word)
